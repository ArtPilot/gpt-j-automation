import os
import translate
import pathlib
import configuration
from html import unescape
import argparse

parser = argparse.ArgumentParser(description='Translite a file and write the translation into another file')
parser.add_argument('inputfolder_name', help='name of the folder with the input files')
parser.add_argument('outputfolder_name', help='name of the folder where the output files will be written to')
parser.add_argument('language', help='the output language in ISO format')
parser.add_argument('subfolder_name', help='name of the output subfolder to create')

args = parser.parse_args()

ORIGINAL_TEXTFILE_FOLDER = os.path.join(args.inputfolder_name,args.subfolder_name)
OUTPUT_TEXTFILE_FOLDER = os.path.join(args.outputfolder_name,args.subfolder_name)
pathlib.Path(OUTPUT_TEXTFILE_FOLDER).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(ORIGINAL_TEXTFILE_FOLDER):
    if filename.endswith(".txt"): 
        # skip existing output files
        output_filename = os.path.join(OUTPUT_TEXTFILE_FOLDER, filename)
        if os.path.isfile(output_filename):
            print(f'error: file {output_filename} already exists')
            continue

        # read and translate input file and write output file
        with open(os.path.join(ORIGINAL_TEXTFILE_FOLDER, filename), 'r') as reader:
            text = reader.read()
            translation = translate.translate_text(text, args.language)
            translation_fixed = unescape(translation)
            with open(output_filename, 'w') as writer:
                writer.write(translation_fixed)
                print("translated {filename} to {args.language}")
        continue
    else:
        continue

