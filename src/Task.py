class Task:
  def __init__(self, fn, next):
    self.next = next
    self.fn = fn

  def run(self):
    self.fn()

  def success(self):
    print 'success'

  def failed(self):
    print 'failed'