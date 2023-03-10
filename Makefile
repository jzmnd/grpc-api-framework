IMAGE := grpc-api-template:latest
CONTAINER := grpc-api-template-server
MODULE := api

launch-dev:
	@python $(MODULE)/server.py

build:
	@docker build -t $(IMAGE) .

launch:
	@docker run -d -p 50051:50051 --name $(CONTAINER) $(IMAGE)

stop:
	@docker stop $(CONTAINER) > /dev/null && echo "Stopped container $(CONTAINER)" || true
	@docker rm $(CONTAINER) 2>/dev/null || true

grpc-gen:
	@python -m grpc_tools.protoc \
		-I $(MODULE)/proto \
		--python_out=./$(MODULE)/generated \
		--grpc_python_out=./$(MODULE)/generated \
		./$(MODULE)/proto/*.proto
	@sed -i '' -E 's/^import.*_pb2/from . &/' ./$(MODULE)/generated/*.py

grpc-clean:
	@find ./$(MODULE)/generated -type f -name '*_pb2*' -delete

.PHONY: build launch stop grpc-clean grpc-gen launch-dev
