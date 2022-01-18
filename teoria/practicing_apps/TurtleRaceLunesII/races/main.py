import pygame, sys


class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/turtle.png")
        self.position = (x, y)
        self.name = "Tortuga"
    
    def avanzar(self):
        self.position[0] += random.rancdint(1, 6)

class Game():
    runners = []
    __startLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        firstRunner = Runner(self.__startLine, 240)
        firstRunner.name = 'Speedy'
        self.runners.append(firstRunner)
        
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            
            pygame.display. flip()
        
        pygame.quit()
        sys.exit()
            
                    


if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()