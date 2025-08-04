import pytest

from main import parse_log_file, group_by_url, calculate_average_response_time


def test_parse_log_file(test_log_file, test_log_data):
    """Корректное чтение и парсинг файла."""
    log_data = parse_log_file(test_log_file)
    assert len(log_data) == len(test_log_data)
    assert log_data[0]['url'] == '/api/context/...'
    assert log_data[0]['response_time'] == 0.024


def test_group_by_url(test_log_data):
    """Корректная группировка по URL."""
    url_data = group_by_url(test_log_data)
    assert '/api/context/...' in url_data
    assert '/api/homeworks/...' in url_data
    assert len(url_data['/api/context/...']) == 3
    assert len(url_data['/api/homeworks/...']) == 2
    assert url_data['/api/context/...'] == [0.024, 0.02, 0.024]
    assert url_data['/api/homeworks/...'] == [0.06, 0.032]


@pytest.mark.parametrize("url_data, expected", [
    (
        {'/api/context': [0.1, 0.3]},
        [('/api/context', 2, 0.2)]
    ),
    (
        {'/api/homeworks': [0.2]},
        [('/api/homeworks', 1, 0.2)]
    ),
    (
        {'/api/context': [0.1, 0.3], '/api/homeworks': [0.2]},
        [('/api/context', 2, 0.2), ('/api/homeworks', 1, 0.2)]
    ),
    (
        {},
        []
    )
])
def test_calculate_average_response_time(url_data, expected):
    """Тест: расчёт среднего времени ответа с разными входными данными."""
    result = calculate_average_response_time(url_data)
    result_rounded = [(
        url, count, response_time
    ) for url, count, response_time in result]
    expected_rounded = [(
        url, count, response_time
    ) for url, count, response_time in expected]
    assert result_rounded == expected_rounded
