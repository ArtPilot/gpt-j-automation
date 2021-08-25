import os
import translate
import pathlib
import configuration
from html import unescape


ORIGINAL_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated/' + configuration.RUN_NUMBER + "/"
ENGLISH_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated-translated/' + configuration.RUN_NUMBER + "/"
pathlib.Path(ENGLISH_TEXTFILE_FOLDER).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(ORIGINAL_TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        with open(ORIGINAL_TEXTFILE_FOLDER + filename, 'r') as reader:
            text = reader.read()
            translation = translate.translate_text(text, "de")
            translation_fixed = unescape(translation)

            with open(ENGLISH_TEXTFILE_FOLDER + filename, 'w') as writer:
                writer.write(translation_fixed)
        continue
    else:
        continue

