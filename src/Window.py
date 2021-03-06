from PIL import ImageGrab
import win32api, win32gui, win32con
from IO import IO
from Widget import Widget
import cv2
import aircv
import time

class Window(IO):
  def __init__(self, title):
    self.title = title
    if (title):
      self.hwnd = self.wait(title)
      self.update()

  @staticmethod
  def exist(title):
    win = win32gui.FindWindow(None, title)
    return int(win) > 0

  @staticmethod
  def start(url):
    win32api.ShellExecute(0, 'open', url, '', '', 1)

  def activate(self):
    win32gui.SetActiveWindow(self.hwnd)

  def wait(self, title):
    hwnd = win32gui.FindWindow(None, title)
    while int(hwnd) <= 0:
      time.sleep(0.2)
      hwnd = win32gui.FindWindow(None, title)

    return hwnd

  def waitWidget(self, dst):
    img = aircv.imread(dst)
    pos = None
    while not pos or pos['result'] < 0.95:
      src = self.shot()
      pos = aircv.find_template(src, img)
      time.sleep(0.2)

    left = pos['rectangle'][0][0]
    top = pos['rectangle'][0][1]
    return Widget(left, top)

  def existWidget(self, dst):
    src = self.shot()
    img = aircv.imread(dst)
    pos = aircv.find_template(src, img)
    return pos and pos['result'] > 0.95

  def position(self):
    left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
    return left, top, right, bottom

  def shot(self, dst = 'win.png'):
    img = ImageGrab.grab(bbox = (self.left, self.top, self.right, self.bottom))
    img.save(dst)
    return aircv.imread(dst)

  def click(self, x, y, count = 2):
    self.mouseMove(self.left + x, self.top + y)
    self.mouseClick('left', count)

  def update(self):
    left, top, right, bottom = self.position()
    self.left = left
    self.top = top
    self.right = right
    self.bottom = bottom

  def close(self):
    win32gui.PostMessage(self.hwnd, win32con.WM_CLOSE, 0, 0)