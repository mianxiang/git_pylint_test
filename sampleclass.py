from abc import ABCMeta, abstractmethod

class entity(metaclass=ABCMeta):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self):
        pass

class Document(entity):
    def __init__(self, title):
        super().__init__(title)

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title