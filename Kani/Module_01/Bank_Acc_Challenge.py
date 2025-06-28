class BankAccount():
    acc_numbers = {
        1:1000,
        2:3000,
        3:7000,
        4:200,
        5:600,
        6:900,
        7:10000,
        8:65472,
        9:0,
        10:4700
    }
    def __init__(self,name,acc_no,amount,balance=0):
        self.name = name
        self.acc_no = acc_no
        self.amount = amount
        self.balance = balance
    
    def acc_verify(self):
        acc_no_array = [1,2,3,4,5,6,7,8,9,10]
        if self.acc_no not in acc_no_array:
            return False
        return True

    def display(self):
        if not self.acc_verify():
            return "Invalid user"
        else:
            actual_balace = BankAccount.acc_numbers[self.acc_no]
            return f"{self.amount} has been withdrawn successfully. New balance is Rs.{BankAccount.acc_numbers[self.acc_no]}"
    
    def withdraw(self):
        if not self.acc_verify():
            return "Invalid user"
        if self.amount > BankAccount.acc_numbers[self.acc_no]:
            return f"Insufficient balance. Enter amount <= Rs.{BankAccount.acc_numbers[self.acc_no]}"
        else:
            BankAccount.acc_numbers[self.acc_no] -= self.amount
            return f"{self.amount} has been withdrawn successfully. New balance is Rs.{BankAccount.acc_numbers[self.acc_no]}" 
    
    def check_balance(self):
        if not self.acc_verify():
            return "Invalid user"
        return f"Your current balance is {BankAccount.acc_numbers[self.acc_no]}"
    
    def deposit(self):
        if not self.acc_verify():
            return "Invalid user"
        if self.amount >= 50:
            BankAccount.acc_numbers[self.acc_no] += self.amount
            return f"Your money {self.amount} has been deposited successfully to Account number {self.acc_no}. New balance: {BankAccount.acc_numbers[self.acc_no]}"
        else:
            return f"Your request {self.amount} for deposit has been declined. Please deposit above 50"
        
    def admin_view_all_balances(self):
        print("All Account Balances:")
        for acc_no, balance in self.acc_numbers.items():
            print(f" * Account No: {acc_no}, Balance: Rs.{balance}")
            
    
    call_backs = {"display":display, "withdraw":withdraw, "check_balance":check_balance, "deposit":deposit}
    

call = BankAccount("Kanishkan",10,100)
# print(call.acc_verify())
print(call.display())
print(call.check_balance())
print(call.deposit())
print(call.withdraw())
call.admin_view_all_balances()