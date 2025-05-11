IMAGE := grpc-api-template:latest
CONTAINER := grpc-api-template-server
MODULE := api

launch-dev:
	@PYTHONPATH=$(PYTHONPATH):./generated/python/ uv run python $(MODULE)/server.py

build:
	@docker build -t $(IMAGE) .

launch:
	@docker run -d -p 50051:50051 --name $(CONTAINER) $(IMAGE)

stop:
	@docker stop $(CONTAINER) > /dev/null && echo "Stopped container $(CONTAINER)" || true
	@docker rm $(CONTAINER) 2>/dev/null || true

grpc-gen:
	@buf lint
	@buf generate

grpc-clean:
	@find ./generated -type f -name '*_pb2*' -delete

.PHONY: build launch stop grpc-clean grpc-gen launch-dev
