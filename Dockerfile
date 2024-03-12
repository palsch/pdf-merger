FROM python:3

WORKDIR /usr/src/app

RUN mkdir /data /data/input /data/output

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD [ "python", "./monitor_and_merge_pdfs.py"]