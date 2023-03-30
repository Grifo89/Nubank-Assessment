from enum import Enum
from typing import NamedTuple


class TransactionOperation(Enum):
    BUY = "buy"
    SELL = "sell"


class Transaction(NamedTuple):
    """
    A class representing a financial transaction.

    Attributes:
    operation (str): The type of transaction ('buy' or 'sell').
    unit_cost (float): The cost of one unit of the asset in the transaction.
    quantity (int): The quantity of units of the asset in the transaction.
    """

    operation: TransactionOperation
    unit_cost: float
    quantity: int


class Tax(NamedTuple):
    """
    A class representing a tax paid on a transaction.

    Attributes:
    tax (float): The amount of tax paid on the transaction.
    """

    tax: float
