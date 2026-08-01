import base64
from pathlib import Path

from openai import OpenAI


client = OpenAI()


def encode_image(image_path: str | Path) -> str:
    """
    Читает локальное изображение и возвращает его в формате Base64.
    """
    path = Path(image_path)

    with path.open("rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")