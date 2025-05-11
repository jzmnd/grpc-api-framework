FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL maintainer="Jez Smith"

ENV SRC_DIR=api
ENV GEN_DIR=generated
ENV CODE_DIR=/opt/grpc-api-framework
WORKDIR ${CODE_DIR}

COPY ./ ./

RUN uv sync --locked

ENV PYTHONPATH="${PYTHONPATH}:./${GEN_DIR}/python/"

EXPOSE 50051

CMD ["uv", "run", "python", "api/server.py"]
