"""
This module contains the IStorage interface
"""

from abc import ABC, abstractmethod

class IStorage(ABC):
    """
    This interface defines the contract for storage classes.
    """

    @abstractmethod
    def read_data(self):
        """
        Reads and returns the readed data, or None if is no data.
        """

    @abstractmethod
    def save_data(self,data):
        """
        Saves the data on the storage.
        """
