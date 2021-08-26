import os
import inferencing
import pathlib
import argparse

parser = argparse.ArgumentParser(description='Inference text unsing files from an imput folder. write to an output folder. accept additional parameters to overwrite the default values.')
parser.add_argument('inputfolder_name', help='name of the folder with the input files')
parser.add_argument('outputfolder_name', help='name of the folder where the output files will be written to')
parser.add_argument('logfolder_name', help='name of the folder where the log files will be written to')
parser.add_argument('--max_tokens', type=int, default=200, help='defaults to 200')
parser.add_argument('--temperature', type=float, default=0.8, help='defaults to 0.8')
parser.add_argument('--max_p', type=float, default=0.9, help='defaults to 0.9')
parser.add_argument('subfolder_name', help='name of the output subfolder to create')

args = parser.parse_args()
INPUT_TEXTFILE_FOLDER = args.inputfolder_name
OUTPUT_TEXTFILE_FOLDER = os.path.join(args.outputfolder_name, args.subfolder_name)
LOG_FOLDER = os.path.join(args.logfolder_name, args.subfolder_name)

# create folders if neccessary
pathlib.Path(OUTPUT_TEXTFILE_FOLDER).mkdir(parents=True, exist_ok=True)
pathlib.Path(LOG_FOLDER).mkdir(parents=True, exist_ok=True)

# iterate through all ".txt"-files in input folder
for filename in os.listdir(INPUT_TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        # skip existing output files
        output_filename = os.path.join(OUTPUT_TEXTFILE_FOLDER, filename)
        if os.path.isfile(output_filename):
            print(f'error: file {output_filename} already exists')
            continue

        # write inferenced data to new file
        with open(os.path.join(INPUT_TEXTFILE_FOLDER, filename), 'r') as reader:
            text = reader.read()
            generated = inferencing.inference(text)
            with open(output_filename, 'w') as writer:
                writer.write(generated[0])
            with open(os.path.join(LOG_FOLDER + filename), 'w') as writer:
                writer.write(str(generated[1]))
            print()