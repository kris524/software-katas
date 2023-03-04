"""Test Bank"""
from hamcrest import assert_that, equal_to
from module.bank import BankAccount

#Red
"""Test that 
When I create an account
And I dont deposit it with any money
Then I will have a bank account that is empty"""

def test_create_bank_account():
    
    bank_acc = BankAccount()

    assert_that(bank_acc.ammount, equal_to(0))

"""Test that 
When I deposit some money into the account
Then the new ammount will be as expected"""
def test_deposit_to_bank_account():
    empty_b_a = BankAccount()
    empty_b_a.deposit(100)
    assert_that(empty_b_a.ammount, equal_to(100))

"""Test that
When I deposit muliple times to the same account 
Then I will get the expected value"""
def test_multiple_deposits():
    empty_b_a = BankAccount()
    empty_b_a.deposit(100)
    empty_b_a.deposit(200)

    assert_that(empty_b_a.ammount, equal_to(300))

"""Test that
When I deposit into seperate BA
Then I will get the expected ammounts"""


"""Test that
When I deposit money into the account
There is a timestamp attached to the transaction"""
