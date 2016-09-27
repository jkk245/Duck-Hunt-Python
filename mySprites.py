#Video Game Summative
#ICS3U1-22
#By Joseph Yim 
#Ms. Tajalli 
#May 30/2014


import pygame, random
#datetime



class Crosshair(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Crosshair.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0,0,0)) 
        self.rect = self.image.get_rect()
        

    def set_crosshairPic(self,gun_type):

        if gun_type == "Pistol":
            self.image = pygame.image.load("Crosshair1.png")
            self.image = self.image.convert()
            self.image.set_colorkey((0,0,0)) 
            self.rect = self.image.get_rect()
        elif gun_type == "Shotgun":
            self.image = pygame.image.load("Crosshair2.png")
            self.image = self.image.convert()
            self.image.set_colorkey((0,0,0)) 
            self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-47,-47)

    def collide(self,other_sprite):
        collisions = pygame.sprite.spritecollide(self.rect,other_sprite,False)
        if collisions == True:
             for collision in mycollisions:
                if collision != self.rect:
                    return True
             return False
            

    def get_currentXpos(self):
        return self.rect.centerx

    def get_center_pos(self):
        return self.rect.center


    def update(self):
        self.rect.center = pygame.mouse.get_pos()





class BluDuck(pygame.sprite.Sprite):

    def __init__(self):
          
          pygame.sprite.Sprite.__init__(self)

          self.__random_choice = random.randint(0,2)

          

          self.images = [pygame.image.load("BluDuck" + str(self.__random_choice*3 + 1) + ".png"),\
                         pygame.image.load("BluDuck" + str(self.__random_choice*3 + 2) + ".png"),\
                         pygame.image.load("BluDuck" + str(self.__random_choice*3 + 3) + ".png")]
                             
          self.death_images = [pygame.image.load("BluDuckDeath.png"),\
                               pygame.image.load("BluDuckDeathFall.png")]


          self.__index = 0
          
          self.image = self.images[self.__index]
          self.rect = self.image.get_rect()
          self.image.set_colorkey((0,0,0))


          self.__dx = 1
          self.__dy = 1

          if self.__random_choice == 0:

              self.__screen_side1 = random.randint(1,2)
              
              if self.__screen_side1 == 1:
                  self.rect.left = -30
                  self.rect.centery = random.randint(20,200)

              elif self.__screen_side1 == 2:
                  pygame.transform.flip(self.image,True,False)
                  self.rect.centerx = 690
                  self.rect.centery = random.randint(20,200)

          elif self.__random_choice == 1:

              self.__screen_side2 = random.randint(1,2)

              if self.__screen_side2 == 1:
                  self.rect.centerx = random.randint(0,280)
                  self.rect.centery = 340

              elif self.__screen_side2 == 2:
                  pygame.transform.flip(self.image,True,False)
                  self.rect.centerx = random.randint(320,640)
                  self.rect.centery = 340

          elif self.__random_choice == 2:

               self.rect.centerx = random.randint(20,620)
               self.rect.centery = 340


    def death(self,isDead):
        if isDead == True:
            self.__dx = 0
            self.__dy = -8
            self.rect.centery -= self.__dy
        else:
            self.__dx = 1
            self.__dy = 1
            

    def death_animate(self,index):
        if index > 1:
            index = 0
        self.image = self.death_images[index]
              

    def update(self):


        self.__index += 0.25
            
        if self.__index == 0 or self.__index == 1 or self.__index == 2:
            self.image = self.images[int(self.__index)]

        if self.__index >= len(self.images):
            self.__index = 0



        if self.__random_choice == 0 and self.__screen_side1 == 1:
            self.rect.left += self.__dx
        elif self.__random_choice == 0 and self.__screen_side1 == 2:
            self.rect.left -= self.__dx 
        elif self.__random_choice == 1 and self.__screen_side2 == 1:
            self.rect.centerx += self.__dx
            self.rect.centery -= self.__dy
        elif self.__random_choice == 1 and self.__screen_side2 == 2:
            self.rect.centerx -= self.__dx
            self.rect.centery -= self.__dy
        elif self.__random_choice == 2:
            self.rect.centery -= self.__dy

        


        

