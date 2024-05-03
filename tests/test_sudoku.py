
def test_valid_sudoku(client):

    data = {'sudoku': [[9, 2, 4, 7, 6, 3, 1, 5, 8],
                       [8, 7, 3, 4, 1, 5, 9, 2, 6],
                       [1, 6, 5, 9, 2, 8, 3, 4, 7],
                       [4, 8, 9, 6, 7, 2, 5, 1, 3],
                       [7, 5, 2, 8, 3, 1, 6, 9, 4],
                       [3, 1, 6, 5, 4, 9, 8, 7, 2],
                       [2, 3, 8, 1, 5, 7, 4, 6, 9],
                       [6, 9, 1, 2, 8, 4, 7, 3, 5],
                       [5, 4, 7, 3, 9, 6, 2, 8, 1]
                        ]
            }

    response = client.post('/validate', data = data)

    assert response.status_code == 200
    assert b'El soduku es valido' in response.data

def test_invalid_sudoku(client):

    data = {'sudoku': [ [1, 3, 7, 9, 8, 6, 4, 5, 2],
                        [9, 2, 5, 3, 4, 7, 1, 6, 8],
                        [8, 6, 4, 5, 2, 1, 9, 7, 3],
                        [7, 5, 3, 8, 1, 4, 6, 2, 9],
                        [6, 1, 2, 7, 3, 9, 8, 4, 5],
                        [4, 8, 9, 6, 5, 2, 3, 1, 7],
                        [5, 7, 1, 4, 9, 3, 2, 9, 6],
                        [2, 9, 8, 1, 6, 5, 7, 3, 4],
                        [3, 4, 6, 2, 7, 8, 5, 9, 1]
                            ]
                }

    response = client.post('/validate', data = data)

    assert response.status_code == 200
    assert b'El sudoku es invalido' in response.data
    assert b'Numero 9 repetido en la fila 7' in response.data
    assert b'Numero 9 repetido en la columna 8' in response.data
    assert b'Numero 9 repetido en alguna cuadricula' in response.data

    data2 = {'sudoku': [[1, 3, 7, 7, 8, 6, 4, 5, 5],
                        [9, 2, 5, 3, 4, 7, 1, 6, 8],
                        [8, 6, 4, 5, 2, 1, 9, 7, 3],
                        [7, 5, 3, 8, 1, 4, 6, 2, 9],
                        [6, 1, 2, 7, 3, 9, 8, 4, 5],
                        [4, 8, 9, 6, 5, 2, 3, 1, 7],
                        [5, 7, 1, 4, 9, 3, 2, 8, 6],
                        [2, 9, 8, 1, 6, 5, 7, 3, 4],
                        [3, 4, 6, 2, 7, 8, 5, 9, 1]
                            ]
                }
    
    response = client.post('/validate', data = data2)

    assert response.status_code == 200
    assert b'El sudoku es invalido' in response.data
    assert b'Numero 7 repetido en la fila 1' in response.data
    assert b'Numero 7 repetido en la columna 4' in response.data
    assert b'Numero 7 repetido en alguna cuadricula' in response.data

    assert b'Numero 5 repetido en la fila 1' in response.data
    assert b'Numero 5 repetido en la columna 9' in response.data
    assert b'Numero 5 repetido en alguna cuadricula' in response.data
