
def test_valid_sudoku(client):

    response = client.get('/')

    assert response.status_code == 200
    assert b'El sudoku es valido' in response.data
    assert b'El numero 7 esta repetido en la fila 1' in response.data
    assert b'El numero 7 esta repetido en la columna 5' in response.data
    assert b'El numero 6 esta repetido en la columna 6' in response.data
    assert b'El numero 3 esta repetido en la columna 7' in response.data
    assert b'El numero 6 esta repetido en la columna 7' in response.data
    assert b'El numero 1 esta repetido en la columna 8' in response.data
    assert b'El numero 4 esta repetido en la columna 8' in response.data
    assert b'El numero 5 esta repetido en la columna 9' in response.data
    assert b'El numero 7 esta repetido en la cuadricula 2' in response.data
    assert b'El numero 3 esta repetido en la cuadricula 3' in response.data
    assert b'El sudoku no es valido' in response.data
    assert b'El numero 6 esta repetido en la fila 7' in response.data
    assert b'El numero 6 esta repetido en la columna 4' in response.data
    assert b'El numero 6 esta repetido en la cuadricula 8' in response.data
