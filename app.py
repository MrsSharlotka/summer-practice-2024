import json
import os
import itertools
import pandas as pd
from typing import List


def is_unique_combination(df: pd.DataFrame, combination: List[str]) -> bool:
    # Проверка на уникальность комбинации признаков для всех сущностей.
    return df.duplicated(subset=combination).sum() == 0


def find_minimal_unique_combination(df: pd.DataFrame) -> List[str]:
    # Находит минимальную по составу комбинацию признаков, которая уникально идентифицирует сущность.
    columns = df.columns
    for r in range(1, len(columns) + 1):
        for combination in itertools.combinations(columns, r):
            if is_unique_combination(df, list(combination)):
                return list(combination)
    return []


def main(json_str: str) -> str:
    # Главная функция, принимающая JSON-строку с данными и возвращающая минимальный набор уникальных признаков.
    data = json.loads(json_str)
    df = pd.DataFrame(data)

    minimal_combination = find_minimal_unique_combination(df)

    output = pd.DataFrame(minimal_combination, columns=["unique_features"])
    return output.to_csv(index=False, encoding='utf-8')


if __name__ == "__main__":
    # Пример использования с тестовыми данными
    for file in os.listdir('.'):
        if file.endswith('.json'):
            with open(file, "r", encoding="utf-8") as json_file:
                json_data = json_file.read()
    print(main(json_data))
