FROM python:3

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main.py"]
