import random

class BankAccount:
    def __init__(self, owner, balance, account_no=None, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = account_no if account_no else random.randint(11111, 99999)
        self.has_overdraft = has_overdraft

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.has_overdraft and self.balance < amount:
            return "You are not allowed to withdraw."
        elif self.has_overdraft or self.balance >= amount:
            self.balance -= amount
            return self.balance

    def __str__(self):
        return f"Account {self.account_no} - Owner: {self.owner} - Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, account_no=None):
        # 使用父类的构造函数
        super().__init__(owner, balance, account_no)
        
    def withdraw(self, amount=None):
        # 覆盖父类的 withdraw 方法
        return "No withdrawals permitted"

# 示例：

# 创建一个普通银行账户
bank_account = BankAccount(owner="Alice", balance=1000)
print(bank_account)  # Account 会显示账户信息

# 存款操作
print(bank_account.deposit(500))  # 1500

# 取款操作
print(bank_account.withdraw(200))  # 1300

# 创建一个储蓄账户
savings_account = SavingsAccount(owner="Bob", balance=2000)
print(savings_account)  # Account 会显示账户信息

# 储蓄账户尝试取款
print(savings_account.withdraw(100))  # No withdrawals permitted



# 代码解释：
# BankAccount 类：
# __init__: 初始化账户的所有基本信息，包括账户的所有者 (owner)、余额 (balance)、账户号码 (account_no) 和是否有透支 (has_overdraft)。
# deposit: 存款方法，增加账户余额并返回新的余额。
# withdraw: 取款方法，如果账户余额足够且没有透支限制，则减少余额；否则返回拒绝信息。
# __str__: 用来生成银行账户的字符串表示，输出账户号码、所有者和余额。
# SavingsAccount 类：
# 继承了 BankAccount 类，表示一个储蓄账户。
# __init__: 使用 super() 调用父类的初始化方法。
# withdraw: 重写了父类的 withdraw 方法，这个方法不接受参数，也不修改余额，直接返回 "No withdrawals permitted"，意味着储蓄账户不允许取款。
# 示例输出：
# python
# Copy code
# Account 35724 - Owner: Alice - Balance: 1000
# 1500
# 1300
# Account 89234 - Owner: Bob - Balance: 2000
# No withdrawals permitted
# 说明：
# 普通 BankAccount 账户可以正常存款和取款，withdraw 方法会根据余额和透支状态决定是否成功取款。
# SavingsAccount 账户覆盖了 withdraw 方法，所有取款操作都会返回 "No withdrawals permitted"，并且不会改变账户余额。
# 通过这种方式，你可以很方便地为不同类型的账户（如储蓄账户、支票账户等）定制不同的取款规则。