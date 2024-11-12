# Key Tracking System

## Requirements

- Python 3.10+
- pip
- docker

## Installation

```bash
pip install -r requirements.txt
```

## Before running the server

Pull the mongo image

```bash
docker pull mongo
```

Run the mongo container

```bash
docker run --name mongodb -p 27017:27017 mongo
```

add `-d` above to run in detached mode.

Kill the mongo container

```bash
docker kill mongodb
docker rm mongodb
```

## Running the server

```bash
fastapi dev main.py
```

## Testing

```bash
python test_create_get_keys.py
```
