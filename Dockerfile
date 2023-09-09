FROM python:3.10

WORKDIR /pingco

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apt-get update && apt apt-get install netcat -y
#RUN apt-get upgrade -y && apt-get install postgresql-dev gcc python3-dev musl-dev -y


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /pingco/entrypoint.sh
ENTRYPOINT ["/pingco/entrypoint.sh"]
