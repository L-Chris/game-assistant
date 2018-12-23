from IO import IO

class Widget(IO):
  def __init__(self, left, top, right = 0, bottom = 0):
    self.left = left
    self.top = top
    self.right = right
    self.bottom = bottom

  def click(self, x, y, count = 2):
    self.mouseMove((self.left + x) / 2, self.top + y)
    self.mouseClick('left', count)