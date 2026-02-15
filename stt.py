import whisper

model = whisper.load_model('base')

def speech_to_text(audio_path: str) -> str:
    'converts audio to english text'

    result = model.transcribe(audio_path, task="translate")

    return result['text']