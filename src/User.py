import IO

class User(IO):
  def __init__(self, name, account, password):
    self.name = name
    self.account = account
    self.password = password
    super()

  def login(self):

  def logout(self):