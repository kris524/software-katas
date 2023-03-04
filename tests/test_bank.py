"""Test Bank"""
from hamcrest import assert_that, equal_to
from module.bank import BankAccount

# Red
def test_create_bank_account():
    """Test that
    When I create an account
    And I dont deposit it with any money
    Then I will have a bank account that is empty"""

    bank_acc = BankAccount()

    assert_that(bank_acc.ammount, equal_to(0))


def test_deposit_to_bank_account():
    """Test that
    When I deposit some money into the account
    Then the new ammount will be as expected"""

    empty_b_a = BankAccount()
    empty_b_a.deposit(100)
    assert_that(empty_b_a.ammount, equal_to(100))


def test_multiple_deposits():
    """Test that
    When I deposit muliple times to the same account
    Then I will get the expected value"""

    empty_b_a = BankAccount()
    empty_b_a.deposit(100)
    empty_b_a.deposit(200)

    assert_that(empty_b_a.ammount, equal_to(300))


"""Test that
When I deposit into two seperate BA
Then I will get the expected ammounts for each account"""
def test_deposits_in_separate_acc():
    ba1 = BankAccount()
    ba1.deposit(100)
    ba2 = BankAccount()
    ba2.deposit(200)

    assert_that(ba2.ammount, equal_to(200))
    assert_that(ba1.ammount, equal_to(100))



"""Test that
When I deposit money into the account
There is a timestamp attached to the transaction"""
