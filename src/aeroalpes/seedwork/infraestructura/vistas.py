from abc import ABC, abstractmethod

class Vista(ABC):

    @abstractmethod
    def obtener_todos(self, **kwargs):
        ...

    @abstractmethod
    def obtener_por(self, **kwargs):
        ...