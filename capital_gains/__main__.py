from data_processing import DataProcessing
from cli import TransactionController


def main():
    operations = DataProcessing().get_transactions()
    print('\nProcessing operation...\n')
    for operation in operations:
        processor = TransactionController()
        processor.processing_transactions(operation)

main()