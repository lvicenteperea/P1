from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def call_procedure(self, procedure_name, *args):
        pass
