from app.ai_vision.schemas import AIRecognitionResult


def test_valid_success_recognition_result():
    result = AIRecognitionResult(
        status="success",
        fashion_attributes={
            "category": "top",
            "type": "shirt",
            "primary_color": "white",
            "secondary_colors": [],
            "pattern": "solid",
        },
    )

    assert result.status == "success"
    assert result.fashion_attributes is not None
    assert result.fashion_attributes.category == "top"

import pytest
from pydantic import ValidationError

def test_extra_field_is_forbidden():
 with pytest.raises(ValidationError):
        AIRecognitionResult(
            status="success",
            unknown_field="test",
        )