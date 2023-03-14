from transcriber import TranscribeResult, Transcriber


def test_main():
    MODEL_NAME = "tiny.en"
    AUDIO_FILE = "tests/test_data/jfk.flac"

    TRUE_TRANSCRIBE_PATH = "tests/test_data/jfk_transcribe_result.json"

    transcriber = Transcriber(model_name = MODEL_NAME)

    transcribe: TranscribeResult = transcriber.run(AUDIO_FILE)
    true_transcribe = TranscribeResult.from_json(TRUE_TRANSCRIBE_PATH)
    assert transcribe.text == true_transcribe.text
