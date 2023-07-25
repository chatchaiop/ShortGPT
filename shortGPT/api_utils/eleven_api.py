import requests
import json
import random

def getVoices(api_key=""):
    url = 'https://api.elevenlabs.io/v1/voices'
    headers = {'accept': 'application/json'}
    if api_key:
        headers['xi-api-key'] = api_key
    response = requests.get(url, headers=headers)
    voices = {}
    for a in response.json()['voices']:
        voices[a['name']] = a['voice_id']
    return voices

def getCharactersFromKey(key):
    return 10000



def generateVoice(text, character, fileName, api_key=""):

    url = "https://api-voice.botnoi.ai/api/service/generate_audio"

    headers = {
        "Content-Type": "application/json",
        "Botnoi-Token": "716c092a6f863141eb0a8b7917cfac356f0200076c1429818c113d105c21694c",
    }

    data = {
        "text": text,
        "speaker": "6",
        "volume": 1,
        "speed": 1,
        "type_media": "mp3",
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        audio_url = response.json().get('audio_url')
        if audio_url:
            audio_response = requests.get(audio_url)
            if audio_response.status_code == 200:
                with open(fileName, "wb") as f:
                    f.write(audio_response.content)
                    return fileName
            else:
                raise Exception(f"Error downloading audio, {audio_response.status_code}")
        else:
            raise Exception("No audio_url in response")
    else:
        message = response.text
        raise Exception(f"Error in response, {response.status_code}, message: {message}")

    return ""

# print(getCharactersFromKey(''))
