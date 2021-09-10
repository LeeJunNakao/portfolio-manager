FROM python:3.8.3-alpine
WORKDIR /usr/app
ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHON_VERSION=3.8 \
  APP_PATH=/home/app \
  PATH=/home/python/.local/lib/python3.8/site-packages:/usr/local/bin:/home/python:/home/python/app/bin:$PATH:/usr/app:/root/.poetry/bin
RUN pip install -U pip
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add curl
RUN pip install -U pytest
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version 1.1.8
RUN source $HOME/.poetry/env
RUN poetry config virtualenvs.create false
COPY pyproject.toml pyproject.toml
RUN poetry install
EXPOSE 5000
CMD ["ash"]