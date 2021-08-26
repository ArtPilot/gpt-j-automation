import os
import translate
import text2speech
import configuration
import argparse


def speak_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"): 
            with open(os.path.join(input_folder, filename), 'r') as reader:
                text = reader.read()
                new_filename = filename[:-4] + ".mp3"
                text2speech.text_to_mp3(text, os.path.join(output_folder, new_filename))
            continue
        else:
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate a file and write the translation into another file')
    parser.add_argument('inputfolder_name', help='name of the folder with the input files')
    parser.add_argument('outputfolder_name', help='name of the folder where the output files will be written to')
    parser.add_argument('subfolder_name', help='name of the output subfolder to create')

    args = parser.parse_args()

    subfolder_name = args.subfolder_name
    input_folder = os.path.join(args.inputfolder_name, args.subfolder_name)
    output_folder = os.path.join(args.outputfolder_name, args.subfolder_name)
    speak_folder(input_folder, output_folder)