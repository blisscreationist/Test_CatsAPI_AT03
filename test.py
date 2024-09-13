import pytest
from main import get_random_cat_image

def test_get_random_cat_image(mocker): # Проверяем успешный запрос и возвращаем правильный URL
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://beautifulcats.com/cat.jpg'}]

    cat_image_url = get_random_cat_image()
    assert cat_image_url == 'https://beautifulcats.com/cat.jpg'

def test_get_random_cat_image_error(mocker): # Проверяем неуспешный запрос
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    cat_image_url = get_random_cat_image()
    assert cat_image_url is None