class Grass(pygame.sprite.Sprite):

     def __init__(self,x_pos,y_pos):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Grass.png")
        self.image = self.image.convert()
        self.image.set_colorkey((0,0,0)) 
        self.rect = self.image.get_rect()

        self.rect.centerx = x_pos
        self.rect.bottom = y_pos

       
            

class Pistol(pygame.sprite.Sprite):

     def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)

        self.images1 = [pygame.image.load("./Pistol/Pistol1.png"),\
                        pygame.image.load("./Pistol/Pistol2.png"),\
                        pygame.image.load("./Pistol/Pistol3.png"),\
                        pygame.image.load("./Pistol/Pistol4.png"),\
                        pygame.image.load("./Pistol/Pistol5.png"),\
                        pygame.image.load("./Pistol/Pistol6.png")]
                        
        
        self.images2 = [pygame.image.load("./Pistol/Pistol_reload1.png"),\
                        pygame.image.load("./Pistol/Pistol_reload2.png"),\
                        pygame.image.load("./Pistol/Pistol_reload3.png"),\
                        pygame.image.load("./Pistol/Pistol_reload4.png"),\
                        pygame.image.load("./Pistol/Pistol_reload5.png"),\
                        pygame.image.load("./Pistol/Pistol_reload6.png"),\
                        pygame.image.load("./Pistol/Pistol_reload7.png"),\
                        pygame.image.load("./Pistol/Pistol1.png")]
        
                                  
        
        self.image = self.images1[0]
                           
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))

        self.rect.bottom = 480
        self.rect.centerx = 320

  
     def fire_animate(self,index):
        self.image = self.images1[index]

            
     def reload_animate(self,index):
        self.image = self.images2[index]


     def update(self,x_pos):

        self.rect.centerx= x_pos
        self.rect.bottom = 480


class Shotgun(pygame.sprite.Sprite):

    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)

        self.images1 = [pygame.image.load("./Shotgun/Shotgun1.png"),\
                        pygame.image.load("./Shotgun/Shotgun2.png"),\
                        pygame.image.load("./Shotgun/Shotgun3.png"),\
                        pygame.image.load("./Shotgun/Shotgun4.png"),\
                        pygame.image.load("./Shotgun/Shotgun5.png")]

        self.images2 = [pygame.image.load("./Shotgun/Shotgun6.png"),\
                        pygame.image.load("./Shotgun/Shotgun7.png"),\
                        pygame.image.load("./Shotgun/Shotgun8.png"),\
                        pygame.image.load("./Shotgun/Shotgun9.png"),\
                        pygame.image.load("./Shotgun/Shotgun10.png"),\
                        pygame.image.load("./Shotgun/Shotgun11.png"),\
                        pygame.image.load("./Shotgun/Shotgun12.png"),\
                        pygame.image.load("./Shotgun/Shotgun13.png"),\
                        pygame.image.load("./Shotgun/Shotgun14.png"),\
                        pygame.image.load("./Shotgun/Shotgun15.png"),\
                        pygame.image.load("./Shotgun/Shotgun16.png"),\
                        pygame.image.load("./Shotgun/Shotgun17.png"),\
                        pygame.image.load("./Shotgun/Shotgun18.png"),\
                        pygame.image.load("./Shotgun/Shotgun19.png"),\
                        pygame.image.load("./Shotgun/Shotgun20.png"),\
                        pygame.image.load("./Shotgun/Shotgun21.png"),\
                        pygame.image.load("./Shotgun/Shotgun22.png"),\
                        pygame.image.load("./Shotgun/Shotgun23.png"),\
                        pygame.image.load("./Shotgun/Shotgun24.png"),\
                        pygame.image.load("./Shotgun/Shotgun25.png"),\
                        pygame.image.load("./Shotgun/Shotgun26.png"),\
                        pygame.image.load("./Shotgun/Shotgun27.png"),\
                        pygame.image.load("./Shotgun/Shotgun28.png"),\
                        pygame.image.load("./Shotgun/Shotgun29.png"),\
                        pygame.image.load("./Shotgun/Shotgun1.png")]

        self.image = self.images1[0]
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.rect.bottom = 480
        self.rect.centerx = 320

    def fire_animate(self,index):
        self.image = self.images1[index]

    def reload_animate(self,index):
        self.image = self.images2[index]

    def update(self,x_pos):

        self.rect.centerx = x_pos
        self.rect.bottom = 480


