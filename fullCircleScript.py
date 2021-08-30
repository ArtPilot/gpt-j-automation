import os
import argparse
import inferencing
import translate
import text2speech

ROOT_PATH = "/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/"
SOURCE_FOLDER = os.path.join(ROOT_PATH, "textformat-en-modifiziert")
GENERATED_FOLDER = os.path.join(ROOT_PATH, "generated")
LOG_FOLDER = os.path.join(ROOT_PATH, "generated-json")
GENERATED_TRANSLATED_FOLDER = os.path.join(ROOT_PATH, "generated-translated")
MP3_FOLDER = os.path.join(ROOT_PATH, "gesprochen")

parser = argparse.ArgumentParser(description='Generate a lot of sound files')
parser.add_argument('first_subfolder_number', type=int)
parser.add_argument('last_subfolder_number', type=int)
args = parser.parse_args()

#generate the desired number of text, translations and sound files
for i in range(args.first_subfolder_number, args.last_subfolder_number + 1):
    subfolder_name = f"{i:02d}"
    generated_run = os.path.join(GENERATED_FOLDER, subfolder_name)
    translated_run = os.path.join(GENERATED_TRANSLATED_FOLDER, subfolder_name)
    inferencing.inferenceFolder(SOURCE_FOLDER, generated_run, os.path.join(LOG_FOLDER, subfolder_name), 200, 0.8, 0.9)
    translate.translate_folder(generated_run, translated_run, "de")
    text2speech.speak_folder(translated_run, os.path.join(MP3_FOLDER, subfolder_name))
