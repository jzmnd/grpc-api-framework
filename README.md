# Modular python gRPC API template

Simple modular template for a python gRPC API.
Uses `buf` (https://buf.build/product/cli) to lint and do code and doc generation.

## Generate protobuf code

Generate protobuf Python code before either running in dev mode or building a Docker image.

```bash
make grpc-gen
```

## Dev mode

```bash
make launch-dev
```

## Dockerized version

```bash
make build
make launch

# To shutdown
make stop
```

## Example request

```bash
grpcurl --plaintext -d '{"name": "Alex", "age": 10, "title": "TITLE_MONARCH"}' localhost:50051 greeter.v1.GreeterService.Reply
```

## Protobuf generated docs

Generated docs are located [here](./generated/docs/README-PROTO.md).
