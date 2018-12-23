# encoding: utf-8
import win32gui
from Window import Window
from User import User
from Actor import Actor

gameWindowTitle = 'Gundam Online'

def main():
  user = User('', '')
  actor = Actor()

  if not Window.exist(gameWindowTitle):
    user.login()

  user.run()
  actor.play()

main()