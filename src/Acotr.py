from enum import Enum
import time
from IO import IO

class ActorState(Enum):
  idle = 1
  walk = 2
  run = 3
  attack = 4
  underAttack = 5
  dead = 6

class Direction(Enum):
  forward = 1
  backward = 2
  left = 3
  right = 4

class Actor(IO):
  def __init__(self):
    self.state = ActorState.idle
    super()

  def searchEnemy(self):
    print 'searchEnemy'

  def attack(self):
    self.state = ActorState.attack

  def run(self):
    print 'run'

  def walk(self):
    print 'walk'

  def jump(self):
    print 'jump'

  def checkSTA(self):
    return True