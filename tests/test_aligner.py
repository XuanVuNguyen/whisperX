from aligner import Aligner
from transcriber import TranscribeResult


def test_aligner():
    LANGUAGE = "en"
    AUDIO_FILE = "tests/test_data/jfk.flac"
    TRUE_TRANSCRIBE_PATH = "tests/test_data/jfk_transcribe_result.json"

    aligner = Aligner(language=LANGUAGE)

    transcribe_result = TranscribeResult.from_json(TRUE_TRANSCRIBE_PATH)

    result = aligner.run(audio_file=AUDIO_FILE, transcribe_result=transcribe_result)

    assert True
