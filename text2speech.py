import boto3
import pathlib
import os

polly_client = boto3.Session().client('polly')

def text_to_mp3(text, output_file_name, voice='Vicki'):
    response = polly_client.synthesize_speech(VoiceId='Vicki',
                    OutputFormat='mp3', 
                    Text = text,
                    Engine = 'neural')
    file_dir = os.path.dirname(output_file_name)
    pathlib.Path(file_dir).mkdir(parents=True, exist_ok=True)
    file = open(output_file_name, 'wb')
    file.write(response['AudioStream'].read())
    file.close()