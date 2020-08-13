FROM python:3.8.5-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./source/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY source/newsfeedproject .

# copy entrypoint.sh
COPY ./docker/entrypoint.sh .
# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
