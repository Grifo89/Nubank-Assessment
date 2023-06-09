from typing import List

from models.models import Tax


class TransactionRepository:
    """
    A repository for tracking transaction data.

    Attributes:
    current_quantity_tracker (int): The current quantity of assets held.
    taxes (List[float]): A list of taxes paid on transactions.
    current_buy_price (float): The current buying price of the asset.
    lost_profit (float): The current amount of lost profit due to sell transactions.
    """

    def __init__(self) -> None:
        self.current_quantity_tracker: int = 0
        self.taxes: List[float] = []
        self.current_buy_price: float = 0
        self.lost_profit: float = 0

    def set_current_quantity(self, value: int) -> None:
        """
        Set the current quantity of assets held.

        Parameters:
        value (int): The new value of the current quantity.
        """
        self.current_quantity_tracker += value

    def get_current_quantity(self) -> int:
        """
        Get the current quantity of assets held.

        Returns:
        int: The current quantity of assets held.
        """
        return self.current_quantity_tracker

    def set_taxes(self, tax: float) -> None:
        """
        Set the tax paid on a transaction.

        Parameters:
        tax (float): The amount of tax paid on the transaction.
        """
        self.taxes.append(tax)

    def get_taxes(self) -> List[Tax]:
        """
        Get a list of taxes paid on transactions.

        Returns:
        List[Tax]: A list of taxes paid on transactions.
        """
        tmp = []
        for tax in self.taxes:
            if type(tax) == str:
                tmp.append({"error": tax})
            else:
                tmp.append({"tax": tax})
        return tmp

    def set_current_buy_price(self, value: float) -> None:
        """
        Set the current buying price of the asset.

        Parameters:
        value (float): The new value of the current buying price.
        """
        self.current_buy_price = value

    def get_current_buy_price(self) -> float:
        """
        Get the current buying price of the asset.

        Returns:
        float: The current buying price of the asset.
        """
        return self.current_buy_price

    def set_lost_profit(self, lost: float) -> None:
        """
        Adjust the lost profit due to sell transactions.

        Parameters:
        lost (float): The amount of lost profit due to a sell transaction.
        """
        if self.lost_profit + lost <= 0:
            self.lost_profit += lost
        else:
            self.lost_profit = 0

    def get_lost_profit(self) -> float:
        """
        Get the current amount of lost profit due to sell transactions.

        Returns:
        float: The current amount of lost profit due to sell transactions.
        """
        return self.lost_profit
