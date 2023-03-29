import json
from typing import List

import pytest

from models.models import Transaction


class TestDataProcessing:
    @pytest.mark.parametrize(
        "data, expected",
        [
            (
                [
                    '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000}]\n',
                    '[{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":10.00, "quantity": 5000}]\n',
                ],
                [
                    [
                        {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
                        {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
                    ],
                    [
                        {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
                        {"operation": "sell", "unit-cost": 10.00, "quantity": 5000},
                    ],
                ],
            )
        ],
    )
    def test_stdin(self, data: str, expected: List[Transaction]):
        transactions = []
        for transaction in data:
            transaction_data = json.loads(transaction.strip())
            transactions.append(transaction_data)
        assert transactions == expected
