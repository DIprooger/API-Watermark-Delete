import cv2
import numpy as np
import io
import torch
from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import StreamingResponse
from model import MODEL
from security import verify_token

app = FastAPI(title="Watermark Cleaner API")

TARGET = (512, 512)
_mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
_std  = np.array([0.229, 0.224, 0.225], dtype=np.float32)

def process(raw: bytes) -> bytes:
    arr = np.frombuffer(raw, np.uint8)
    img_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    orig_h, orig_w = img_bgr.shape[:2]

    # ресайз к модели
    img_res = cv2.resize(img_bgr, TARGET)

    # нормализация и предсказание
    img_rgb = cv2.cvtColor(img_res, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
    img_norm = (img_rgb - _mean) / _std
    input_tensor = torch.from_numpy(img_norm.transpose(2, 0, 1)).unsqueeze(0)

    with torch.no_grad():
        logits = MODEL(input_tensor)
        mask_prob = torch.sigmoid(logits)[0, 0].cpu().numpy()
    mask_bin = (mask_prob > 0.5).astype(np.uint8) * 255

    # пост‑процесс
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    mask_clean = cv2.dilate(
        cv2.morphologyEx(mask_bin, cv2.MORPH_CLOSE, kernel),
        kernel, iterations=1
    )

    clean = cv2.inpaint(img_res, mask_clean, 3, cv2.INPAINT_TELEA)

    # масштабируем обратно
    clean_orig = cv2.resize(clean, (orig_w, orig_h))
    _, png = cv2.imencode(".png", clean_orig)
    return png.tobytes()

@app.post("/clean", dependencies=[Depends(verify_token)])
def clean(file: UploadFile = File(...)):
    raw = file.file.read()
    result = process(raw)
    return StreamingResponse(
        io.BytesIO(result),
        media_type="image/png",
        headers={"Content-Disposition": 'inline; filename="cleaned.png"'},
    )
