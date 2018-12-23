from IO import IO
from Window import Window

class User(IO):
  def __init__(self, account, password, scene):
    self.account = account
    self.password = password
    self.scene = scene

  def login(self):
    if not Window.exist(''):
      Window.start(url)
    self.sendString(self.account)
    self.sendString(self.password)

  def run(self):
    print 'run'