from enum import Enum

class SceneType(Enum):
  instance = 1

class Scene:
  def __init(self):
    self.type = SceneType.instance