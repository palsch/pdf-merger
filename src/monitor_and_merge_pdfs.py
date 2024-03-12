import os
import time
import argparse
import configparser
from datetime import datetime

from pdf_merge import merge_pdfs

def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def process_files(file1, file2, output_folder):
    print("Processing files:", file1, file2)
    # Generate timestamp for output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{timestamp}_scanned_merged.pdf"

    # Add your processing logic here
    merge_pdfs(file1, file2, f"{output_folder}/{output_filename}")

    # Delete the processed files
    os.remove(file1)
    os.remove(file2)

def monitor_folder(folder, output_folder):
    front_file = None
    back_file = None
    while True:
        files = os.listdir(folder)
        # print("Files in folder:", files)
        # print("Processed front:", front_file)
        # print("Processed back:", back_file)
        time.sleep(10)  # Adjust this delay as needed

        for file in files:
            if "front" in file and front_file is None:
                front_file = file
                
            if "back" in file and back_file is None:
                back_file = file

        if front_file is not None and back_file is not None:
            time.sleep(5)  # Adjust this delay as needed
            process_files(os.path.join(folder, front_file), os.path.join(folder, back_file), output_folder)

            front_file = None
            back_file = None


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="PDF Merger Script")
    parser.add_argument("--config", "-c", default="config.ini", help="Path to config file")
    args = parser.parse_args()

    # Read config file
    config_file = args.config
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file '{config_file}' not found.")

    config = read_config(config_file)

    # Get settings from config
    input_folder = config.get("Settings", "input_folder")
    output_folder = config.get("Settings", "output_folder")

    monitor_folder(input_folder, output_folder)
