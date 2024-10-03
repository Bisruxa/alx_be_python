class BankAccount:
  def __init__(self,initial_balance=0):
   self.account_balance = initial_balance
   
  def deposit(self,amount):
   if amount >0 :
     self.account_balance +=amount
    #  print(f"Deposited: ${amount}")
   else:
     print("deposite amount must be positive")

   
  def withdraw(self,amount):
    if amount>0 and amount <= self.account_balance:
     self.account_balance -= amount
    #  print(f"Withdrew: ${amount}")
     return True
    elif amount > self.account_balance:
    #  print("Insufficient funds")
     return False
    else:
      print("amount must be positive")
      return False
  def display_balance(self):
    float(self.account_balance)
    print(f"Current Balance: ${self.account_balance}")