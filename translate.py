import os
import six
from google.cloud import translate_v2 as translate
from html import unescape

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'aqueous-timer-323814-bc940f9d191f.json'

def translate_text(text, target_language):
    """Translates text into the target language.

    target_language must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)

    return result["translatedText"]