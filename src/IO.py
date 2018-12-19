from ctypes import windll
from enum import Enum
import time

dd = windll.loadLibrary('DD64.dll')
KEY_DELAY = 0.1

class MouseButton(Enum):
  left = [1, 2]
  right = [4, 8]
  middle = [16, 32]
  x1 = [64, 128]
  x2 = [256, 512]

class MouseWheelDirection(Enum):
  forward = 1
  backward = 2

class KeyCode(Enum):
  a = 1
  b = 2

class IO:
  def __init__(self):
    self.dd = dd

  def mouseMove(self, x, y, relative = False):
    if relative:
      self.dd.DD_movR(x, y)
    else:
      self.dd.DD_mov(x, y)

  def mouseClick(self, type, count = 1):
    key = MouseButton[type]

    if not isinstance(count, int) or count <= 0:
      print('count must be a positive int!')
      return

    if not key:
      print(key + ' is not exists!')
      return

    for i in range(1, count):
      self.dd.DD_btn(key[0])
      time.sleep(KEY_DELAY)
      self.dd.DD_btn(key[1])
      time.sleep(KEY_DELAY)

  def mouseWheel(self, type, count = 1):
    key = MouseWheelDirection[type]

    if not key:
      print(key + ' is not exists!')
      return

    if not isinstance(count, int) or count <= 0:
      print('count must be a positive int!')
      return

    for i in range(1, count):
      self.dd.DD_whl(key)
      time.sleep(KEY_DELAY)

  def sendKey(self, type, count = 1):
    key = KeyCode[type]

    if not isinstance(count, int) or count <= 0:
      print('count must be a positive int!')
      return

    if not key:
      print(key + ' is not exists!')
      return

    for i in range(1, count):
      self.dd.DD_key(key, 1)
      time.sleep(KEY_DELAY)
      self.dd.DD_key(key, 2)
      time.sleep(KEY_DELAY)

  def sendString(self, str):
    dd.DD_str(str)