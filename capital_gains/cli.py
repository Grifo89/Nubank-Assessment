from typing import List

from capital_gains.repository import TransactionRepository
from capital_gains.models import Transaction, Tax


class TransactionController():
    """
    A class that handles transactions for a particular asset.
    """

    # class variable
    tax_rate = 0.2

    def __init__(self) -> None:
        """
        Initializes a new instance of the TransactionController class.
        """
        self.repository = TransactionRepository()

    def _new_buy_price(self, transaction: Transaction) -> None:
        """
        Calculates the new weighted buy price based on a new buy transaction.

        Args:
            transaction (dict): A dictionary containing the details of the buy transaction,
            including the quantity and unit cost of the asset.

        Returns:
            None.
        """
        numerator = 0
        current_quantity = self.repository.get_current_quantity()
        weighted_price = self.repository.get_current_buy_price()
        denominator = current_quantity + transaction['quantity']
        numerator = (current_quantity * weighted_price) + (transaction['quantity'] * transaction['unit-cost'])
        weighted_price = round((numerator/denominator), 2)
        self.repository.set_current_buy_price(weighted_price)

    def _buy(self, transaction: Transaction) -> None:
        """
        Executes a buy transaction for the asset.

        Args:
            transaction (dict): A dictionary containing the details of the buy transaction,
            including the quantity and unit cost of the asset.

        Returns:
            None.
        """
        quantity = transaction['quantity']
        self._new_buy_price(transaction)
        self.repository.set_current_quantity(quantity)
        self.repository.set_taxes(0)
        

    def _sell(self, transaction: Transaction) -> None:
        """
        Executes a sell transaction for the asset.

        Args:
            transaction (dict): A dictionary containing the details of the sell transaction,
            including the quantity and unit cost of the asset.

        Returns:
            None.
        """
        quantity = transaction['quantity']
        operation_amount = transaction['quantity'] * transaction['unit-cost']
        self.repository.set_current_quantity(-quantity)
        profit = self._profit_calculator(transaction)
        tax = self._tax_calculator(profit, operation_amount)
        self.repository.set_taxes(tax)

    def _tax_calculator(self, profit: float, operation_amount: float) -> float:
        """
        Calculates the tax amount for a sell transaction.

        Args:
            profit (float): The profit of the sell transaction.
            operation_amount (float): The total amount of the sell transaction.

        Returns:
            float: The tax amount for the sell transaction.
        """

        lost_profit = self.repository.get_lost_profit()
        self.repository.set_lost_profit(profit)
        total_profit = profit + lost_profit
        if operation_amount > 20000 and total_profit > 0:
           return total_profit * self.tax_rate
        else:
           return 0

    def _profit_calculator(self, transaction: Transaction) -> float:
        """
        Calculates the profit of a sell transaction.

        Args:
            transaction (dict): A dictionary containing the details of the sell transaction,
            including the quantity and unit cost of the asset.

        Returns:
            float: The profit of the sell transaction.
        """
        buy_price = self.repository.get_current_buy_price()
        profit = (transaction['unit-cost'] - buy_price) * transaction['quantity']
        return round(profit, 2)

    def processing_transactions(self, 
            transactions: List[Transaction]) -> List[Tax]:
        """
        Process a list of transactions and return the corresponding taxes.

        Parameters:
        transactions (List[Transaction]): A list of transactions to be processed.

        Returns:
        List[Tax]: A list of taxes corresponding to the processed transactions.
        """
        for transaction in transactions:
            match transaction['operation']:
                case 'buy':
                    self._buy(transaction)
                case 'sell':
                    self._sell(transaction)
                case _:
                    raise Exception("Invalid transation")
        taxes = self.repository.get_taxes()
        print(taxes,"\n")