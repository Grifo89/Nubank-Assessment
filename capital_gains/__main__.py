from capital_gains.data_processing import DataProcessing
from capital_gains.cli import TransactionController

def main():
    operations = DataProcessing().get_transactions()
    print('\nProcessing operation...\n')
    for operation in operations:
        processor = TransactionController()
        processor.processing_transactions(operation)

main()