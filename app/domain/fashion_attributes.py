from typing import List, Optional

from pydantic import BaseModel, Field


class FashionAttributes(BaseModel):
    """
    Структурированные fashion-характеристики предмета одежды.

    Значение None означает, что характеристику невозможно определить
    по фотографии или пользователь ещё её не указал.
    """

    category: Optional[str] = Field(
        default=None,
        description=(
            "Верхнеуровневая категория вещи: "
            "top, bottom, dress, outerwear или shoes."
        ),
    )

    type: Optional[str] = Field(
        default=None,
        description="Основной тип вещи, например shirt, trousers или sneakers.",
    )

    subtype: Optional[str] = Field(
        default=None,
        description=(
            "Уточняющий подтип вещи, например "
            "oxford_shirt или wide_leg_trousers."
        ),
    )

    primary_color: Optional[str] = Field(
        default=None,
        description="Основной цвет вещи.",
    )

    secondary_colors: List[str] = Field(
        default_factory=list,
        description="Дополнительные заметные цвета вещи.",
    )

    pattern: Optional[str] = Field(
        default=None,
        description="Тип принта или отсутствие принта.",
    )

    fit: Optional[str] = Field(
        default=None,
        description=(
            "Характер посадки вещи: "
            "slim, regular, relaxed или oversized."
        ),
    )

    silhouette: Optional[str] = Field(
        default=None,
        description="Визуальный силуэт вещи.",
    )

    style_tags: List[str] = Field(
        default_factory=list,
        description="Стилевые характеристики вещи.",
    )

    season: List[str] = Field(
        default_factory=list,
        description="Подходящие сезоны использования вещи.",
    )

    formality: Optional[str] = Field(
        default=None,
        description="Уровень формальности вещи.",
    )

    warmth_level: Optional[int] = Field(
        default=None,
        ge=1,
        le=5,
        description="Уровень тепла от 1 до 5.",
    )

    statement_level: Optional[int] = Field(
        default=None,
        ge=1,
        le=5,
        description="Визуальная акцентность вещи от 1 до 5.",
    )

    description: Optional[str] = Field(
        default=None,
        description="Краткое нейтральное описание вещи.",
    )