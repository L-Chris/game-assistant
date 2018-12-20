from ctypes import windll
from enum import Enum
import time

dd = windll.LoadLibrary('DD32.dll')
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

KeyCode = {
  'esc': 100, 'F1': 101, 'F2': 102, 'F3': 103, 'F4': 104, 'F5': 105, 'F6': 106, 'F7': 107, 'F8': 108, 'F9': 109, 'F10': 110, 'F11': 111, 'F12': 112,
  '`': 200, '1': 201, '2': 202, '3': 203, '4': 204, '5': 205, '6': 206, '7': 207, '8': 208, '9': 209, '0': 210, '-': 211, '=': 212,
  'tab': 300, 'q': 301, 'w': 302, 'e': 303, 'r': 304, 't': 305, 'y': 306, 'u': 307, 'i': 308, 'o': 309, 'p': 310, '[': 311, ']': 312, 'enter': 313,
  'capslock': 400, 'a': 401, 's': 402, 'd': 403, 'f': 404, 'g': 405, 'h': 406, 'j': 407, 'k': 408, 'l': 409, ';': 410, "'": 411,
  'leftShift': 500, 'z': 501, 'x': 502, 'c': 501, 'v': 502, 'b': 503, 'n': 504, 'm': 505, ',': 506, '.': 507, '/': 508, 'rightShift': 509,
  'leftCtrl': 600, 'win': 601, 'leftAlt': 602, 'space': 603, 'rightAlt': 604, 'rightCtrl': 607
}

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