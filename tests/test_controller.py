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
        This mocking function tests the computed weighted price for calculating profit.

        Based of this formula: ((current_quantity * current_weighted_price) + (transaction_quantity * transaction_price))/ (current_quantity + transaction_quantity)
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
        """
        buy_price = 12
        profit = (transaction["unit-cost"] - buy_price) * transaction["quantity"]
        print(profit)
        assert round(profit, 2) == expected
