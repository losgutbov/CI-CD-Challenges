from app import app


def test_index_route():

    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "<p>Olá, Mundo!</p>"


def test_teste_route():

    response = app.test_client().get("/teste/")

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Testado!!"
