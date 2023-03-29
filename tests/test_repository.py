from capital_gains.repository import TransactionRepository
import pytest

class TestRepository:
 
    repository = TransactionRepository()
    
    def test_current_quantity(self):
       self.repository.set_current_quantity(2000)
       assert self.repository.get_current_quantity() == 2000

    def test_taxes(self):
        self.repository.set_taxes(300)
        self.repository.set_taxes(500)
        assert self.repository.get_taxes() == [{'tax': 300}, {'tax': 500}]

    def test_current_buy_price(self):
        self.repository.set_current_buy_price(1234)
        assert self.repository.get_current_buy_price() == 1234

    @pytest.mark.parametrize('lost_profit', [-40000, 30000])
    def test_lost_profit(self,lost_profit):
        self.repository.set_lost_profit(lost_profit)
        if lost_profit < 0:
            assert self.repository.get_lost_profit() == -40000
        else:
            assert self.repository.get_lost_profit() == -10000