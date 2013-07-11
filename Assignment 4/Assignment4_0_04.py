""" Name: Assignment 4 v0.04
    Authors: Joel Murphy
    Date: July 10, 2013
    Purpose: Side scroller game, collect coins to get points and avoid enemies.
"""
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/character.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.delay = 6
        self.pause = 0
        self.dy = 0
        self.up = -1
        self.down = 1
        self.speed = 1.1
        self.slow = 1.2
        
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("yay.ogg")
            self.sndThunder = pygame.mixer.Sound("thunder.ogg")
            self.sndEngine = pygame.mixer.Sound("engine.ogg")
            self.sndEngine.play(-1)
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        if mousey != self.rect.centery:
            self.pause += 1
            """if mousey < self.rect.centery:
                self.dy = self.up
            else:
                self.dy = self.down"""
            if self.pause >= 6:
                if self.rect.centery + (self.dy * self.speed) > screen.get_height() - 31:
                    self.rect.center = (50, screen.get_height() - 31)
                    self.dy = 0
                elif self.rect.centery + (self.dy * self.speed) < 21:
                    self.rect.center = (50, 21)
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
                            print 'slowdown'
                            self.dy = self.dy / self.slow
                    else:
                        self.dy = self.dy * self.speed
                    self.rect.centery += self.dy
        else:
            self.pause = 0
            self.dy = 0
        print(mousex, mousey, self.rect.center, self.dy)
                
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/coin.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = 5
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.left = screen.get_width()
        self.rect.centery = random.randrange(10, screen.get_height()-10)

class GroundEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/groundEnemy.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
    
    def reset(self):
        self.rect.bottom = screen.get_height() - 10
        self.rect.left = screen.get_width()
        self.dx = random.randrange(5, 10)

class AirEnemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/airEnemy.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right < 0:
            self.reset()
    
    def reset(self):
        self.rect.bottom = random.randrange(20, screen.get_height() - 30)
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
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
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
    gEnemy1 = GroundEnemy()
    gEnemy2 = GroundEnemy()
    gEnemy3 = GroundEnemy()
    aEnemy1 = AirEnemy()
    aEnemy2 = AirEnemy()
    background = Background()
    hills = Hills()
    foreground = Foreground()
    sidewalk = Sidewalk()
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.OrderedUpdates(background, hills, foreground, sidewalk, coin, player)
    enemySprites = pygame.sprite.Group(gEnemy1, gEnemy2, gEnemy3, aEnemy1, aEnemy2)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        
        #check collisions
        
        if player.rect.colliderect(coin.rect):
            player.sndYay.play()
            coin.reset()
            scoreboard.score += 100

        hitClouds = pygame.sprite.spritecollide(player, enemySprites, False)
        if hitClouds:
            player.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
            for theCloud in hitClouds:
                theCloud.reset()
        
        friendSprites.update()
        enemySprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
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
    background = Background()
    hills = Hills()
    foreground = Foreground()
    sidewalk = Sidewalk()
    
    allSprites = pygame.sprite.OrderedUpdates(background, hills, foreground, sidewalk, player)
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Mail Pilot.     Last score: %d" % score ,
    "Instructions:  You are a mail pilot,",
    "delivering mail to the islands.",
    "",
    "Fly over an island to drop the mail,",
    "but be careful not to fly too close",    
    "to the clouds. Your plane will fall ",
    "apart if it is hit by lightning too",
    "many times. Steer with the mouse.",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
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
    
    
