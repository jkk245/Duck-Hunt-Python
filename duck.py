



class BluDuck(pygame.sprite.Sprite):

    def __init__(self):
          
          pygame.sprite.Sprite.__init__(self)

          random_choice = random.randint(0,2)

          

          self.images = [pygame.image.load("BluDuck" + random_choice*3 + 1 + ".png"),\
                         pygame.image.load("BluDuck" + random_choice*3 + 2 + ".png"),\
                         pygame.image.load("BluDuck" + random_choice*3 + 3 + ".png")]
                             
          self.death_images = [pygame.image.load("BluDuckDeath.png"),/
                               pygame.image.load("BluDuckDeathFall.png")]


          self.__index = 0
          
          self.image = self.images[self.__index]
          self.rect = self.image.get_rect()
          self.image.set_colorkey((0,0,0))


          self.__dx = 1
          self.__dy = 1

          if random_choice == 0:

              screen_side1 = random.randint(1,2)
              
              if screen_side1 == 1:
                  self.rect.left = -30
                  self.rect.centery = random.randint(20,200)

              elif screen_side2 == 2:
                  pygame.transform.flip(self.image,True,False)
                  self.rect.centerx = 690
                  self.rect.centery = random.randint(20,200)

           elif random_choice == 1:

              screen_side2 = random.randint(1,2)

              if screen_side2 = 1:
                  self.rect.centerx = random.randint(0,280)
                  self.rect.centery = 340

              elif screen_side2 == 2:
                  pygame.transform.flip(self.image,True,False)
                  self.rect.centerx = random.randint(320,640)
                  self.rect.centery = 340

           elif random_choice == 2:

               self.rect.centerx = random.randint(20,620)
               self.rect.centery = 340


    def death(self,isDead):
        if isDead == True:
            self.__dx = 0
            self.__dy = -8
        else:
            self.__dx = 1
            self.__dy = 1

    def death_animate(self,index):
        self.image = self.death_images[index]
              

    def update(self):


        self.__index += 0.25
            
        if self.__index == 0 or self.__index == 1 or self.__index == 2:
            self.image self.images[int(self.__index)]

        if self.__index >= len(self.images):
            self.__index = 0



        if random_choice == 0 and screenside1 == 1:
            self.rect.left += self.__dx
        elif random_choice == 0 and screenside1 == 2:
            self.rect.left -= self.__dx 
        elif random_choice == 1 and screenside2 == 1:
            self.rect.centerx += self.__dx
            self.rect.centery -= self.__dy
        elif random_choice == 1 and screenside2 == 2:
            self.rect.centerx -= self.__dx
            self.rect.centery -= self.__dy
        elif random_choice == 2:
            self.rect.centery -= self.__dy
            
            
            
            
            


        
          

          
              





         















              
              
              
              
              


          

    
