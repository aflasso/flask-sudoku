
def test_home_page(client):
    response = client.get('/sudoku')

    assert response.status_code == 200

