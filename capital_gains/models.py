from pydantic import BaseModel, Field


class Transaction(BaseModel):
    """
    A class representing a financial transaction.

    Attributes:
    operation (str): The type of transaction ('buy' or 'sell').
    unit_cost (float): The cost of one unit of the asset in the transaction.
    quantity (int): The quantity of units of the asset in the transaction.
    """
    operation: str
    unit_cost: float = Field(alias="unit-cost")
    quantity: int

class Tax(BaseModel):
    """
    A class representing a tax paid on a transaction.

    Attributes:
    tax (float): The amount of tax paid on the transaction.
    """
    tax: float