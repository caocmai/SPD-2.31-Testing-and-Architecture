# by Kami Bigdely
# Extract superclass.

class Location:
    
    def __init__(self, x, y, visible=True):
        self.x = x
        self.y = y
        self.visible = visible

    def display(self, message):
        if self.visible:
            print(message)


class Circle(Location):
    
    def __init__(self, x, y, r, visible=True):
      super(Circle, self).__init__(x, y, visible)
    #   self.center_x = x
    #   self.center_y = y
      self.r = r
      self.visible = visible
      
    def display(self):
        message = "drew the circle"
        super(Circle, self).display(message)
        # print('drew the circle.')
        
    def set_visible(self,is_visible):
        self.visible = is_visible
        
    def get_center(self):
        return self.x, self.y
    
    
class Rectangle(Location):
    
    def __init__(self, x, y, width, height, visible=True):
        super(Rectangle, self).__init__(x, y, )
        # Location.__init__(self, x, y)
        # left-bottom corner.
        # self.x = x
        # self.y = y
        self.width = width
        self.height = height
        # self.visible = visible
        
        
    def display(self):
        message = 'drew the rectable.'
        super(Rectangle, self).display(message)
            
    def hide(self):
        self.visible = False
        
    def make_visible(self):
        self.visible = True
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())