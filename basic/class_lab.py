class BankAccount():
  def __init__(self, accountType = 'checking', balance = 0):
    self.accountType = accountType
    self.balance = balance
    self.overDraftFee = 0

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposit: ${amount} ")
    print(f"Balance: ${self.balance} ")
  
  def withdrawl(self, amount):
    self.balance -= amount
    print(f'Withdrawl: ${amount}')
    print(f'Balance: ${self.balance} ')
    if (self.balance < 0):
      self.overDraftFee += 20
      print(f'Over Draft Fee: ${self.overDraftFee} ')
      

class ChildBankAccount(BankAccount):
  def __init__(self, balance=0):
    super().__init__(accountType='Child Account')
  
  def withdrawl(self, amount):
    if (amount > self.balance):
      print(f"You have only ${self.balance}. ")
      print(f'Withdrawl: ${self.balance}')
      print(f'Balance: $0 ')
      self.balance = 0
    else:
      return super().withdrawl(amount)


andreaAccount = ChildBankAccount()
andreaAccount.deposit(20)
andreaAccount.withdrawl(18)
andreaAccount.withdrawl(5)