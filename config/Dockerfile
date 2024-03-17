FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /corp_django
WORKDIR /corp_django
COPY requirements.txt /corp_django/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /corp_django/