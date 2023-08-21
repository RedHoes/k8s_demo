FROM python:3.9

WORKDIR /myapp

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY slack_bot.py .

CMD ["python3", "slack_bot.py"]