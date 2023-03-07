import os

import pytest

import whisperx


# @pytest.mark.parametrize('model_name', whisperx.available_models())
def test_transcribe(model_name: str = "tiny.en"):
    model = whisperx.load_model(model_name).cuda()
    audio_path = "tests/test_data/jfk.flac"

    language = "en" if model_name.endswith(".en") else None
    result = model.transcribe(audio_path, language=language, temperature=0.0)
    assert result["language"] == "en"

    transcription = result["text"].lower()
    assert "my fellow americans" in transcription
    assert "your country" in transcription
    assert "do for you" in transcription
