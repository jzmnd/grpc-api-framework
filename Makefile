IMAGE := grpc-api-template:latest
CONTAINER := grpc-api-template-server
MODULE := api

launch-dev:
	@python $(MODULE)/server.py

build:
	@docker build -t $(IMAGE) .

launch:
	@docker run -d -p 50051:50051 --name $(CONTAINER) $(IMAGE)

grpc-gen:
	@python -m grpc_tools.protoc \
		-I $(MODULE)/proto \
		--python_out=./$(MODULE)/generated \
		--grpc_python_out=./$(MODULE)/generated \
		./$(MODULE)/proto/*.proto
	@sed -i '' -E 's/^import.*_pb2/from . &/' ./$(MODULE)/generated/*.py

grpc-clean:
	@find ./$(MODULE)/generated -type f -name '*_pb2*' -delete

.PHONY: grpc-clean grpc-gen launch-dev
