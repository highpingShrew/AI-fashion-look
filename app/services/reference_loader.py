import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
REFERENCE_DIR = PROJECT_ROOT / "data" / "reference"


def load_reference(filename: str) -> Any:
    """
    Загружает JSON-справочник из папки data/reference.

    filename передаётся без расширения .json.
    Например: load_reference("categories").
    """

    file_path = REFERENCE_DIR / f"{filename}.json"

    if not file_path.exists():
        raise FileNotFoundError(
            f"Справочник не найден: {file_path}"
        )

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Некорректный JSON в справочнике {file_path}: {error}"
        ) from error