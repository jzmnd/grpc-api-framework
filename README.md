# Modular python gRPC API template

Simple modular template for a python gRPC API.
Uses `buf` (https://buf.build) to lint and do code and doc generation.

## Generate protobuf code

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
```

## Example request

```bash
grpcurl --plaintext -d '{"name": "Alex", "age": 10, "title": "TITLE_MONARCH"}' localhost:50051 greeter.v1.GreeterService.Reply
```
