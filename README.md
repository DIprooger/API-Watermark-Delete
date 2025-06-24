<details> <summary>🇷🇺 Русский</summary>

# API-Watermark-Delete
FastAPI is an application for removing watermarks. It features a trained model for finding and creating masks.

🧼 Watermark Cleaner API

Watermark Cleaner — это FastAPI-приложение, которое использует нейросетевую модель Unet++ для автоматического удаления водяных знаков с изображений.

🚀 Возможности

- Принимает изображение (формат: PNG, JPEG) через POST-запрос.
- Выдаёт результат с удалённым водяным знаком.
- Защита API через токен.
- Поддержка запуска в Docker.

📦 Быстрый старт (через Docker)

1. Склонируйте репозиторий:
```
   git clone git@github.com:DIprooger/API-Watermark-Delete.git
   cd API-Watermark-Delete
```
2. Создайте `.env` файл с переменной токена:
```
   TOKEN=your_secret_token
```
3. Запустите контейнер:
```
   docker-compose up --build
```
4. API будет доступно по адресу:
```
   http://localhost:8886/clean
```
🧪 Пример использования (curl)
```
curl -X POST http://localhost:8886/clean \
  -H "Authorization: Bearer your_secret_token" \
  -F "file=@path_to_image.jpg" \
  --output cleaned.png
```
🔐 Авторизация

Каждый запрос к `/clean` требует токен авторизации. Он указывается в `.env` как:
```
TOKEN=your_secret_token
```
В запросе используется заголовок:
```
Authorization: Bearer your_secret_token
```
🧠 Модель

Модель использует:
- Архитектуру: Unet++
- Энкодер: resnet34
- Реализация: segmentation_models_pytorch

В папке присутствуют файлы с весами:
- watermark_model.pth
- watermark_model_0.1.pth
- watermark_model_0.2.pth
- watermark_model_0.3.pth

По умолчанию загружается watermark_model.pth. Другие — возможные версии или эксперименты.

📁 Структура проекта

.<br>
├── Dockerfile <br>
├── docker-compose.yml <br>
├── main.py              # Точка входа FastAPI<br>
├── model.py             # Загрузка нейросетевой модели<br>
├── security.py          # Проверка токена<br>
├── watermark_model*.pth # Веса модели<br>
├── requirements-runtime.txt<br>
└── .env

⚙️ Зависимости

Указаны в requirements-runtime.txt. Устанавливаются автоматически при сборке Docker-образа.

📌 TODO

- Документация по каждому весу модели.
- Интерфейс загрузки изображений через веб.
- Поддержка изображений большего размера.

🛡️ Лицензия

Укажите лицензию здесь, если она применима.

📬 Обратная связь

Pull requests и предложения приветствуются!


</details> <details> <summary>🇬🇧 English</summary>

# API-Watermark-Delete

FastAPI application for removing watermarks from images using a trained neural network model to detect and mask them.

🧼 Watermark Cleaner API

Watermark Cleaner is a FastAPI application that uses a Unet++ neural network to automatically remove watermarks from images.

🚀 Features

- Accepts image input (formats: PNG, JPEG) via POST request.
- Returns an image with the watermark removed.
- Token-based API authentication.
- Docker support for easy deployment.

📦 Quick Start (via Docker)

1. Clone the repository:
```
   git clone git@github.com:DIprooger/API-Watermark-Delete.git
   cd API-Watermark-Delete
```
2. Create a `.env` file with the token:
```
   TOKEN=your_secret_token
```
3. Run the container:
```
   docker-compose up --build
```
4. The API will be available at:
```
   http://localhost:8886/clean
```
🧪 Example usage (curl)
```
curl -X POST http://localhost:8886/clean \
  -H "Authorization: Bearer your_secret_token" \
  -F "file=@path_to_image.jpg" \
  --output cleaned.png
```
🔐 Authorization

All requests to `/clean` require a bearer token.

Use this header in requests:

Authorization: Bearer your_secret_token

🧠 Model

The application uses:
- Architecture: Unet++
- Encoder: resnet34
- Implementation: segmentation_models_pytorch

Model weights available:
- watermark_model.pth
- watermark_model_0.1.pth
- watermark_model_0.2.pth
- watermark_model_0.3.pth

By default, `watermark_model.pth` is loaded. Others may be experimental or alternative versions.

📁 Project Structure

. <br>
├── Dockerfile<br>
├── docker-compose.yml<br>
├── main.py              # FastAPI entry point<br>
├── model.py             # Neural network model loader<br>
├── security.py          # Token validation<br>
├── watermark_model*.pth # Model weights<br>
├── requirements-runtime.txt<br>
└── .env

⚙️ Dependencies

All dependencies are listed in `requirements-runtime.txt` and are installed during Docker image build.

📌 TODO

- Document each model version.
- Add a web upload interface.
- Support for larger image formats.

🛡️ License

Specify your license here if applicable.

📬 Feedback

Pull requests and contributions are welcome!
</details>