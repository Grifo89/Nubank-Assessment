import json, sys
from typing import List, Any

class DataProcessing():
    """
    A class for processing financial transactions.

    Attributes:
    transactions (List[Any]): A list of financial transactions.
    """
    def __init__(self):
        self.transactions: List[Any] = []

    def _stdin(self) -> None:
        """
        Reads a JSON array of transactions from standard input.

        Raises:
        Exception: If the input is not a valid JSON array.
        """
        try:
            print("\nEnter/Paste your transactions, press enter and Ctrl-D to process them.\n")
            lines = sys.stdin.readlines()
            for transaction in lines:
                transaction_data = json.loads(transaction.strip())
                self.transactions.append(transaction_data)
        except json.JSONDecodeError:
            print("\nThere was an Error. Please enter a valid JSON array\n")

    def get_transactions(self) -> List[Any]:
        """
        Gets the list of transactions processed by the class.

        Returns:
        List[Any]: A list of financial transactions.
        """
        self._stdin()
        return self.transactions