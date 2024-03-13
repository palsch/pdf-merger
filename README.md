# PDF Merger Script

This script monitors a folder for two PDF files with "front" and "back" in their filenames. It then merges these PDFs into one by alternating pages from both PDFs, with the pages from the second PDF added in reverse order.

I use this script when scanning documents with an automatic feeder. The process involves scanning the front pages first and then the back pages separately. This results in two PDF files that need to be merged.

## Usage with Docker

You can use docker to run the script. Here you have to only specify the `input` and `output` folder.

```bash
docker run -d --name pdf-merger --restart unless-stopped -v /local/input:/data/input -v /local/output:/data/output docker.io/palsch/pdf-merger:latest
```

Docker Hub: https://hub.docker.com/r/palsch/pdf-merger 

### Build

```bash
docker build -t pdf-merger . 

# build multi platform and push to dockerhub
docker buildx build -t palsch/pdf-merger:latest --platform linux/amd64,linux/arm64 --push .
```

### Systemd service

Register docker container as systemd service and enable it by using Podman

```bash
podman generate systemd --new --files --name pdf-merger --restart-policy always
cp container-pdf-merger.service /etc/systemd/system/systemctl 
enable container-pdf-merger.service
```

## Requirements
- Python 3.x
- PyPDF2 library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/palsch/pdf-merger.git
   cd pdf-merger
   ```

1. Install the required dependencies:
   ```bash
   pip install PyPDF2
   pip install configparser
   ```

1. Create a config.ini file in the root of the project with the following content:

   ```ini
   [Settings]
   input_folder = /path/to/input/folder
   output_folder = /path/to/output/folder
   ```

## Usage
1. Place your PDF files in the `input_folder` folder.
1. Run the script `monitor_and_merge_pdfs.py` with the `--config` argument to specify the path to the config file:

   ```bash
   python monitor_and_merge_pdfs.py --config /path/to/config.ini
   ```
   
   If the --config argument is not provided, the script will use config.ini in the root directory by default.

   The script will continuously monitor the `input_folder` folder for two PDF files with "front" and "back" in their filenames.

1. When both "front" and "back" PDFs are detected, the script will merge them into one PDF file by alternating pages from both PDFs, with the pages from the "back" PDF added in reverse order.

1. The merged PDF file will be saved in the output folder with a timestamp in its filename, e.g., `20220307_154321_scanned_merged.pdf`.

## File Structure
* `input_folder/`: Place your "front" and "back" PDF files here.
* `output_folder/`: Merged PDF files will be saved here.
* `config.ini`: Configuration file for input and output folder paths.

## Notes
* Make sure the PDF files have the word "front" and "back" in their filenames, e.g., `document_front.pdf` and `document_back.pdf`.
* The script uses the PyPDF2 library to manipulate PDF files.

## Author
palsch
