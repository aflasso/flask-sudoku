"""
This module contains de sudoku_verifier class
"""
from flaskr.interfaces.i_problem_solver import IProblemSolver

class SudokuVerifier(IProblemSolver):
    """
    This class verifies if a sudoku is valid, through the IProblemSolver contract
    """

    def compute_result(self, data):
        """
        Computes the result of the given problem in the data.
        """
        return self.verify_sudoku(data)

    def get_rows(self,sudoku:list):
        """
        Gets the rows of the sudoku.
        """

        result_rows = []

        for row in sudoku:
            copy_row = row[:]
            copy_row.sort()
            result_rows.append(copy_row)

        return result_rows

    def get_columns(self, sudoku):
        """
        Gets the columns of the sudoku.
        """

        result_columns = []

        for i in range(9):
            column = []
            for j in range(9):
                column.append(sudoku[j][i])

            column.sort()
            result_columns.append(column)

        return result_columns


    def get_grids(self, sudoku: list):
        """
        Gets the grids of the sudoku.
        """
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

    def verify_one_sudoku_section(self, section: list):
        """
        Verifies one section of the sudoku for repeated numbers.
        """

        repited_numbers = []

        for number in section:

            row_copy = section[:]

            row_copy.remove(number)

            is_repited = self.binary_search(row_copy, number)

            if is_repited:

                if number not in repited_numbers:
                    repited_numbers.append(number)

        return repited_numbers

    def verify_sudoku_section(self, section:list[list]):
        """
        Verifies one section of the sudoku for conflicts.
        """

        conflict_section = []

        section_number = 1
        for one_section in section:

            conflicts_in_section = self.verify_one_sudoku_section(one_section)

            if conflicts_in_section:

                conflict_section.append({f'{section_number}' : conflicts_in_section})

            section_number += 1

        return conflict_section

    def verify_sudoku(self, sudoku):
        """
        Verifies the overall validity of the sudoku.
        """

        rows = self.get_rows(sudoku)
        columns = self.get_columns(sudoku)
        grids = self.get_grids(sudoku)

        conflicts_rows = self.verify_sudoku_section(rows)
        conflicts_columns = self.verify_sudoku_section(columns)
        conflicts_grids = self.verify_sudoku_section(grids)

        is_valid = not conflicts_rows and not conflicts_columns and not conflicts_grids

        result = {
            'valid' : is_valid,
            'conflict_rows' : conflicts_rows,
            'conflict_columns' : conflicts_columns,
            'conflict_grids' : conflicts_grids
        }

        return result

    def binary_search(self, arr, target):
        """
        Performs a binary search on a sorted list.
        """

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2


            if arr[mid] == target:
                return True

            elif arr[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return False
