# This file contains Singleton AI class which implements OpenAI and Replicate API methods
import os
import openai
import replicate 

class AI:
    __instance = None

    def __new__(cls, openai_api_key: str, replicate_api_token: str) -> None:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            openai.api_key = openai_api_key
            os.environ["REPLICATE_API_TOKEN"] = replicate_api_token
            return cls.__instance
        
        else:
            raise Exception("This class is a Singleton")

    @classmethod
    def generate_text_from_prompt(cls, prompt):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": prompt},
            ]
        )
        return response.choices[0].message.content
    
    @classmethod
    def transcribe_speech_to_text(cls, audio_file_path):
        audio_file = open(audio_file_path, 'rb')
        transcript = openai.Audio.transcribe('whisper-1', audio_file)
        return transcript.text
    
    @classmethod
    def image_to_text(cls, img_file_path):
        text = replicate.run(
            "pharmapsychotic/clip-interrogator:a4a8bafd6089e1716b06057c42b19378250d008b80fe87caa5cd36d40c1eda90",
            input={'image': open(img_file_path, 'rb')}
        )
        return text