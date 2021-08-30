import boto3
import pathlib
import os
import pathlib

polly_client = boto3.Session().client('polly')

def text_to_mp3(text, output_file_name, voice='Vicki'):
    # get audio file from amazon
    response = polly_client.synthesize_speech(VoiceId='Vicki',
                    OutputFormat='mp3', 
                    Text = text,
                    Engine = 'neural')
    file_dir = os.path.dirname(output_file_name)

    #create folder if needed
    pathlib.Path(file_dir).mkdir(parents=True, exist_ok=True)

    # do not overwrite files
    if os.path.isfile(output_file_name):
        print(f'error: file {output_file_name} already exists')
        return -1
    
    # create and write file
    file = open(output_file_name, 'wb')
    file.write(response['AudioStream'].read())
    written_bites = file.tell()
    file.close()
    return written_bites # return file size in bytes

def speak_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"): 
            with open(os.path.join(input_folder, filename), 'r') as reader:
                text = reader.read()
                new_filename = filename[:-4] + ".mp3"
                text_to_mp3(text, os.path.join(output_folder, new_filename))
            print(f"created file {new_filename}")
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