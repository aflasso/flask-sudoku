"""
This module contains de sudoku_verifier class
"""
from flaskr.interfaces.i_problem_solver import IProblemSolver

class SudokuVerifier(IProblemSolver):
    """
    This class verifies if a sudoku is valid, through the IProblemSolver contract
    """

    def compute_result(self, data):
        return super().compute_result(data)
    
    def get_rows(self,sudoku:list):
        
        result_rows = []

        for row in sudoku:
            row.sort()
            result_rows.append(row)

        return result_rows

    def get_columns(self, sudoku):
        result_columns = []

        for i in range(9):
            column = []
            for j in range(9):
                column.append(sudoku[j][i])
            
            column.sort()
            result_columns.append(column)
        
        return result_columns
                

    def get_grids(self, sudoku: list):
        
        result_grids = []

        for i in range(0,9,3):

            for h in range(0,9,3):
                grid = []

                for j in range(i, i+3, 1):
                    
                    for k in range(h, h+3, 1):
                        
                        grid.append(sudoku[j][k])

                grid.sort()
                result_grids.append(grid)
            
        return result_grids
