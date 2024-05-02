"""
This module contains the IProblemSolver interface.
"""

from abc import ABC, abstractmethod


class IProblemSolver(ABC):
    """
    This interface defines the contract for problem-solving classes.
    """

    @abstractmethod
    def compute_result(self,data):
        """
        Computes and returns the result based on the input data.
        """
