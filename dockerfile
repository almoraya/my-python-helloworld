FROM        python:3.9

LABEL       maintain="Alexander M A"

COPY        . /app

WORKDIR     /app

RUN         python3 -m venv /opt/venv
RUN         . /opt/venv/bin/activate
RUN         python3 -m pip install --upgrade pip && pip install -r requirements.txt

CMD         . /opt/venv/bin/activate && exec python app.py
