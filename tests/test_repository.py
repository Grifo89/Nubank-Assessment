from repository.repository import TransactionRepository
import pytest


class TestRepository:
    """
    This class tests the TransactionRepository class.

    Attributes:
    repository: An instance of the TransactionRepository class.

    Methods:
    test_current_quantity: Test the set and get methods of the current quantity.
    test_taxes: Test the set and get methods of the taxes list.
    test_current_buy_price: Test the set and get methods of the current buy price.
    test_lost_profit: Test the set and get methods of the lost profit.
    """

    repository = TransactionRepository()

    def test_current_quantity(self):
        """
        This method tests the set and get methods of the current quantity.

        Args:
            self: the object instance

        Returns:
            None

        Raises:
            AssertionError: If the actual result of the test does not match the expected result.
        """
        self.repository.set_current_quantity(2000)
        assert self.repository.get_current_quantity() == 2000

    def test_taxes(self):
        """
        This method tests the set and get methods of the taxes list.

        Args:
            self: the object instance

        Returns:
            None

        Raises:
            AssertionError: If the actual result of the test does not match the expected result.
        """
        self.repository.set_taxes(300)
        self.repository.set_taxes(500)
        assert self.repository.get_taxes() == [{"tax": 300}, {"tax": 500}]

    def test_current_buy_price(self):
        """
        This method tests the set and get methods of the current buy price.

        Args:
            self: the object instance

        Returns:
            None

        Raises:
            AssertionError: If the actual result of the test does not match the expected result.
        """
        self.repository.set_current_buy_price(1234)
        assert self.repository.get_current_buy_price() == 1234

    @pytest.mark.parametrize("lost_profit", [-40000, 30000])
    def test_lost_profit(self, lost_profit: float):
        """
        This method tests the set and get methods of the lost profit.

        Args:
            self: the object instance
            lost_profit (float): a negative or positive integer representing the lost profit.

        Returns:
            None

        Raises:
            AssertionError: If the actual result of the test does not match the expected result.
        """
        self.repository.set_lost_profit(lost_profit)
        if lost_profit < 0:
            assert self.repository.get_lost_profit() == -40000
        else:
            assert self.repository.get_lost_profit() == -10000
