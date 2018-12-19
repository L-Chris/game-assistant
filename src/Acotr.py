from enum import Enum
import time

class ActorState(Enum):
  idle = 1
  walk = 2
  run = 3
  attack = 4
  underAttack = 5
  dead = 6

class Actor:
  def __init__(self):
    self.state = ActorState.idle
    print 'init'

  def searchEnemy(self):
    print 'searchEnemy'

  def attack(self):
    self.state = ActorState.attack
    print 'attck'

  # sta for run
  def checkSTA(self):
    return True