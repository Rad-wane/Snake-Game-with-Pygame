import pygame
import sys
import random

pygame.init()

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((w_h/2), (w_h/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0

    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*grid_size))%w_h), (cur[1]+(y*grid_size))%w_h)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        self.length = 1
        self.positions = [((w_h/2), (w_h/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
    
    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_size,grid_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)
    
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, g_w_h-1)*grid_size, random.randint(0, g_w_h-1)*grid_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

    
def drawGrid(surface):
    for y in range(0, int(g_w_h)):
        for x in range(0, int(g_w_h)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*grid_size, y*grid_size), (grid_size,grid_size))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*grid_size, y*grid_size), (grid_size,grid_size))
                pygame.draw.rect(surface, (84,194,205), rr)

w_h = 480
grid_size=20
g_w_h=w_h/grid_size
up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
  pygame.init()

  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((w_h, w_h), 0, 32)

  surface = pygame.Surface(screen.get_size())
  surface = surface.convert()
  high_score=0
  
  snake=Snake()
  food=Food()
  
  myfont = pygame.font.SysFont("monospace",16)
  
  while True:
      clock.tick(10)
      snake.handle_keys()
      drawGrid(surface)  
      if snake.score>=high_score:
          high_score=snake.score
      snake.move()
      if snake.get_head_position() == food.position:
        
        snake.length += 1
        snake.score += 1
        food.randomize_position()
      
      snake.draw(surface)
      food.draw(surface)
      screen.blit(surface, (0,0))
      text = myfont.render("Score {0}".format(snake.score)+" \n High Score {0}".format(high_score), 1, (0,0,0))
      
      screen.blit(text, (5,10))
      pygame.display.update()
main()

