## Тестовое задание:
### Краткая суть:
Скрипт читает файл и формирует отчет со списком эндпоинтов, количеством запросов по каждому эндпоинту и средним временем ответа. Пути к файлам и название отчета передаются как параметры, например python main.py --file file.log --report average.
### Примеры запуска скрипта:
```
python main.py --file example1.log --report average
URL                         Total requests    Average response time
------------------------  ----------------  -----------------------
/api/context/...                        21                0.0426667
/api/homeworks/...                      71                0.158423
/api/specializations/...                 6                0.0346667
/api/users/...                           1                0.072
/api/challenges/...                      1                0.056
(venv) 
```
```
python main.py --file example2.log --report average
URL                         Total requests    Average response time
------------------------  ----------------  -----------------------
/api/homeworks/...                   55241                0.0926407
/api/context/...                     43907                0.0193524
/api/specializations/...              8329                0.0517524
/api/users/...                        1446                0.0657268
/api/challenges/...                   1475                0.0781939
(venv)
```
```
python main.py --file example1.log example2.log --report average
URL                         Total requests    Average response time
------------------------  ----------------  -----------------------
/api/context/...                     43928                0.0193635
/api/homeworks/...                   55312                0.0927252
/api/specializations/...              8335                0.0517401
/api/users/...                        1447                0.0657312
/api/challenges/...                   1476                0.0781789
(venv)
```
### Работа тестов:
```
pytest
============================================================================================== test session starts ==============================================================================================
platform win32 -- Python 3.13.4, pytest-8.4.1, pluggy-1.6.0
rootdir: *****\test_task_log_file_processing
collected 7 items                                                                                                                                                                                                

tests\test_logic.py .......
```
