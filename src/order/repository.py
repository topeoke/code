import sys
from abc import ABC, abstractclassmethod
sys.path.insert(0, '/Users/temi/cosmic-code/code/src/order')
from domain.model import Portfolio
from typing import List


class AbstractRepository(ABC):

    @abstractclassmethod
    def add(self, portfolio: Portfolio):
        raise NotImplementedError

    def get(self, reference: str) -> Portfolio:
        raise NotImplementedError


class FakeRepository(AbstractRepository):
    def __init__(self, portfolio: List[Portfolio]):
        self.portfolio = portfolio
    
    def get(self):
        return [i.id for i in self.portfolio]

    def add(self, port: Portfolio) -> str:
        ref_list =[ i.id for i in self.portfolio]
        if port.id not in ref_list:
            self.portfolio.append(port)
            return port.id
    
    def list(self):
        return self.portfolio


    def commit(self):
        print ('Saving to database....')
    

