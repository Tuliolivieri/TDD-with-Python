import json

from pyparsing import Dict

def load_json(path_to_file: str) -> list[Dict]:
    '''retorna uma lista de objetos a partir do
    arquivo em path_to_file'''
    with open(path_to_file) as file:
        return json.loads(file.read())


def order_by(field: str, data: list[Dict], reverse=False) -> None:
    '''ordena [data] pelo campo field, crescente se reverse=False
    ou não fornecido'''
    data.sort(key=lambda x: x[field], reverse=reverse)


