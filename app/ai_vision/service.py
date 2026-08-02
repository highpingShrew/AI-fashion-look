from pathlib import Path

from app.ai_vision.client import send_image_to_vision
from app.ai_vision.schemas import AIRecognitionResult


def recognize_image(
    image_path: str | Path,
) -> AIRecognitionResult:
    """
    Распознаёт предмет одежды на изображении
    и возвращает валидированный AIRecognitionResult.
    """
    return send_image_to_vision(image_path)