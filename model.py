import torch, segmentation_models_pytorch as smp

def load_model(weights="watermark_model.pth"):
    ckpt = torch.load(weights, map_location="cpu")
    ckpt = {k.replace("model.", "", 1): v for k, v in ckpt.items()}
    model = smp.create_model(
        arch="UnetPlusPlus",
        encoder_name="resnet34",
        in_channels=3,
        classes=1,
        encoder_weights=None
    )
    model.load_state_dict(ckpt, strict=False)
    model.eval()
    return model

MODEL = load_model()
