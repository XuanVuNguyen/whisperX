import numpy as np
from aligner import AlignResult, Aligner
from transcriber import TranscribeResult


def test_aligner():
    LANGUAGE = "en"
    AUDIO_FILE = "tests/test_data/jfk.flac"
    TRUE_TRANSCRIBE_PATH = "tests/test_data/jfk_transcribe_result.json"
    TRUE_ALIGN_PATH = "tests/test_data/jfk_align_result.json"

    aligner = Aligner(language=LANGUAGE)

    transcribe_result = TranscribeResult.from_json(TRUE_TRANSCRIBE_PATH)

    result = aligner.run(audio_file=AUDIO_FILE, transcribe_result=transcribe_result)
    expected_result = AlignResult.from_json(TRUE_ALIGN_PATH)

    for segment, expected_segment in zip(result.word_segments, expected_result.word_segments):
        start = segment.start
        expected_start = expected_segment.start

        assert np.isclose(start, expected_start)

    assert True
