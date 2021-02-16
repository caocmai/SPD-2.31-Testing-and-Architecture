# By Kamran Bigdely Nov. 2020
# Move Field (attribute)
class Gun:
    def __init__(self, name, bullets):
        self.name = name  
        self.bullets = bullets      
    def shoot(self):
        print('shoot')
        if self.bullets > 0:
            self.bullets -= 1
        else:
            return "None bullets left"
    def reload(self):
        print('reload')

class Player:
    def __init__(self, guns):        
        self.guns = guns
        # self.num_cathridge_bullets = [] # corresponding list that holds number of bullets for 
                                        # each gun in the 'self.guns'
        # for _ in range(len(guns)):
        #     # initialize with 10 bullets in each gun's cathridge.
        #     self.num_cathridge_bullets.append(10) 
    def fire_once(self):
        for gun in guns:
            print(gun.name)
            gun.shoot()
        # for i, gun in enumerate(self.guns):
        #     if self.num_cathridge_bullets[i] > 0:
        #         gun.shoot()
        #         self.num_cathridge_bullets[i] -= 1
        #         break
            
def game_loop():
    while (True):
        player.fire_once()
        # other logic here.
        break

guns = [Gun('pistol', 10), Gun('rifle', 20)]
player = Player(guns)
game_loop()
