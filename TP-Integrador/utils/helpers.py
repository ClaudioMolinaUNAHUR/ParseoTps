import json

def to_json(data):
    return json.dumps(
        data,
        default=lambda o: o.__dict__,
        indent=2,
        ensure_ascii=False,
    )
