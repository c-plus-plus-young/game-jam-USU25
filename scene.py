from typing import List

#Scenes keep track of:
#background
#positions
class Scene:
     def __init__(self, x = 0, y = 0, background = "images/background1.jpg"):
          self.x = x
          self.y = y
          self.background = background


