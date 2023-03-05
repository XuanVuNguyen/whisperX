import whisperx

from whisperx_main import TranscribeAligner
import whisperx_dataclasses as resp

# def test_dummy():
    

#     device = "cuda" 
#     audio_file = "tests/jfk.flac"

#     # transcribe with original whisper
#     model = whisperx.load_model("tiny.en", device)
#     result = model.transcribe(audio_file)

#     print(result["segments"]) # before alignment

#     # load alignment model and metadata
#     model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)

#     # align whisper output
#     result_aligned = whisperx.align(result["segments"], model_a, metadata, audio_file, device)

    # print(result_aligned["segments"]) # after alignment
    # print(result_aligned["word_segments"]) # after alignment
def test_main():
    MODEL_NAME = "tiny.en"
    LANGUAGE = "en"
    DEVICE = "cuda"
    AUDIO_FILE = "my_tests/jfk.flac"

    TRUE_TRANSCRIBE_PATH = "my_tests/true_transcribe.json"

    model = TranscribeAligner(MODEL_NAME, LANGUAGE, DEVICE)


    transcribe: resp.TranscribeResult = model.transcribe(AUDIO_FILE)
    true_transcribe = resp.TranscribeResult.from_json(TRUE_TRANSCRIBE_PATH)
    assert transcribe.__dict__ == true_transcribe.__dict__

    # align_w_trans: resp.WordSegmentList= model.align(AUDIO_FILE, transcribe)
    # align_wo_trans: resp.WordSegmentList = model.align(AUDIO_FILE)
