FROM thehale/python-poetry

COPY src/ /opt/src/
COPY input/ /opt/input/
COPY output/ /opt/output/
ADD poetry.lock /opt/
ADD pyproject.toml /opt/

WORKDIR /opt/

RUN poetry install


CMD poetry run python src/app.py
