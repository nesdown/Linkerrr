#!/usr/bin/env python3

from pprint import pprint

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

def cloud_recognition(audio_name):
    result = {
        'accuracy': 0.0,
        'sphinx': "",
        'google_speech': "",
        'google_cloud': "",
        "witai": "",
        "houndify": ""
    }

    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audio_name)
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
    # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        data = r.recognize_sphinx(audio)
        print("Sphinx thinks you said " + data)
        result['sphinx'] = data

    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
        print("Google Speech Recognition results:")
        data = r.recognize_google(audio, show_all=True)

        result['accuracy'] = ("{0:.2f}".format(data['alternative'][0]['confidence']))
        result['google_speech'] = data['alternative'][0]['transcript']
        pprint(data)  # pretty-print the recognition result
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""
    {
      "type": "service_account",
      "project_id": "edrive-1572363261363",
      "private_key_id": "f0aa6aee262f0b67070cf44c8aa62d6b8491eb27",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDKP7QxYQu0mEyj\nkcXqi2Qw7HT9ALXHxonxL3YSSD84ur2zzNDFpE2VCEe5DIkliO1iOCW3SG3hXqZj\ngpVpizXI/KCBycwqhd416a/GmoL9dnTMss57wgirozde9QC2HDBNa8brRNOI+vSu\nmkRieG2a8jc9rWWtgAf/+aUhnCPz7uFhZatLlxiqw1MwB8aGkTXR8XguPg5wKMg9\nvumzqxs3oyoEcMxYutSH6Qd0s7gKhGTP6/UT8kz89S9Ms3MI/F2AdTR91YzQ9/0Q\nQPd4V2JZYSAUggvbp0u56ENk+Nl5MBVC8FUo5P58Suq/GQejFbhTLS35CNYsqM/f\nzrVpQajtAgMBAAECggEAD1NAbjVyU57uv74+BwXE88gXHUy+eYLb1QDJq5z53WyZ\nD1THxRIsJszX0nfWtJdplXW3temxGdC4PvYYKEU6MB6kcvE9nUNDkUZB4YS3xEkD\nlLc/2jTbv1XAzls2UJZWOqeeDRnMBacuf0SFRgjmFUWhVfUbrUf0Uzsxfhh8yPEA\ndfABuz3MAZ5EOsauemGxr2JkeMsH7bwJLCFqVLhQ/Zp00ZC9QLj/IsXuDGP4IRQQ\nNwQALcQQfI6zwqjYDYliqIOUgbBO3yx1e2ZPX4/ATZt75/WgOZED/eTHl/f2jQO0\nOElVgv+FeMt25tj10+UroyRSj9bcX0OGZ08P68CyqQKBgQDrcUaItXzvdr24pg8N\n+1NP2aV23ZEQuFqh4gtTb/6ODCHKVMg9HdahJ/vDcbSvZQrzP40eknysoOtMFFrC\n3abXuF1u3EsF05w5HwNLKudAIEiXGoIkzlvDoeNgVRoEyf2pnYlQsPVnNBJWga14\nkU3cVjzNnacjrjnZ27XCMDFQcwKBgQDb6HfRsNRmebRDxvXfW7QMeWAeBOwNPy3H\n6Lan/aKQyFnC3khtVmgTA0l/sNLhNS/4DiSGM7Vu1sVPGMQvlSUOFiDK0uJxkkVb\n0UpQjJS91exu0Ux/RVFuX/GiLD7/UVyg2MUOWV1ej2pkfPACStjlJd9G4fVTvNCd\naMBtC9+pHwKBgQDXhaHjkv8C1ddmJ9ywF9hzx/BHlxssCxYsChgEEQkcTs6/wExs\nZdwLOealSnjz9bLIaOxth/rIq6W4xwkuSGhqIEKnMNEcTFE9mL4TGPsHIIZSi9mG\nh8BInPDfRgfDSoQBuEvyqYp7JpeCyMJbE+gKQob2UdKmPt6GJzGCyUrbMQKBgQCD\nv+MJXkfinUfC05C7INXeI1nSomBKD2/+NQ4511tuIpqkhUgfOYVg3rdKKUYuZw82\nLkLzpEcvAL11hgEEAPcSWW+MFIxWPqwPNnSvjYoPsfrU6dBK79y5pAHAh4G2tagp\nNbXZwvCNlp7HVZL1zKHlp6r9bKLuaFET/Y5LxrFZQQKBgQDrJ8uS1/+1VE/nan62\n6n1y6eiTs3OCKTevOvKNtm0hoKp0F8wtHp2MuG4SQ5YeCKD2oBKreKe53a/1IkNM\nIZbjhRsskYlR8NXG817sjNXrl8snquxz9GQfE9dbs6UtzRSVrw4LYurL0pR1m89T\nupTDVZDY7O7qvmI37tvHGj+4eg==\n-----END PRIVATE KEY-----\n",
      "client_email": "starting-account-taowflzcsd3m@edrive-1572363261363.iam.gserviceaccount.com",
      "client_id": "116889265760389828557",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/starting-account-taowflzcsd3m%40edrive-1572363261363.iam.gserviceaccount.com"
    }
    """
    try:
        print("Google Cloud Speech recognition results:")
        data = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, show_all=True)
        pprint(data)  # pretty-print the recognition result

        result['google_cloud'] = data['results'][0]['alternatives'][0]['words'][0]['word']

        # print(data['results'][0]['alternatives'][0]['words'][0]['word'])
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))

    # recognize speech using Wit.ai
    WIT_AI_KEY = "K6Z4HOUNB72P4RAL5CYOAMB23DOMYI2C"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        print("Wit.ai recognition results:")
        data = r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True)
        pprint(data)  # pretty-print the recognition result
        result['witai'] = data['_text']

    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))

    HOUNDIFY_CLIENT_ID = "lrM1LLtKb529KMpqJ9lJOA=="  # Houndify client IDs are Base64-encoded strings
    HOUNDIFY_CLIENT_KEY = "7lqP0oPQKnTHUkCBBPWV4pc7Qv5PMv_WDmPc0q5vlKOc2oVSot1WjRh0kDb1Faq1gYRrwi2ABvKrgI34WA0pDA=="  # Houndify client keys are Base64-encoded strings
    try:
        data = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
        print("Houndify thinks you said " + data)
        result['houndify'] = data

    except sr.UnknownValueError:
        print("Houndify could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Houndify service; {0}".format(e))

    return result

    # # recognize speech using IBM Speech to Text
    # IBM_USERNAME = "apikey"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    # IBM_PASSWORD = "in2Ej3cm1ZG0WoqGJQ4ByMFS_s1Sz_AYPfw9BcqKrsNH"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    # try:
    #     print("IBM Speech to Text results:")
    #     pprint(r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, show_all=True))  # pretty-print the recognition result
    # except sr.UnknownValueError:
    #     print("IBM Speech to Text could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results from IBM Speech to Text service; {0}".format(e))