'''
class Revolver(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


    self.images1 = [pygame.image.load("./Revolver/
'''   

    



    



class AmmoKeeper(pygame.sprite.Sprite): 

    def __init__(self,gun_type,ammoInGun,totalAmmoCount):
        
        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.Font("8-bit.ttf", 30)
        self.__gun = gun_type
        self.__currentAmmo = ammoInGun
        self.__totalAmmo = totalAmmoCount
        


    def set_totalAmmo(self,total_ammo):
        self.__totalAmmo = total_ammo

    def set_currentAmmo(self,current_ammo):
        self.__currentAmmo = current_ammo

    def get_currentAmmo(self):
        return self.__currentAmmo

    def get_totalAmmo(self):
        return self.__totalAmmo
        
        
    def ammoFired(self):
        self.__currentAmmo -= 1

 
    def update(self,x_pos,y_pos):

        self.__message = self.__gun + ": " + str(self.__currentAmmo) + "/" + str(self.__totalAmmo)
        self.image = self.__font.render(self.__message, 1, (250,250,10)) 
        self.rect = self.image.get_rect() 
        self.rect.center = (x_pos,y_pos)
        


class ScoreKeeper(pygame.sprite.Sprite):

    def __init__(self,score):

        pygame.sprite.Sprite.__init__(self)
        self.__font = pygame.font.Font("8-bit.ttf", 25)
        self.__playerScore = score
        self.__playerLives = 3

    def set_playerScore(self,currentScore):
        self.__playerScore = currentScore

    def playerDied(self):
        self.__playerLives -= 1

    def game_over(self):
        if self.__playerLives == 0:
            return True

    def update(self):

        self.__message = "Lives Remaining: " + str(self.__playerLives) + " "*5 + "Score: " + str(self.__playerScore)
        self.image = self.__font.render(self.__message,1,(250,250,10))
        self.rect = self.image.get_rect()
        self.rect.center = (320,22) 

    



class Upgrade(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.pistol = pygame.image.load("./Upgrades/pistol_upg.png")
        self.shotgun = pygame.image.load("./Upgrades/shotty_upg.png")
        self.minigun = pygame.image.load("./Upgrades/minigun_upg.png")
        self.revolver = pygame.image.load("./Upgrades/revolver_upg.png")
        self.ammobox = pygame.image.load("./Upgrades/ammobox.png")

        self.__dy = 3

        choice = random.randint(1,1000)

        if choice >= 1 and choice <= 500:
            self.image = self.ammobox
        elif choice >= 500 and choice <= 800:
            self.image = self.pistol
        elif choice >= 1 and choice <= 250:
            self.image = self.shotgun
        elif choice >= 800 and choice <= 1000:
            self.image = self.revolver
        elif choice == 1000:
            self.image = self.minigun

        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(20,620)
        self.rect.centery = -20



    def update(self):

        self.rect.bottom += self.__dy
        
        


class Dog(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load("./Dog/Dog1.png"),\
                       pygame.image.load("./Dog/Dog2.png"),\
                       pygame.image.load("./Dog/Dog3.png"),\
                       pygame.image.load("./Dog/Dog4.png"),\
                       pygame.image.load("./Dog/Dog5.png")]

        self.__index = 0

        self.image = self.images[self.__index]
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0))

        self.rect.centerx = -30
        self.rect.bottom = 620

    def animate(self):
        pass


    def update(self):
        pass
        
        
                       


    

        
        
'''
class Upgrade(pygame.sprite.Sprite):
'''







    




        
        
