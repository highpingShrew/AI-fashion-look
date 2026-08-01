from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from app.domain.fashion_attributes import FashionAttributes

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_validator

class RecognitionStatus(str, Enum):
    SUCCESS = "success"
    PARTIAL = "partial"
    REJECTED = "rejected"

class AIRecognitionResult(BaseModel):
    """
    Результат распознавания одной вещи модулем AI Vision.
    """

    model_config = ConfigDict(extra="forbid")

    schema_version: str = Field(
        default="1.0",
        description="Версия схемы результата AI Vision.",
    )

    
    status: RecognitionStatus = Field(
    description="Статус распознавания.",
)

    fashion_attributes: Optional[FashionAttributes] = Field(
        default=None,
        description="Распознанные характеристики вещи.",
    )

    uncertain_fields: List[str] = Field(
        default_factory=list,
        description="Поля, которые модели не удалось определить уверенно.",
    )

    image_quality_issues: List[str] = Field(
        default_factory=list,
        description="Проблемы качества исходного изображения.",
    )
    
    @model_validator(mode="after")
    def validate_attributes_for_status(self):
        if (
            self.status in {
                RecognitionStatus.SUCCESS,
                RecognitionStatus.PARTIAL,
            }
            and self.fashion_attributes is None
        ):
            raise ValueError(
                "fashion_attributes is required for success or partial status"
            )

        return self    