from IO import IO

class User(IO):
  def __init__(self, account, password):
    self.account = account
    self.password = password
    super()

  def login(self):
    self.sendString(self.account)
    self.sendString(self.password)
    self.sendKey('enter')