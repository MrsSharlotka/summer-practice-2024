# summer-practice-2024

##### Обзор
Этот проект решает задачу определения минимального набора признаков, которые однозначно идентифицируют сущность в наборе данных, представленных в формате JSON. Каждая сущность в JSON описывается набором признаков. Алгоритм, разработанный в этом проекте, минимизирует вычислительную сложность и количество шагов для нахождения такого набора признаков.

##### Файлы в репозитории
- app.py: Этот файл содержит основной алгоритм для поиска минимального набора признаков, который однозначно идентифицирует сущность в наборе данных, и для преобразования данных JSON в формат CSV.
- test_app.py: Этот файл содержит модульные тесты для проверки корректности алгоритма и процесса преобразования данных.
- распределение-педагогической-нагрузки.json: Пример файла JSON, содержащий описание набора сущностей с их признаками.

##### Описание алгоритма
Алгоритм разработан для выполнения следующих шагов:
- Чтение входных данных JSON: Алгоритм начинает с чтения входного файла JSON, который содержит описание сущностей и их признаков.
- Проверка уникальности комбинаций признаков: Используя функцию is_unique_combination, алгоритм проверяет, является ли текущий набор признаков уникальным для каждой сущности в наборе данных.
- Поиск минимального уникального набора признаков: С помощью функции find_minimal_unique_combination алгоритм находит минимальный по составу набор признаков, который однозначно идентифицирует каждую сущность. Алгоритм оптимизирован для выполнения за наименьшее количество шагов и с минимальной вычислительной сложностью.
- Преобразование данных в CSV: После нахождения минимального уникального набора признаков, данные преобразуются в формат CSV для дальнейшего использования или анализа.

##### Тестирование
Для запуска модульных тестов, проверяющих корректность работы алгоритма и преобразования данных, используйте следующую команду:

`python -m unittest test_app.py`

Эта команда выполнит тесты, определенные в test_app.py, чтобы убедиться, что алгоритм правильно находит минимальный уникальный набор признаков и корректно преобразует данные в CSV.

### Заключение
Этот проект предоставляет эффективное решение для нахождения минимального набора признаков, однозначно идентифицирующих сущности в наборе данных. Алгоритм минимизирует количество шагов и вычислительную сложность, обеспечивая точное и быстрое преобразование данных JSON в формат CSV. Модульные тесты гарантируют надежность и корректность работы алгоритма.
