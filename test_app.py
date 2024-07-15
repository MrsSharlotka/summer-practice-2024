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
        self.assertTrue(is_unique_combination(self.df, ["фамилия", "класс", "подгруппа", "предмет"]))
        # Проверяем неуникальную комбинацию
        self.assertFalse(is_unique_combination(self.df, ["фамилия", "класс"]))

    def test_find_minimal_unique_combination(self):
        result = find_minimal_unique_combination(self.df)
        # Проверяем, что результат содержит все необходимые признаки
        self.assertTrue(set(result).issubset({"фамилия", "класс", "подгруппа", "предмет"}))
        # Проверяем, что результат действительно минимален
        self.assertEqual(len(result), 4)

    def test_main(self):
        json_str = json.dumps(self.data)
        csv_result = main(json_str)
        # Проверяем, что в результатах есть все необходимые признаки
        self.assertIn("unique_features", csv_result)
        self.assertIn("фамилия", csv_result)
        self.assertIn("класс", csv_result)
        self.assertIn("подгруппа", csv_result)
        self.assertIn("предмет", csv_result)

if __name__ == "__main__":
    unittest.main()
