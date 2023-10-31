import json


def read_json_file(name: str, cls=None):
    data = None
    with open(f'{name}.txt') as file:
        data = json.load(file)
        print(data)
    return data


def create_json_file(name: str, data, cls=None):
    with open(f'{name}.txt', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2, cls=cls)


if __name__ == "__main__":
    data = [('Zoo', 100),
            ('Small bed', 1),
            ('Big bed', 2)]
    create_json_file("rooms_time_list", data)
    read_json_file("rooms")

