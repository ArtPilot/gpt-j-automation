import boto3
import pathlib
import os

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