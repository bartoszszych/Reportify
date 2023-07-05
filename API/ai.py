import os
import typing
import openai
import replicate 
from PyQt5.QtCore import QObject, pyqtSignal

class AI(QObject):
    __instance = None
    error_occured = pyqtSignal(str)

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, openai_api_key: str, replicate_api_token: str) -> None:
        super().__init__()

        openai.api_key = openai_api_key
        os.environ["REPLICATE_API_TOKEN"] = replicate_api_token

    def generate_text_from_prompt(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system", "content": prompt},
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            error_message = f"Error: {e}"
            self.error_occured.emit(error_message)

    def transcribe_speech_to_text(self, audio_file_path):
        try:
            audio_file = open(audio_file_path, 'rb')
            transcript = openai.Audio.transcribe('whisper-1', audio_file)
            return transcript.text
        except Exception as e:
            error_message = f"Error: {e}"
            self.error_occured.emit(error_message)

    def image_to_text(self, img_file_path):
        try:
            text = replicate.run(
                "pharmapsychotic/clip-interrogator:a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90",
                input={'image': open(img_file_path, 'rb')}
            )
            return text
        except Exception as e:
            error_message = f"Error: {e}"
            self.error_occured.emit(error_message)