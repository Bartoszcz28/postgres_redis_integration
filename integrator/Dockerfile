FROM python:3.10
# RUN apt-get update && apt-get -y install cron vim
WORKDIR /app
ADD integrator.py .
# COPY crontab /etc/cron.d/crontab
# COPY hello.py /app/hello.py
# RUN chmod 0644 /etc/cron.d/crontab
# RUN /usr/bin/crontab /etc/cron.d/crontab

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# run crond as main process of container
CMD ["python", "./integrator.py"]
