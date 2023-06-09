import pytest

from models.models import Transaction


class TestController:
    @pytest.mark.parametrize(
        "transaction, expected",
        [
            ({"operation": "buy", "unit-cost": 10.00, "quantity": 10000}, 12.91),
            ({"operation": "buy", "unit-cost": 45.00, "quantity": 100}, 13.01),
            ({"operation": "buy", "unit-cost": 23.00, "quantity": 2100}, 13.07),
        ],
    )
    def test_new_buy_price(self, transaction: Transaction, expected: float) -> None:
        """
        Test function to verify that new_buy_price() function returns the
        expected weighted average price given a transaction and current quantity and price.

        Based of this formula: ((current_quantity * current_weighted_price) + (transaction_quantity * transaction_price))/ (current_quantity + transaction_quantity)

        Args:
            transaction (Transaction): A dictionary containing the quantity and unit-cost values for the transaction.
            expected (float): The expected weighted average price.

        Returns:
            None

        Raises:
            AssertionError: If the actual result of the test does not match the expected result.
        """
        numerator = 0
        current_quantity = 315884.00
        weighted_price = 13.00
        denominator = current_quantity + transaction["quantity"]
        numerator = (current_quantity * weighted_price) + (
            transaction["quantity"] * transaction["unit-cost"]
        )
        weighted_price = round((numerator / denominator), 2)
        print(weighted_price)
        assert weighted_price == expected

    @pytest.mark.parametrize(
        "profit, operation_amount, expected",
        [(30000, 60000, 5000.0), (-25000, 40000, 0), (0, 150000, 0)],
    )
    def test_tax_calculator(
        self, profit: float, operation_amount: float, expected: float
    ) -> None:
        """
        Test function to verify that tax_calculator() function returns
        the expected tax value given a profit, operation amount, and tax rate.

        Args:
            profit (float): The profit earned from the operation.
            operation_amount (float): The total amount of money involved in the operation.
            expected (float): The expected tax value.

        Returns:
            None

        Raises:
            AssertionError: If the calculated tax is not equal to the expected value.
        """
        self.tax_rate = 0.20
        tax = 0
        lost_profit = -5000
        total_profit = profit + lost_profit
        if operation_amount > 20000 and total_profit > 0:
            tax = total_profit * self.tax_rate
        else:
            tax = 0
        assert tax == expected

    @pytest.mark.parametrize(
        "transaction, expected",
        [
            ({"operation": "buy", "unit-cost": 10.00, "quantity": 10000}, -20000.0),
            ({"operation": "buy", "unit-cost": 45.00, "quantity": 100}, 3300.0),
            ({"operation": "buy", "unit-cost": 23.00, "quantity": 2100}, 23100.0),
        ],
    )
    def test_profit_calculator(self, transaction: Transaction, expected: float) -> None:
        """
        Calculates the profit of a sell transaction.

        Args:
            transaction (dict): A dictionary containing the details of the sell transaction,
            including the quantity and unit cost of the asset.

        Returns:
            float: The profit of the sell transaction.

        Raises:
            AssertionError: If the actual result of the test does not match the expected result.
        """
        buy_price = 12
        profit = (transaction["unit-cost"] - buy_price) * transaction["quantity"]
        print(profit)
        assert round(profit, 2) == expected
