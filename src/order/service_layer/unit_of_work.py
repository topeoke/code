import sys
sys.path.insert(0, '/Users/temi/cosmic-code/code/src/order')
from abc import ABC, abstractmethod
from adapters import repository

class AbstractUnitOfWork(ABC):
    #portfolio: repository.AbstractRepository

    def __exit__(self, *args):
        pass

    @abstractmethod
    def __enter__(self, *args):
        raise NotImplementedError

class FakeUnitOfWork(AbstractUnitOfWork):

    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.committed = False

    def __enter__(self):
        self.portfolio = repository.FakeRepository(self.portfolio)
        return self.portfolio

    def __commit__(self):
        self.committed = True
    
    def __exit__(self, *args):
        pass
