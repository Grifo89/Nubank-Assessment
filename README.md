Capital Gains 🤑 💸 CLI Application
============

This is a CLI application capable of processing stock operations and calculates the taxes over the transactions. This is an assesment proposed by Nubank. [This is the assessment sheet](assessment.pdf).

This application is built based on a MVC architecture approach. 

---
## Requirements

This application requires `python >= 3.11`

---

## Features
- Multi-line input.
- Input redirection using `files.txt`
- MVC architecture approach
---

## Setup
In order to get up and running the application you should:
 - Unzip the project and get inside the root directory.
 - Install `python >= 3.11`
 - Create a virtual environment inside the root directory `python3 -m venv venv`
 - Activate the virtual environment `source venv/bin/activate`
 - Install the required packages `pip install -r requirements.txt`

---

## Usage

Once you have the needed setup, you can start using the application. 

Being at the root directory, the application runs typing the following command `python capital_gains`, after typing the command there are two options on wich you can choose:

1. You can press Enter and get into the console interactive mode, where you can pass in the stock operation, which is made up of many transaction. When you finish to do it press `Enter` and `Ctrl + d` to execute the program. 

2. You can, after typing the command, redirect a file to the application as an input using **input redirection** `python capital_gains < test.txt`

### Input Example

Each operation is made by many transactions. The application can process several operations as an input. 

The input should have a operation per line.

Operation Input Data
> `[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000}]`

Output Data
> `[{"tax":0.00}, {"tax":10000.00}]`
---
## Testing

If you would like to run the application tests, at the root directory run the following command `python -m pytest`.

---
## Author

🤖 Christian Miño 💪🏻
