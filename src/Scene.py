import threading
import time
from enum import Enum
from Window import Window

class SceneType(Enum):
  instance = 1

class Scene(Window):
  def __init(self, title, images):
    self.title = title
    self.type = SceneType.instance
    self.images = images

  def get(self):
    for img in self.images:
      if self.findWidget(img.url):
        self.type = img.type
        break

  def task(self):
    while True:
      self.get()
      time.sleep(1)

  def run(self):
    threading.Thread(target=self.task)