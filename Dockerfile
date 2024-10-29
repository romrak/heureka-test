FROM python:3.13.0-slim AS build-image

COPY pyproject.toml .
COPY heureka heureka
COPY README.md .

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate && python3 -m pip install build && pip install .

FROM python:3.13.0-slim AS run-image
COPY --from=build-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /opt/heureka

COPY heureka heureka
COPY heureka/main.py .
#CMD ["python -u ./main.py"]
CMD ["python", "-u","main.py"]

