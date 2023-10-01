FROM python:3.10

WORKDIR /app
ADD data_generator.py .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "./data_generator.py"]