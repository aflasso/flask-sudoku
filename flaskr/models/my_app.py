"""
This module contains the MyApp class
"""

from flaskr.models.file_storage import FileStorage

class MyApp():
    """
    This class represents the controller of the program.
    """
    
    def read_input(self):
        """
        This method returns the readed data readed by the Istorage interface contract
        """
        return FileStorage.read_data()