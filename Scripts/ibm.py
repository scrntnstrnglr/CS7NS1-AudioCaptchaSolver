# coding=utf-8
import json
from os.path import join, dirname
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('2SSH7ZDGn788ZPiu6IZVkAn8DaTuOEy9zr0och7yYAj3')
service = TextToSpeechV1(authenticator=authenticator)
service.set_service_url('https://gateway-lon.watsonplatform.net/text-to-speech/api')

voices = service.list_voices().get_result()

with open(join(dirname(__file__), 'output.wav'),
          'wb') as audio_file:
    response = service.synthesize(
        'Hello world!', accept='audio/wav',
        voice="en-US_AllisonVoice").get_result()
    audio_file.write(response.content)