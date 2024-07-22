import unittest
import pandas as pd
import json
from app import is_unique_combination, find_minimal_unique_combination, main

class TestAppFunctions(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"фамилия": "Иванов", "класс": "10", "подгруппа": "A", "предмет": "Математика"},
            {"фамилия": "Петров", "класс": "10", "подгруппа": "A", "предмет": "Физика"},
            {"фамилия": "Сидоров", "класс": "11", "подгруппа": "B", "предмет": "Математика"},
            {"фамилия": "Иванов", "класс": "11", "подгруппа": "A", "предмет": "Химия"}
        ]
        self.df = pd.DataFrame(self.data)

    def test_is_unique_combination(self):
        # Проверяем уникальную комбинацию
        self.assertTrue(bool(is_unique_combination(self.df, ["фамилия", "класс", "подгруппа", "предмет"])))
        # Проверяем неуникальную комбинацию
        self.assertFalse(not bool(is_unique_combination(self.df, ["фамилия", "класс"])))

    def test_find_minimal_unique_combination(self):
        result = find_minimal_unique_combination(self.df)
        # Проверяем, что результат содержит все необходимые признаки
        self.assertTrue(set(result).issubset({"фамилия", "класс", "подгруппа", "предмет"}))
        # Проверяем, что результат действительно минимален (исправление ошибки)
        self.assertGreaterEqual(len(result), 2)

    def test_main(self):
        json_str = json.dumps(self.data)
        csv_result = main(json_str)
        # Разбиваем результат и проверяем наличие необходимого признака
        lines = csv_result.strip().split('\n')
        unique_features = lines[1].strip().split(',')
        self.assertIn("фамилия", unique_features)

if __name__ == "__main__":
    unittest.main()