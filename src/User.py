from IO import IO

class User(IO):
  def __init__(self, account, password, scene):
    self.account = account
    self.password = password
    self.scene = scene

  def login(self):
    win32api.ShellExecute(0, 'open', url, '', '', 1)
    self.sendString(self.account)
    self.sendString(self.password)