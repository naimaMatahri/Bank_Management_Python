"""
Naima Matahri
Class: CS 521 - Spring 1
Date: 02/27/2024
Final Project
This program simulates a bank management system.
It prompts the user for Costumer ID, Full name,
Account Number, Account type(Saving or Checking Account)
and starting balance.
Saves the information to a text file.
Allows the user to get the data back to make a deposit, withdraw
or delete an account.
"""
import sys

from costumer import Costumer

costumer = Costumer('', '', '', '', '')


def create_customer_account():
    """Call the create account method from Costumer class
    and sets a new costumer and saves it to the text file."""
    costumer.create_account()
    save_created_account_to_file()


def save_created_account_to_file():
    """writes and saves the created costumer to the text file
    and displays in the console """
    try:
        with open('file.txt', 'a') as file:
            file.write((f"{costumer.get_id()},{costumer.get_name()},{costumer.get_account_number()},"
                        f"{costumer.get_account_type()},{costumer.get_balance()}"
                        .replace("}", " ").replace(' " ', '  ')))

            file.write('\n')
            file.close()
    except OSError:
        print('File name does not exist, please try again!')
        sys.exit()
    # Prin the new created Costumer
    print('New Costumer Created: ', [
        'Costumer ID: ', costumer.get_id(), 'Costumer Name:', costumer.get_name(), 'Account Number: ',
        costumer.get_account_number(), 'Account Type: ', costumer.get_account_type(),
        'Balance: ', '$', costumer.get_balance()])


def check_balance():
    """Reads from the file a specific account
    and checks for the current balance.
    Checks if the account exists and if the file exists."""
    try:
        with open('file.txt', 'r') as file:
            lines = file.readlines()
            file.close()
            # Checks is Account exists
            account_found = False
            costumer_account_number = input('Please enter the Account number you want to check: ')
            for line in lines:
                split_line = line.split(",")
                if len(line) > 0:
                    if costumer_account_number in split_line[2]:
                        print('Your Current Balance is = ', split_line[4])
                        print('Costumer Information', line)
                        account_found = True
            if not account_found:
                print("No existing record with this number\n")
    except OSError:
        print('File name does not exist, please try again!')
        sys.exit()


def deposit():
    """reads the file gets a specific account, gets the current balance
    and allows for deposit. We get back the new balance and
    displays the new data in the console."""
    try:
        with open('file.txt', 'r') as file:
            lines = file.readlines()
            file.close()
            account_found = False
            costumer_account_number = input('Please enter the Account number you want to deposit to: ')
            for line in lines:
                split_line = line.split(",")
                if len(line) > 0:
                    if costumer_account_number in split_line[2]:
                        amount_deposit = float(input('Please enter amount to deposit: '))
                        print('Balance before deposit: ', line)
                        number = float(split_line[4])
                        number += amount_deposit
                        split_line[4] = str(number)
                        print('Your new balance; ', number)
                        print('Account with new balance: ', split_line)
                        account_found = True
            if not account_found:
                print("No existing record with this number\n")
    except OSError:
        print('File name does not exist, please try again!')
        sys.exit()


def withdraw():
    """reads the file gets a specific account, gets the current balance
        and allows for withdrawal.If balance is less than withdrawal
        display a message. We get back the new balance and
        displays the new data in the console."""
    try:
        with open('file.txt', 'r') as file:
            lines = file.readlines()
            account_found = False
            costumer_account_number = input('Please enter the Account number you want to withdraw from: ')
            for line in lines:
                split_line = line.split(",")
                if len(line) > 0:
                    if costumer_account_number in split_line[2]:
                        amount_withdraw = float(input('Please enter amount to withdraw: '))
                        print('Account before withdraw: ', line)
                        number = float(split_line[4])
                        if amount_withdraw < number:
                            number -= amount_withdraw
                            split_line[4] = str(number)
                            print('Your new balance; ', number)
                            print('Account with new balance: ', split_line)
                            account_found = True
                        else:
                            print("You cannot withdraw larger amount")

            if not account_found:
                print("No existing record with this number\n")
    except OSError:
        print('File name does not exist, please try again!')
        sys.exit()


def delete_account():
    """Allows to delete a specific account based on the account number"""
    try:
        with open('file.txt', 'r') as file_read:
            lines = file_read.readlines()
            file_read.close()
            costumer_account_number = input('Please enter the Account number you want to delete: ')
            # pointer for position
            pointer = 1
            # opening in writing mode
            with open('file.txt', 'w') as file_write:
                for line in lines:
                    split_line = line.split(",")
                    if costumer_account_number != split_line[2]:
                        file_write.write(line)
                        pointer += 1
                        print('Account was deleted!')
                file_write.close()
    except OSError:
        print('File name does not exist, please try again!')
        sys.exit()


def menu():
    """Menu to display the choices the user can make or exit if done"""
    choice = ''
    while choice != 6:
        print("\tMAIN MENU")
        print("\t1. Create New Account")
        print("\t2. Check Balance")
        print("\t3. Deposit Amount")
        print("\t4. Withdraw Amount")
        print("\t5. Delete an Account")
        print("\t6. EXIT")
        choice = input("\tPlease select an option: ")
        if choice == '1':
            create_customer_account()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            deposit()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            delete_account()
        elif choice == '6':
            print("\tThank you for using our system!")
            break
        else:
            print("Invalid choice")


def main():
    """Calls main to run the program"""
    menu()


if __name__ == "__main__":
    main()
