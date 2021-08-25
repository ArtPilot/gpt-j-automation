import os
import inferencing
import pathlib
import configuration

INPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/textformat-en-modifiziert/'
OUTPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated/' + configuration.RUN_NUMBER + "/"
LOG_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated-json/' + configuration.RUN_NUMBER + "/"

pathlib.Path(OUTPUT_TEXTFILE_FOLDER).mkdir(parents=True, exist_ok=True)
pathlib.Path(LOG_FOLDER).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(INPUT_TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        with open(INPUT_TEXTFILE_FOLDER + filename, 'r') as reader:
            text = reader.read()
            generated = inferencing.inference(text)
            with open(OUTPUT_TEXTFILE_FOLDER + filename, 'w') as writer:
                writer.write(generated[0])
            with open(LOG_FOLDER + filename, 'w') as writer:
                writer.write(str(generated[1]))
        continue
    else:
        continue