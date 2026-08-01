from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Outfit(BaseModel):
    """
    Образ, сформированный только из существующих вещей гардероба.
    """

    outfit_id: UUID = Field(
        default_factory=uuid4,
        description="Уникальный идентификатор образа.",
    )

    item_ids: List[UUID] = Field(
        min_length=2,
        description="Идентификаторы вещей, входящих в образ.",
    )

    explanation: str = Field(
        min_length=1,
        description="Объяснение, почему вещи сочетаются между собой.",
    )

    score: Optional[float] = Field(
        default=None,
        ge=0,
        le=1,
        description="Итоговая оценка комбинации от Fashion Engine.",
    )