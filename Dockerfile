FROM python:3.8-slim

LABEL maintainer="Jez Smith"

RUN apt-get update

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ENV SRC_DIR api
ENV GEN_DIR generated
ENV CODE_DIR /opt/grpc-api-framework
COPY ./${SRC_DIR} ${CODE_DIR}/${SRC_DIR}
COPY ./${GEN_DIR} ${CODE_DIR}/${GEN_DIR}
WORKDIR ${CODE_DIR}

ENV PYTHONPATH "${PYTHONPATH}:./${GEN_DIR}/python/"

EXPOSE 50051

CMD ["python", "api/server.py"]
