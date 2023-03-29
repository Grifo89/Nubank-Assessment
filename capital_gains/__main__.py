import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import data_processing.data_processing as dp
import controller.cli as cli


def main():
    operations = dp.DataProcessing().get_transactions()
    for operation in operations:
        processor = cli.TransactionController()
        processor.processing_transactions(operation)

main()