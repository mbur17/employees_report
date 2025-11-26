## employee-reports

Скрипт генерирует отчёты на основе CSV-файлов с данными о сотрудниках.  
Используются стандартные библиотеки (`argparse`, `csv`, `logging`), а таблица выводится с помощью `tabulate`.

Текущий реализованный отчёт:
-   **`performance`** — средняя эффективность по позициям, сортировка по убыванию.

Архитектура реализована с учетом возможности добавлять новые отчёты.

### Запуск
Пример запуска:
```bash
python3 main.py --files employees1.csv employees2.csv --report performance
```
Ожидаемый вывод:

![coverage](https://private-user-images.githubusercontent.com/153096322/519046306-4f4cf5ac-1cc1-4e8e-bf00-e0e08fbe6d71.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxNDI3NDksIm5iZiI6MTc2NDE0MjQ0OSwicGF0aCI6Ii8xNTMwOTYzMjIvNTE5MDQ2MzA2LTRmNGNmNWFjLTFjYzEtNGU4ZS1iZjAwLWUwZTA4ZmJlNmQ3MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEyNlQwNzM0MDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mN2RkZjNjNDQyYjZmNTNmMjM0ZGQ0OGM1YTVkMWVjZTY2M2YyZTI0NTc0YmQ1Mzk3MzY1YmE4ODczYzA3YTlhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.K8YplGX20_6IVaVhvcSvXfdIeVH9mcaNJ1NeT_7Qlzc)

### Как устроен проект
```bash
employees_report/
├─ main.py                # CLI, вывод таблицы
├─ readers.py 						# чтение CSV-файлов
├─ reporting/
   ├─ base.py             # базовый класс отчёта
   ├─ performance.py      # отчёт средней эффективности
   └─ __init__.py         # реестр доступных отчётов
└─ tests/
```
### Как добавить новый отчёт
1.  Создать файл `reporting/my_report.py`
2.  Наследоваться от `BaseReport`
3.  Реализовать:
    -   `name` — строковый идентификатор отчёта
    -   `headers` — колонки таблицы
    -   `build(rows)` — формирование результата
4.  Зарегистрировать отчёт в `reporting/__init__.py`

### Тестирование
Тесты запускаются командой:
`pytest`

Покрытие кода:
`pytest --cov`

![coverage](https://private-user-images.githubusercontent.com/153096322/519046783-9494e7a4-84d2-4115-bb46-cf63413994bc.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxNDI0OTYsIm5iZiI6MTc2NDE0MjE5NiwicGF0aCI6Ii8xNTMwOTYzMjIvNTE5MDQ2NzgzLTk0OTRlN2E0LTg0ZDItNDExNS1iYjQ2LWNmNjM0MTM5OTRiYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEyNlQwNzI5NTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kZmUyMjRhNTdmNGUzOGFlY2UwZTA1NzA3NzA4MTg4OTBlNjFlZjdhMmRhYTg4ZjJhY2JlOTIwMDIzNzk0MjY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.tCRQjs0Qoxty-Ku0XRigbATm1AtKua3ZOcdX88wN2ZQ)
