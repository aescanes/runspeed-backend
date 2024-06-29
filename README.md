

# Run Speed API


## Getting Started

### create local environment

```
python -m venv venv
```

### activate local environment

```
source venv/bin/activate
```

### install requirements

```
pip install -r requirements.txt
```

### run api

```
export FLASK_APP=api.py
flask run
```
or
```
python api.py
```

## Example of endpoints

### Pace to speed
```
api/v1.0/pace-to-speed/<m:s>
```
e.g.
```
api/v1.0/pace-to-speed/4:30
```

### Speed to pace
```
api/v1.0/speed-to-pace/<speed>
```
e.g.
```
api/v1.0/speed-to-pace/12.3
```
## Run tests
```
pytest
```