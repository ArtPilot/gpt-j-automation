# importing the requests library
import requests
import urllib
import json
import os
  
RUN_NUMBER = '01'
INPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/textformat-en/'
OUTPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated/' + RUN_NUMBER + "/"

# defining the api-endpoint
BASE_URL = "http://d5d2-46-114-139-115.ngrok.io/engines/completions"

def drop_incomplete_last_sentences(text):
        sentence_end_sign = ['.', ';', '?', '!', '/n']
        last_sentence_end = max(text.rfind('.'), text.rfind('?'), text.rfind('!'), text.rfind('/n'), text.rfind(';'))
        if last_sentence_end > 0:
                text = text[0:last_sentence_end + 1]
        return text


def inference(input):
        encoded_input = urllib.parse.quote(input, safe='')

        params = "?prompt=" + encoded_input + "&max_tokens=200&temperature=0.8&top_p=0.9&top_k=40&n=1&stream=false&echo=false&presence_penalty=0.0001&repetition_penalty=1&best_of=1&recursive_depth=0&recursive_refresh=0"

        # headers
        headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json'
        }
        
        # sending post request and saving response as response object
        r = requests.post(url = BASE_URL + params, headers=headers)
        
        # extracting response text 
        response = r.json()
        choice = response['choices'][0] # there is only one result
        #print(choice)
        generated_text = choice['text'][len(choice['prompt']):]
        generated_full_sentences = drop_incomplete_last_sentences(generated_text)
        return generated_full_sentences