import base64
import mimetypes
from pathlib import Path

from openai import OpenAI

from app.ai_vision.prompts import (
    VISION_SYSTEM_PROMPT,
    VISION_USER_PROMPT,
)


def get_client() -> OpenAI:
    return OpenAI()


def encode_image(image_path: str | Path) -> str:
    path = Path(image_path)

    with path.open("rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def send_image_to_vision(image_path: str | Path) -> str:
    path = Path(image_path)

    mime_type, _ = mimetypes.guess_type(path.name)
    mime_type = mime_type or "image/jpeg"

    image_data = encode_image(path)
    client = get_client()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": VISION_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": VISION_USER_PROMPT,
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:{mime_type};base64,{image_data}",
                    },
                ],
            },
        ],
    )

    return response.output_text