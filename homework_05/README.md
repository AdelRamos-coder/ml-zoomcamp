# Homework 5 - Deployment

ML Zoomcamp 2026, module 5.

In this homework I loaded the course model (pipeline.bin), served it with FastAPI and ran it inside Docker.

First I checked the model file:

```
sha256sum pipeline.bin
1646bbdcd38d4f044da6b630c5b332c93a314245a8c21929011c42de51f629f1  pipeline.bin
```

it matches the one in the homework.

## Answers

- Q1: uv 0.11.32
- Q2: 1.7.2
- Q3: 0.533
- Q4: 0.770
- Q5: python:3.11.15-slim-bookworm
- Q6: 0.770

## Notes

Install the environment:

```
uv sync --locked
uv run python smoke_test.py
```

Q3 - load the model with pickle:

```
uv run python q3_predict.py
```

got 0.532994 -> 0.533

Q4 - run the API:

```
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

and in another terminal:

```
uv run python q4_request.py
```

response: `{'conversion_probability': 0.769799, 'conversion': True}`

Q5 - the base image is in the first line of the Dockerfile.

Q6 - docker:

```
docker build -t zoomcamp-model:2026-hw5 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
python q6_test.py
```

same result as the API (0.770), makes sense since it's the same model and same dependencies.
