# encoding: utf-8
import win32gui
from Window import Window
from Scene import Scene
from User import User

title = ''

def main():
  scene = Scene()
  user = User('', '', scene)

  win = Window(title)
  if int(win.hwnd) <= 0:
    user.login()

main()