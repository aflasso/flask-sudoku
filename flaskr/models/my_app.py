"""
This module contains the MyApp class
"""

from flaskr.models.file_storage import FileStorage
from flaskr.models.sudoku_verifier import SudokuVerifier

class MyApp():
    """
    This class represents the controller of the program.
    """
    def __init__(self) -> None:

        self.sudoku_verifier = SudokuVerifier()

    def read_input(self):
        """
        This method returns the readed data readed by the Istorage interface contract
        """
        return FileStorage.read_data()

    def verify_sudoku(self, sudoku):
        """
        This method returns de computed result of the SudokuVerifier class
        """
        return self.sudoku_verifier.compute_result(sudoku)
