import os
import translate
import text2speech
import configuration


TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated-translated/' + configuration.RUN_NUMBER + "/"
OUTPUT_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/gesprochen/' + configuration.RUN_NUMBER + "/"

for filename in os.listdir(TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        with open(TEXTFILE_FOLDER + filename, 'r') as reader:
            text = reader.read()
            text2speech.text_to_mp3(text, OUTPUT_FOLDER + filename[:-4] + ".mp3")
        continue
    else:
        continue

