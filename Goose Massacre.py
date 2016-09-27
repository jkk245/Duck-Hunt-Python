#Goose Hunt Revamped Edition
#By Joseph Yim 
#May 30/2014

#IDEA

#IMPORT AND INTIALIZE
import pygame,mySprites,random
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.mixer.init()

def main():

    #DISPLAY
    pygame.display.set_caption("Goose Hunt Revamped Edition - Joseph Yim")

    #ENTITIES

    
    background = pygame.image.load("background.png")
    background = background.convert()
    screen.blit(background,(0,0))



    blue_ducks = []
    for numberOfBluDucks in range(10):
        duck1 = mySprites.BluDuck()
        blue_ducks.append(duck1)

    
    '''
    blue_ducks1 = []
    for numberOfBluDucks in range(2):
        duck1 = mySprites.BluDuck_Horizontal(random.randint(20,280))
        blue_ducks1.append(duck1)

    blue_ducks2 = []
    for numberOfBluDucks in range(3):
        duck2 = mySprites.BluDuck_Diagonal(random.randint(0,380))
        blue_ducks2.append(duck2)

    blue_ducks3 = []
    for numberOfBluDucks in range(3):
        duck3 = mySprites.BluDuck_Vertical(random.randint(10,630))
        blue_ducks3.append(duck3)
    '''
    cross_hair = mySprites.Crosshair()
    grass = mySprites.Grass(320,370)
    
    pistol = mySprites.Pistol()
    shotgun = mySprites.Shotgun()
    
    
    pistol_ammoKeeper = mySprites.AmmoKeeper("M1911",15,999)
    shotgun_ammoKeeper = mySprites.AmmoKeeper("Double-Barrel Shotgun",2,2)
    minigun_ammoKeeper = mySprites.AmmoKeeper("Minigun",2500,0)
    
    scoreKeeper = mySprites.ScoreKeeper(0)

    
   
    
    
    
    

    duckGroup = pygame.sprite.Group(blue_ducks)
    
    gun_type1 = pygame.sprite.Group(pistol)
    gun_type2 = pygame.sprite.Group(shotgun)
    
    ammo_type1 = pygame.sprite.Group(pistol_ammoKeeper)
    ammo_type2 = pygame.sprite.Group(shotgun_ammoKeeper)
    
    staticGroup = pygame.sprite.Group(grass)
    

    allSprites = pygame.sprite.Group(cross_hair,scoreKeeper)

  

   

    
    #ALTER

        
    #ASSIGN
    clock = pygame.time.Clock()
    playtime = 0.0
    milliseconds = clock.tick(30)
    playtime += milliseconds / 1000.0
    keepGoing = True

    

    ifPistol = False
    ifShotgun = True
    ifMinigun = False
    

    fire_gun = False
    reload_gun = False
    
    death_fall = False

    spawn = False
   
    
    count1 = 0
    count2 = 0
    count3 = 0
    death_count = 0
    inc_chance = 50
    score = 0

   


    
    #hide the mouse pointer
    pygame.mouse.set_visible(False)

    #LOOP
    while keepGoing:

        #TIME
        clock.tick(30)
        #pygame.set_timer(pygame.USEREVENT,1000)

        #EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                fire_gun = True
                if ifPistol == True:
                    if pistol_ammoKeeper.get_currentAmmo() <= 0:
                        fire_gun = False
                        reload_gun = True
                    else:
                        pistol_ammoKeeper.ammoFired()
                        

                if ifShotgun == True:
                    if shotgun_ammoKeeper.get_currentAmmo() <= 0:
                        fire_gun = False
                        reload_gun = True
                    else:
                        shotgun_ammoKeeper.ammoFired()
                    
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    reload_gun = True

            elif event.type == pygame.USEREVENT:
                possible_upgrade = mySprites.Upgrade()
                upgradeGroup = pygame.sprite.Group(possible_upgrade)
                


                    

        
        ducks_killed = []
        for duck in duckGroup:
            if duck.rect.collidepoint(pygame.mouse.get_pos()) and fire_gun == True:
                ducks_killed.append(duck)
                
                
                #duck_collisions = pygame.sprite.spritecollide(crosshair,duck,False)
                #for duck in duck_collisions: 
            
                
                #if death_count > 10:
                    #death_count = 0
                    #death_fall = True
                
                #if death_count == 0 or death_count == 20:
                    #duck.death_animate(int(death_count/10))
                                   
                #death_count += 10
                
        
            
            
        #for ducks in ducks_killed:
            #if pygame.sprite.spritecollide(ducks,grass,True) == False:
                #ducks.death_fall(True)
                
        
        
        
        if ifPistol == True:
 
            if fire_gun == True:
                
                count1 += 10
                if count1 > 50:
                    count1 = 0
                    fire_gun = False
                if count1 == 0 or count1 == 10 or count1 == 20 or count1 == 30 or\
                   count1 == 40 or count1 == 50:
                    pistol.fire_animate(int(count1/10))


            if reload_gun == True:
                if count2 == 0 or count2 == 10 or count2 == 20 or count2 == 30 or\
                   count2 == 40 or count2 == 50 or count2 == 60 or count2 == 70:
                    pistol.reload_animate(int(count2/10))
                    
                count2 += 5
                if count2 > 70:
                    count2 = 0
                    
                    pistol_ammoKeeper.set_totalAmmo(pistol_ammoKeeper.get_totalAmmo() -\
                                             (15 - pistol_ammoKeeper.get_currentAmmo()))
                    pistol_ammoKeeper.set_currentAmmo(15)
                    reload_gun = False
                    
                    
        elif ifShotgun == True:

            if fire_gun == True:

                count1 += 5
                if count1 > 40:
                    count1 = 0
                    fire_gun = False

                if count1 == 0 or count1 == 10 or count1 == 20 or count1 == 30 or\
                   count1 == 40:
                    shotgun.fire_animate(int(count1/10))

            if reload_gun == True: #24

                if count2 == 0 or count2 == 10 or count2 == 20 or count2 == 30 or\
                   count2 == 40 or count2 == 50 or count2 == 60 or count2 == 70 or\
                   count2 == 80 or count2 == 90 or count2 == 100 or count2 == 110 or\
                   count2 == 120 or count2 == 130 or count2 == 140 or count2 == 150 or\
                   count2 == 160 or count2 == 170 or count2 == 180 or count2 == 190 or\
                   count2 == 200 or count2 == 210 or count2 == 220 or count2 == 230 or\
                   count2 == 240:
                    shotgun.reload_animate(int(count2/10))
                    
                count2 += 2
                if count2 > 240:
                    count2 = 0

                    shotgun_ammoKeeper.set_totalAmmo(shotgun_ammoKeeper.get_totalAmmo() -\
                                                 (2 - shotgun_ammoKeeper.get_currentAmmo()))
                    shotgun_ammoKeeper.set_currentAmmo(2)
                    reload_gun = False

                if shotgun_ammoKeeper.get_totalAmmo() == 0 and\
                   shotgun_ammoKeeper.get_currentAmmo() == 0:
                    ifShotgun = False
                    ifPistol = True

       
        '''        
        possible_chance = random.randint(0,inc_chance)
        if possible_chance >= int(inc_chance/2):
            possible_upgrade = mySprites.Upgrade()
            upgradeGroup = pygame.sprite.Group(possible_upgrade)
            spawn = True
        else:
            inc_chance += 1
            spawn = False
        '''









      
        allSprites.clear(screen, background)

        if ifPistol == True:
            ammo_type1.clear(screen, background)
        elif ifShotgun == True:
            ammo_type2.clear(screen, background)
            
            

        if ifPistol == True:
            
            gun_type1.clear(screen, background)
            gun_type1.update(cross_hair.get_currentXpos())
            gun_type1.draw(screen)

        elif ifShotgun == True:
            
            gun_type2.clear(screen, background)
            gun_type2.update(cross_hair.get_currentXpos())
            gun_type2.draw(screen)

        if ifPistol == True:
            ammo_type1.update(250,430)
            ammo_type1.draw(screen)
            
        elif ifShotgun == True:
            ammo_type2.update(340,430)
            ammo_type2.draw(screen)
            
        elif ifMinigun == True:
            ammo_type3.update(300,430)
            ammo_type3.draw(screen)

        

            
        duckGroup.clear(screen, background)
        #death bool,duck_type,direction
        
        if ducks_killed != []:
            for ducks in ducks_killed:
                ducks.death_animate(death_count)

                death_count += 1

                
                
                ducks.death(True)
                duckGroup.update()
                duckGroup.draw(screen)
        else:
            duckGroup.update()
            duckGroup.draw(screen)
            
        

        if spawn == True:
            upgradeGroup.clear(screen, background)
            upgradeGroup.update()
            upgradeGroup.draw(screen)
        
        

        
        allSprites.update() 
        allSprites.draw(screen)
        

  
        
        
        
        pygame.display.flip() 

    #unhide the mouse pointer
    pygame.mouse.set_visible(True)

    #close the game window
    pygame.quit()


main()













        
