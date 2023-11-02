import json
from pathlib import Path


def read_json_file(name: str, cls=None):
    info = None
    path = Path(Path.cwd().parent, "model", name)
    with open(str(path)) as file:
        info = json.load(file)
        print(info)
    return info


def create_json_file(name: str, data, cls=None):
    path = Path(Path.cwd().parent, "model", name)
    with open(str(path), 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2, cls=cls)


if __name__ == "__main__":
    data = [('Zoo', 100),
            ('Small bed', 1),
            ('Big bed', 2)]
    create_json_file("rooms_time_list", data)
    read_json_file("rooms")

