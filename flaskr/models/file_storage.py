"""
This module contains the FileStorage class.
Has the responsability to manage the file process
"""

from flaskr.interfaces.i_storage import IStorage

class FileStorage(IStorage):
    """
    This class represents a file storage utility.
    """

    @staticmethod
    def read_data():

        readed_data = []

        with open('./flaskr/files/input.txt', 'r', encoding='UTF-8') as file:

            first_line = int(file.readline().strip())

            print(first_line)

            for _ in range(first_line):
                sudoku = []

                line = file.readline()
                while line != '\n' and line != '':
                    
                    row = [int(number) for number in line.strip()]

                    sudoku.append(row)

                    line = file.readline()
                readed_data.append(sudoku)


        return readed_data


