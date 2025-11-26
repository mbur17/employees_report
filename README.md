## employees-report

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

![coverage](https://private-user-images.githubusercontent.com/153096322/519058259-e3a7e7d1-027c-412d-9ccc-c91e6467e1a7.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxNDQyOTcsIm5iZiI6MTc2NDE0Mzk5NywicGF0aCI6Ii8xNTMwOTYzMjIvNTE5MDU4MjU5LWUzYTdlN2QxLTAyN2MtNDEyZC05Y2NjLWM5MWU2NDY3ZTFhNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEyNlQwNzU5NTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT00YWMzMTgzNDZiZmQ2NDI5Mzk5MDE4NDMyZGE1ZWExMDE4YWEzMmM1ODMwZDJlMWJiMGQyNDM4M2EyYjNmZThhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2QQ_kd9F_fRimxlBnYL0CLhBv2150YQ0lUH-EoWUxPQ)

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

![coverage](https://private-user-images.githubusercontent.com/153096322/519058017-45477723-ca4f-4ca9-bf2e-84fd9cd08cbe.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxNDQzNjQsIm5iZiI6MTc2NDE0NDA2NCwicGF0aCI6Ii8xNTMwOTYzMjIvNTE5MDU4MDE3LTQ1NDc3NzIzLWNhNGYtNGNhOS1iZjJlLTg0ZmQ5Y2QwOGNiZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEyNlQwODAxMDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNWJmNmM0Yzk0NDQzZWJmYjExYzI3Nzk5NTVmYjIxMzFlMzVjMTVhZTA2MGMyYTc5ZjlhY2ZhNjkyMGJhMTM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.X-9v5E2r19JL1o3SdimtRf6amW0NMhGaRjrnFbVKqhE)
