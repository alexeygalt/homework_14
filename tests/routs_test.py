from main import app
import pytest

# пытаясь запусить данный тест получаю исключение 500 != 200, хотя в Postman и Браузере 200
# помогите)
def test_get_title_page():
    response = app.test_client().get('/movie/187')
    assert response.status_code == 200
    # assert type(response.json) == dict
