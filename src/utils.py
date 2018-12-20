import win32gui
import time
from PIL import ImageGrab
import cv2
import aircv

def winWait(title):
  hwnd = win32gui.FindWindow(None, title)
  while int(hwnd) <= 0:
    time.sleep(1)
    hwnd = win32gui.FindWindow(None, title)
  return hwnd

def widgetWait(parent, dest):
  imgSrc = winShot(parent)
  imgDst = aircv.imread(dest)
  pos = None
  while not pos or pos['result'] < 0.95:
    imgSrc = winShot(parent)
    pos = aircv.find_template(imgSrc, imgDst)
    time.sleep(2)

  left = pos['rectangle'][0][0]
  top = pos['rectangle'][0][1]
  return left, top

def winShot(win):
  left, top, right, bottom = win32gui.GetWindowRect(win)
  img = ImageGrab.grab((left, top, right, bottom))
  img.save('win.png')
  return aircv.imread('win.png')