from typing import List



class Entity:
     def setX(self, x):
          pass
     def setY(self, y):
          pass
     def getX(self):
          pass
     def getY(self):
          pass
     def getWidth():
          pass
     def getHeight():
          pass

class PlayerPos(Entity):
     def __init__(self, x = 100, y = 100, width = 50, height = 50):
          self.x = x
          self.y = y
          self.width = width
          self.height = height

     def setX(self, x):
          self.x = x
     def setY(self, y):
          self.y = y
     def getX(self):
          return self.x
     def getY(self):
          return self.y
     def getWidth(self):
          return self.width
     def getHeight(self):
          return self.height
     
class PersonPos(Entity):
     def __init__(self, x = 100, y = 100, width = 50, height = 50):
          self.x = x
          self.y = y
          self.width = width
          self.height = height

     def setX(self, x):
          self.x = x
     def setY(self, y):
          self.y = y
     def getX(self):
          return self.x
     def getY(self):
          return self.y
     def getWidth(self):
          return self.width
     def getHeight(self):
          return self.height

#Scenes keep track of:
#Entities
#background
#positions
class Scene:
     def __init__(self, background = "images/water.png", objects: List[Entity] = None):
          self.background = background
          self.objects = objects
