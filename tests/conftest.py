import json

import pytest


@pytest.fixture
def test_log_data():
    """Возвращает тестовые данные."""
    return [
        {"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.024, "http_user_agent": "..."},
        {"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.02, "http_user_agent": "..."},
        {"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/context/...", "request_method": "GET", "response_time": 0.024, "http_user_agent": "..."},
        {"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/homeworks/...", "request_method": "GET", "response_time": 0.06, "http_user_agent": "..."},
        {"@timestamp": "2025-06-22T13:57:32+00:00", "status": 200, "url": "/api/homeworks/...", "request_method": "GET", "response_time": 0.032, "http_user_agent": "..."},
    ]


@pytest.fixture
def test_log_file(tmp_path, test_log_data):
    """Создает файл с тестовыми данными."""
    file_path = tmp_path / "test.log"
    with open(file_path, 'w') as f:
        for entry in test_log_data:
            f.write(json.dumps(entry) + '\n')
    return file_path


@pytest.fixture
def test_log_second_file(tmp_path, test_log_data):
    """Создает файл с тестовыми данными."""
    file_path = tmp_path / "test2.log"
    with open(file_path, 'w') as f:
        for entry in test_log_data:
            f.write(json.dumps(entry) + '\n')
    return file_path
