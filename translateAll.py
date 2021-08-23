import os
import translate
from html import unescape

ORIGINAL_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/textformat/'
ENGLISH_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/textformat-en/'

for filename in os.listdir(ORIGINAL_TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        with open(ORIGINAL_TEXTFILE_FOLDER + filename, 'r') as reader:
            text = reader.read()
            translation = translate.translate_text(text, "en")
            translation_fixed = unescape(translation)
            with open(ENGLISH_TEXTFILE_FOLDER + filename, 'w') as writer:
                writer.write(translation_fixed)
        continue
    else:
        continue

