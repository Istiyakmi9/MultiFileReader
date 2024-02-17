FROM python:3.10-slim

WORKDIR /app

COPY . .

# RUN python3 -m venv /opt/venv

# COPY ./requirements.txt /app/requirements.txt
# RUN . /opt/venv/bin/activate && pip install -r requirements.txt

RUN apt-get update
# RUN apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
RUN apt-get install tesseract-ocr
RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]