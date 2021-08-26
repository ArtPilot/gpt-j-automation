import os
import inferencing
import pathlib
import argparse

def inferenceFolder(input_folder, output_folder, log_folder, max_tokens, temperature, top_p):
    # create folders if neccessary
    pathlib.Path(output_folder).mkdir(parents=True, exist_ok=True)
    pathlib.Path(log_folder).mkdir(parents=True, exist_ok=True)

    # iterate through all ".txt"-files in input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"): 
            # skip existing output files
            output_filename = os.path.join(output_folder, filename)
            if os.path.isfile(output_filename):
                print(f'error: file {output_filename} already exists')
                continue

            # write inferenced data to new file
            with open(os.path.join(input_folder, filename), 'r') as reader:
                text = reader.read()
                generated = inferencing.inference(text, max_tokens, temperature, top_p)
                with open(output_filename, 'w') as writer:
                    writer.write(generated[0])
                with open(os.path.join(log_folder, filename), 'w') as writer:
                    writer.write(str(generated[1]))
                print(f"inferenced text unsing input from {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Inference text unsing files from an imput folder. write to an output folder. accept additional parameters to overwrite the default values.')
    parser.add_argument('inputfolder_name', help='name of the folder with the input files')
    parser.add_argument('outputfolder_name', help='name of the folder where the output files will be written to')
    parser.add_argument('logfolder_name', help='name of the folder where the log files will be written to')
    parser.add_argument('--max_tokens', type=int, default=200, help='defaults to 200')
    parser.add_argument('--temperature', type=float, default=0.8, help='defaults to 0.8')
    parser.add_argument('--top_p', type=float, default=0.9, help='defaults to 0.9')
    parser.add_argument('subfolder_name', help='name of the output subfolder to create')

    args = parser.parse_args()
    input_folder = args.inputfolder_name
    output_folder = os.path.join(args.outputfolder_name, args.subfolder_name)
    log_folder = os.path.join(args.logfolder_name, args.subfolder_name)
    max_tokens = args.max_tokens
    temperature = args.temperature
    top_p = args.top_p
    inferenceFolder(input_folder, output_folder, log_folder, max_tokens, temperature, top_p)