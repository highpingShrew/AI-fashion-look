from datetime import datetime, timezone
from typing import Any, Dict, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from app.domain.fashion_attributes import FashionAttributes


class RecognitionMetadata(BaseModel):
    """
    Техническая информация о результате AI-распознавания.
    """

    model_name: Optional[str] = Field(
        default=None,
        description="Название модели, которая распознавала вещь.",
    )

    prompt_version: Optional[str] = Field(
        default=None,
        description="Версия промпта AI Vision.",
    )

    confidence: Optional[float] = Field(
        default=None,
        ge=0,
        le=1,
        description="Общая уверенность распознавания от 0 до 1.",
    )

    needs_review: bool = Field(
        default=True,
        description="Нужно ли пользователю проверить результат распознавания.",
    )


class WardrobeItem(BaseModel):
    """
    Предмет одежды, сохранённый в цифровом гардеробе.
    """

    item_id: UUID = Field(
        default_factory=uuid4,
        description="Уникальный идентификатор вещи.",
    )

    image_path: str = Field(
        min_length=1,
        description="Путь к сохранённому изображению вещи.",
    )

    fashion_attributes: FashionAttributes = Field(
        description="Структурированные fashion-характеристики вещи.",
    )

    recognition: RecognitionMetadata = Field(
        description="Метаданные AI-распознавания.",
    )

    # Зарезервировано для Post-MVP.
    # В MVP поле не заполняется и не участвует в бизнес-логике.
    commerce: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Будущие commerce-данные. В MVP не используются.",
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Дата и время создания записи.",
    )

    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Дата и время последнего изменения записи.",
    )