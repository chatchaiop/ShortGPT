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
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ5dVpxQlZadWxhTTVXbUlGRTlhbHNTODljMUozIiwiaWF0IjoxNjkwMjUxOTA5LCJuYmYiOjE2OTAyNTE5MDksImp0aSI6ImRmYmI4ODM2LWE1MDgtNDhhMS04ZDE3LWMyOGRmOTVjZjEyYiIsImV4cCI6MTY5MDI3MzUwOSwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjpmYWxzZSwidWlkIjoiNzVjMzg3YzAtNTI1OC01ZDRmLTk2MjAtMTI2MGUzYThhNmQzIn0.--3IKMq-F8NQ9XKBbAQm37KZ9Md4P_0GBpRvqdlnSeU"  # ใส่ API Key ของคุณที่นี่
    url = "https://api-genvoice.botnoi.ai/voice/v1/generate_voice"

    data = {
        "audio_id": "TLBIY",
        "text": text,
        "text_delay": text,
        "speaker": "6",
        "volume": "100",
        "speed": "1",
        "type_voice": "wav",
    }

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Referer": "https://voice.botnoi.ai/",
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        audio_data = response.content

        with open(fileName, "wb") as f:
            f.write(audio_data)

        return fileName
    else:
        message = response.text
        raise Exception(f"Error in response, {response.status_code}, message: {message}")

    return ""

# print(getCharactersFromKey(''))
