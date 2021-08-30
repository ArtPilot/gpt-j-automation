import os
import six
from google.cloud import translate_v2 as translate
from html import unescape
import argparse
import pathlib

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'../aqueous-timer-323814-bc940f9d191f.json'

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
    result = translate_client.translate(text, target_language=target_language, format_="text")

    return result["translatedText"]

def translate_folder(input_folder, output_folder, language):
    pathlib.Path(output_folder).mkdir(parents=True, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"): 
            # skip existing output files
            output_filename = os.path.join(output_folder, filename)
            if os.path.isfile(output_filename):
                print(f'error: file {output_filename} already exists')
                continue

            # read and translate input file and write output file
            with open(os.path.join(input_folder, filename), 'r') as reader:
                text = reader.read()
                translation = translate_text(text, language)
                translation_fixed = unescape(translation)
                with open(output_filename, 'w') as writer:
                    writer.write(translation_fixed)
                    print(f"translated {filename} to {language}")
            continue
        else:
            continue

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate a file and write the translation into another file')
    parser.add_argument('inputfolder_name', help='name of the folder with the input files')
    parser.add_argument('outputfolder_name', help='name of the folder where the output files will be written to')
    parser.add_argument('language', help='the output language in ISO format')
    parser.add_argument('subfolder_name', help='name of the output subfolder to create')

    args = parser.parse_args()

    input_folder = os.path.join(args.inputfolder_name, args.subfolder_name)
    output_folder = os.path.join(args.outputfolder_name, args.subfolder_name)
    language = args.language
    translate_folder(input_folder, output_folder, language)
