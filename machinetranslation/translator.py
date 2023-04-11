"""
Translator functions
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Translate English to French."""
    #write the code here
    response = language_translator.translate(
        englishText,
        model_id='en-fr').get_result()
    frenchText = response['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """Translate French to English."""
    #write the code here
    response = language_translator.translate(
        frenchText,
        model_id='fr-en').get_result()
    englishText = response['translations'][0]['translation']
    return englishText

#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

#print(englishToFrench('This is a test.'))
#print(frenchToEnglish("C'est un test."))
