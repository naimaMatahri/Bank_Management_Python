"""
Naima Matahri
Class: CS 521 - Spring 1
Date: 02/27/2024
Final Project
Costumer Class, that creates new costumer.
"""


class Costumer:
    """Costumer class used to create a new costumer,
    with setters and getters
    """

    def __init__(self, costumer_id, name, account_number, account_type, balance):
        self._id = costumer_id
        self.__name = name
        self.__account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def set_id(self, costumer_id):
        """Set the costumer ID"""
        self._id = costumer_id

    def get_id(self):
        """Return the costumer ID"""
        return self._id

    def get_account_number(self):
        """Get the account number"""
        return self.__account_number

    def set_account_number(self, account_number):
        """Set the account number"""
        self.__account_number = account_number

    def get_name(self):
        """Get the costumer name and return it"""
        return self.__name

    def set_name(self, name):
        """Set the costumer name"""
        self.__name = name

    def get_account_type(self):
        """Return the account Type"""
        return self.account_type

    def set_account_type(self, account_type):
        """Set the account Type: Saving or Checking"""
        self.account_type = account_type

    def get_balance(self):
        """Return the current balance"""
        return self.balance

    def set_balance(self, balance):
        """Set the balance"""
        self.balance = balance

    def create_account(self):
        """Method used tp create new costumers,
        checks for the correct input if not re-prompt again"""
        while True:
            try:
                costumer_id = int(input('Please enter Costumer ID: '))
                if costumer_id < 0 or not costumer_id.is_integer():
                    print("Please enter a positive integer!")
                    continue
                else:
                    self.set_id(costumer_id)
                    break
            except ValueError:
                print('Please enter an integer!')
                continue
        while True:
            name = str(input('Please enter full name: '))
            if not name.isalpha():
                print("Please enter a string!")
                continue
            else:
                self.set_name(name)
                break
        while True:
            try:
                account_number = int(input('Please enter account number: '))
                if account_number < 0 or not account_number.is_integer():
                    print("Please enter a positive integer!")
                    continue
                else:
                    self.set_account_number(account_number)
                    break
            except ValueError:
                print('Please enter an integer!')
                continue
        while True:
            account_type = str(input('Please enter account type: '))
            if not account_type.isalpha():
                print("Please enter a string!")
                continue
            else:
                self.set_account_type(account_type)
                break
        while True:
            try:
                balance = float(input('Please enter starting balance: '))
                if balance < 0 or not balance.is_integer():
                    print("Please enter a positive number!")
                    continue
                else:
                    self.set_balance(balance)
                    break
            except ValueError:
                print('Please enter a number!')
                continue

    def __str__(self):
        return (f"'Costumer ID': {self.get_id()}, ' Full Name': {self.get_name()},"
                f"' Account Number': {self.get_account_number()},"
                f"' Account Type': {self.get_account_type()}, ' Balance':{self.get_balance()}")

    # Magic method
    def __eq__(self, get):
        return self.balance == get.get_balance()


costumers = Costumer('', '', '', '', '')
if __name__ == "__main__":
    # We are expecting int in the get ID
    assert (costumers.set_id(int) != ''), "Error: did not work as expected"
    # We are expecting float in the get Balance
    assert (costumers.set_balance(int) != ''), "Error: did not work as expected"

    print('Getting correct input in ID and balance unit test successful!')
