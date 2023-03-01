"""Test Bank"""
from module.bank import BankAccount
from hamcrest import assert_that, equal_to


"""Test that 
When I create an account
And I dont deposit it with any money
Then I will have a bank account that is empty"""

def test_create_bank_account():
    
    bank_acc = BankAccount()

    assert_that(bank_acc.ammount, equal_to(0))
