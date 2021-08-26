import os
import inferencing
import pathlib
import configuration

INPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/textformat-en-modifiziert/'
OUTPUT_TEXTFILE_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated/' + configuration.RUN_NUMBER + "/"
LOG_FOLDER = '/Users/jan/Nextcloud/Art-Pilot/Ausstellungsplanung Übersicht/Texte für ArtPilot/generated-json/' + configuration.RUN_NUMBER + "/"

# create folders if neccessary
pathlib.Path(OUTPUT_TEXTFILE_FOLDER).mkdir(parents=True, exist_ok=True)
pathlib.Path(LOG_FOLDER).mkdir(parents=True, exist_ok=True)

# iterate through all ".txt"-files in input folder
for filename in os.listdir(INPUT_TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        # skip existing output files
        output_filename = OUTPUT_TEXTFILE_FOLDER + filename
        if os.path.isfile(output_filename):
            print(f'error: file {output_filename} already exists')
            continue

        # write inferenced data to new file
        with open(INPUT_TEXTFILE_FOLDER + filename, 'r') as reader:
            text = reader.read()
            generated = inferencing.inference(text)
            with open(output_filename, 'w') as writer:
                writer.write(generated[0])
            with open(LOG_FOLDER + filename, 'w') as writer:
                writer.write(str(generated[1]))