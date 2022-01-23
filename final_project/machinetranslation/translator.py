"""This module incorporates two functions which use ibm_watson to translate from
 english to french, and french to english"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
LT = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
LT.set_service_url(URL)

def english_to_french(english_text):
    """ A function written using ibm api to translate from english to french"""
    translation = LT.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ A function written using ibm api to translate from french to english"""
    translation = LT.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
