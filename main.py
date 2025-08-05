import json
import argparse
from tabulate import tabulate


def parse_log_file(file_path):
    """Функция парсит json-файл в словарь."""
    with open(file_path, 'r') as file:
        log_data = [json.loads(line) for line in file]
    return log_data


def group_by_url(log_data):
    """Функция группирует данные по URL."""
    url_data = {}
    for log in log_data:
        url = log['url']
        if url not in url_data:
            url_data[url] = []
        url_data[url].append(float(log['response_time']))
    return url_data


def calculate_average_response_time(url_data):
    """Функция рассчитывает среднее время ответа для каждой группы по URL."""
    response_data = []
    for url, response_time in url_data.items():
        total_time = sum(response_time)
        count = len(response_time)
        average_time = total_time / count
        response_data.append((url, count, average_time))
    return response_data


def print_table(data):
    """Функция отвечает за вывод данных в виде таблицы."""
    print(tabulate(
        data,
        headers=['URL', 'Total requests', 'Average response time'],
        tablefmt='simple'
    ))


def main():
    """Основная логика работы скрипта."""
    parser = argparse.ArgumentParser(description='Обработка лог-файла')
    parser.add_argument(
        '--file',
        required=True,
        nargs='+',
        help='Путь к лог-файлу'
    )
    parser.add_argument(
        '--report',
        default='average',
        choices=['average'],
        help='Тип отчета'
    )
    args = parser.parse_args()

    log_data = []
    for file in args.file:
        try:
            file_log_data = parse_log_file(file)
            log_data.extend(file_log_data)
        except Exception as e:
            print(f'Ошибка чтения {file}: {e}')
            continue

    url_data = group_by_url(log_data)

    if args.report == "average":
        average_data = calculate_average_response_time(url_data)
        print_table(average_data)
    else:
        print('Неподдерживаемый тип отчета')


if __name__ == "__main__":
    main()
