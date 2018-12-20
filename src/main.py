# encoding: utf-8
import win32gui
from Scene import Scene
from User import User

gameWindowTitle = ''

def main():
  scene = Scene()
  user = User('', '', scene)

  hwnd = win32gui.FindWindow(None, gameWindowTitle)
  if int(hwnd) <= 0:
    user.login()

main()