"""The sample class test which includes the abstract class and its child class"""
from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    """The abstract class which represents the base class of all kinds of document"""
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def get_title(self):
        """Set the title"""

    @abstractmethod
    def set_title(self, title):
        """Get the title"""


class Document(Entity):
    def __init__(self, title):
        super().__init__(title)

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title
