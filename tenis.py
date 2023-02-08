import pygame
import random

pygame.init()

width, height = 700, 500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Play with me!")
my_font = pygame.font.SysFont('comicsans',40,False,True)



FPS = 60

black = (0,0,0)
white = (255,255,255)
vel = 5

class pad:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self,win):
        pygame.draw.rect(win,white,(self.x,self.y,self.w,self.h))

    def move(self,up=True):
        if up:
            if self.y>0:
                self.y -= vel
        else:
            if self.y <400:
                self.y += vel

def move_pad(key,left,right):
  #  if key[pygame.K_w]:
  #      left.move(up=True)
  #  if key[pygame.K_s]:
  #      left.move(up=False)

    if key[pygame.K_UP]:
        right.move(up=True)
    if key[pygame.K_DOWN]:
        right.move(up=False)


class Ball:

    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = 5
        self.y_vel = 0

    def draw(self,win):
        pygame.draw.circle(win,white,(self.x,self.y),self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def lost(self):
        self.x = width//2
        self.y = height//2
        self.x_vel *= - 1
        self.y_vel = 0

def draw(win,pads,ball):
    win.fill(black)

    for each_pad in pads:
        each_pad.draw(win)

    ball.draw(win)
    pygame.display.update()

def ball_logic(ball,left,right):
    if ball.x + ball.radius >= width:
        score_left.append(1)
        ball.lost()
    elif ball.x - ball.radius <= 0:
        score_right.append(1)
        ball.lost()
    if ball.y + ball.radius >= height:
        ball.y_vel *= -1
    if ball.y - ball.radius <= 0:
        ball.y_vel *= - 1


    ## pad touch

    if left.y + left.h <ball.y + left.h and left.y + left.h >ball.y and ball.x < 46:
        if ball.y - left.y <= 50:
            ball.x_vel = 5
            ball.y_vel = -5
        if ball.y - left.y > 50:
            ball.x_vel = 5
            ball.y_vel = 5


    if right.y + right.h <ball.y + right.h and right.y + right.h >ball.y and ball.x > 654:
        if ball.y - right.y <= 50:
            if ball.y - right.y <=25:
                ball.x_vel = -5
                ball.y_vel = -9
            else:
                ball.x_vel = -5
                ball.y_vel = -5
        if ball.y - right.y > 50:
            if ball.y - right.y < 75:
                ball.x_vel = -5
                ball.y_vel = 9
            else:
                ball.x_vel = -5
                ball.y_vel = 5

def left_pad_logic(ball,left,pad_speed,pad_random_pos):
    if ball.x_vel < 0:
        if ball.x < 350:
            if ball.y - (left.y+(pad_random_pos*10)) <=0:
                if left.y > 0:
                    left.y -= pad_speed
                if abs(ball.y-left.y)>0 and abs(ball.y-left.y)>10 and ball.y<16:
                    ball.y_vel = 5
            elif ball.y - (left.y+(pad_random_pos*10))>0:
                if left.y < 400:
                    left.y += pad_speed
                if abs(ball.y-left.y)>0 and  abs(ball.y-left.y)>10 and ball.y>480:
                    ball.y_vel = -5

score_left = []
score_right = []
def main():
    run = True
    clock = pygame.time.Clock()

    left = pad(0,150,30,100)
    right = pad(670,150,30,100)
    ball = Ball(width//2,height//2,15)

    while run:
        clock.tick(FPS)
        draw(win,[left,right],ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        move_pad(keys, left, right)
        ball.move()

        ball_logic(ball,left,right)



        #print(len(score_left),len(score_right))

        left_pad_logic(ball, left,random.randint(6,8),random.randint(1,9))

        text = my_font.render("{} - {}".format(len(score_left),len(score_right)),1,(255,255,255))
        win.blit(text,(300,20))
        pygame.display.update()



    pygame.quit()

if __name__ == "__main__":
    main()