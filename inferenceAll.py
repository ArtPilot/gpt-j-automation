import os
import inferencing
import pathlib

RUN_NUMBER = '01'
INPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/textformat-en/'
OUTPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated/' + RUN_NUMBER + "/"

for filename in os.listdir(INPUT_TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        with open(INPUT_TEXTFILE_FOLDER + filename, 'r') as reader:
            text = reader.read()
            generated_text = inferencing.inference(text)
            pathlib.Path(OUTPUT_TEXTFILE_FOLDER).mkdir(parents=True, exist_ok=True)
            with open(OUTPUT_TEXTFILE_FOLDER + filename, 'w') as writer:
                writer.write(generated_text)
        continue
    else:
        continue