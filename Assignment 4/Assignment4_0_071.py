""" Name: Assignment 4 v0.071
    Authors: Joel Murphy
    Date: July 13, 2013
    Purpose: Side scroller game, collect coins to get points and avoid enemies.
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.delay = 6
        self.imgDelay = 3
        self.pause = 0
        self.imgPause = 0
        self.frame = 0
        self.dy = 0
        self.up = -1
        self.down = 1
        self.speed = 1.1
        self.slow = 1.2
        self.image = self.imgList[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = 50
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("yay.ogg")
            self.sndThunder = pygame.mixer.Sound("thunder.ogg")
            self.sndEngine = pygame.mixer.Sound("engine.ogg")
            self.sndEngine.play(-1)
    
    def loadImages(self):
        imgMaster = pygame.image.load("images/PlayerSpriteSheet.bmp")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (39, 36)
        offset = ((2, 2), (45, 2), (88, 2), (131, 2))

        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.PlayerAnimate()
        if mousey != self.rect.centery:
            self.pause += 1
            """if mousey < self.rect.centery:
                self.dy = self.up
            else:
                self.dy = self.down"""
            if self.pause >= 6:
                if self.rect.centery + (self.dy * self.speed) > screen.get_height() - 28:
                    self.rect.center = (50, screen.get_height() - 28)
                    self.dy = 0
                elif self.rect.centery + (self.dy * self.speed) < 18:
                    self.rect.center = (50, 18)
                    self.dy = 0
                else:
                    if self.rect.centery > mousey and self.dy >= 0:
                        self.dy = -1
                    elif self.rect.centery < mousey and self.dy <= 0:
                        self.dy = 1
                    
                    if 0.5 >= (self.rect.centery + self.dy) - mousey > 0 or -0.5 <= (self.rect.centery + self.dy) - mousey < 0:
                        self.rect.center = (50, mousey)
                        self.dy = 0
                    elif (self.rect.centery + (self.dy * self.speed) <= mousey + 50 and self.dy < 0) or (self.rect.centery + (self.dy * self.speed) >= mousey - 50 and self.dy > 0):
                        if self.dy / self.slow > 1:
   ###                      print 'slowdown'
                            self.dy = self.dy / self.slow
                    else:
                        self.dy = self.dy * self.speed
                    self.rect.centery += self.dy
        else:
            self.pause = 0
            self.dy = 0
        print(mousex, mousey, self.rect.center, self.dy)
        
    def PlayerAnimate(self):
        self.imgPause += 1
        oldCenter = self.rect.center
        if self.imgPause >= self.imgDelay:
            self.imgPause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = self.imgList[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter
            #self.rect.center = (320, 240)
                
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/coin.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.height = screen.get_height()-31
        self.reset()
        
        self.dx = 4
    
    def update(self, height):
        self.height = height
        print height
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.left = screen.get_width()
        self.rect.centery = self.height

class GroundEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.imgDelay = 3
        self.imgPause = 0
        self.frame = 0
        self.image = self.imgList[0]
        self.rect = self.image.get_rect()
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("images/GEnemySpriteSheet.bmp")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (39, 42)
        offset = ((2, 2), (45, 2), (88, 2), (131, 2))

        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.GEnemyAnimate()
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def GEnemyAnimate(self):
        self.imgPause += 1
        oldCenter = self.rect.center
        if self.imgPause >= self.imgDelay:
            self.imgPause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = self.imgList[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter
            #self.rect.center = (320, 240)
    
    def reset(self):
        self.rect.bottom = screen.get_height() - 10
        self.rect.left = screen.get_width()
        self.dx = random.randrange(5, 10)

class AirEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.imgDelay = 3
        self.imgPause = 0
        self.frame = 0
        self.image = self.imgList[0]
        self.rect = self.image.get_rect()
        self.reset()
        
    def loadImages(self):
        imgMaster = pygame.image.load("images/AEnemySpriteSheet.bmp")
        imgMaster = imgMaster.convert()
        
        self.imgList = []
        
        imgSize = (102, 84)
        offset = ((2, 2), (108, 2), (214, 2), (320, 2))

        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.imgList.append(tmpImg)
    
    def update(self):
        self.AEnemyAnimate()
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def AEnemyAnimate(self):
        self.imgPause += 1
        oldCenter = self.rect.center
        if self.imgPause >= self.imgDelay:
            self.imgPause = 0
            self.frame += 1
            if self.frame >= len(self.imgList):
                self.frame = 0
                
            self.image = self.imgList[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter
            #self.rect.center = (320, 240)
    
    def reset(self):
        self.rect.bottom = random.randrange(84, screen.get_height() - 30)
        self.rect.left = screen.get_width()
        self.dx = random.randrange(5, 10)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Background.gif")
        self.rect = self.image.get_rect()
        self.dx = 1
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx
        if self.rect.right <= 640:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0

class Hills(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Hills.gif")
        self.rect = self.image.get_rect()
        self.dx = 3
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx
        if self.rect.right <= 640:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0

class Foreground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Foreground.gif")
        self.rect = self.image.get_rect()
        self.dx = 4
        self.reset()
        
    def update(self):
        self.rect.left -= self.dx
        if self.rect.right <= 640:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0

class Sidewalk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Sidewalk.gif")
        self.rect = self.image.get_rect()
        self.rect.left = 0

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.travel = 0
        self.getPoint = 30
        self.addEnemyCounter = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.travel += 1
        if self.travel >= self.getPoint:
            self.score += 2
            self.addEnemyCounter += 2
            self.travel = 0
        self.text = "planes: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
    
def game():
    pygame.display.set_caption("Mail Pilot!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player = Player()
    coin = Coin()
    gEnemy = []
    enemyThreshold = 300
    initialAEnemies = 2 * enemyThreshold
    AReinforcements = False
    aEnemy = []
    bground = Background()
    hills = Hills()
    foreground = Foreground()
    sidewalk = Sidewalk()
    scoreboard = Scoreboard()
    
    for index in range(2):
        gEnemy.append(GroundEnemy())
    
    friendSprites = pygame.sprite.OrderedUpdates(bground, hills, foreground, sidewalk, player)
    coinSprite = pygame.sprite.Group(coin)
    enemySprites = pygame.sprite.Group(gEnemy, aEnemy)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        
        clock.tick(30)
        pygame.mouse.set_visible(True)
        enemySprites = pygame.sprite.Group(gEnemy, aEnemy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        
        #check collisions
        
        if player.rect.colliderect(coin.rect):
            player.sndYay.play()
            coin.reset()
            scoreboard.score += 100
            scoreboard.addEnemyCounter += 100
        print scoreboard.addEnemyCounter, enemyThreshold, AReinforcements, len(aEnemy), len(gEnemy)
        hitClouds = pygame.sprite.spritecollide(player, enemySprites, False)
        if hitClouds:
            player.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theCloud in hitClouds:
                theCloud.reset()
        
        if scoreboard.addEnemyCounter >= enemyThreshold:
            if AReinforcements == False:
                AReinforcements = True
                scoreboard.addEnemyCounter = 0
                gEnemy.append(GroundEnemy())
            else:
                AReinforcements = False
                scoreboard.addEnemyCounter = 0
                
                aEnemy.append(AirEnemy())
        
        
        friendSprites.update()
        if scoreboard.score < initialAEnemies:
            coinSprite.update(screen.get_height()-31)
        else:
            coinSprite.update(random.randrange(21, screen.get_height()-31))
        enemySprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        coinSprite.draw(screen)
        enemySprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    player.sndEngine.stop()
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
    
def instructions(score):
    pygame.display.set_caption("Mail Pilot!")

    player = Player()
    bground = Background()
    hills = Hills()
    foreground = Foreground()
    sidewalk = Sidewalk()
    
    allSprites = pygame.sprite.OrderedUpdates(bground, hills, foreground, sidewalk, player)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Mail Pilot.     Last score: %d" % score ,
    
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    player.sndEngine.stop()    
    pygame.mouse.set_visible(True)
    return donePlaying
        
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()


if __name__ == "__main__":
    main()
    
    
