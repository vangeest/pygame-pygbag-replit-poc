import asyncio

import pygame

#
# define constants 
# constants are variables of which the value does not change
# convention is to use uppercase for naming constants
#
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BRICK_WIDTH = 96
BRICK_HEIGHT = 32
BALL_WIDTH = 16
BALL_HEIGHT = 16

#
# read images
#
spritesheet = pygame.image.load('img/Breakout_Tile_Free.png').convert_alpha() # convert_alpha increases speed of blit and keeps transparancy of .png

brick_img = pygame.Surface((384, 128)) # create new image
brick_img.blit(spritesheet, (0, 0), (0, 0, 384, 128)) # copy part of sheet to image
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT)) # resize image

ball_img = pygame.Surface((64, 64))
ball_img.blit(spritesheet, (0, 0), (1403, 652, 64, 64))
ball_img = pygame.transform.scale(ball_img, (BALL_WIDTH, BALL_HEIGHT))

async def main():
  #
  # variables
  #
  ball_x = 0
  ball_y = 0
  ball_speed_x = 1
  ball_speed_y = 1

  brick_x = [100+0*BRICK_WIDTH, 100+1*BRICK_WIDTH, 100+2*BRICK_WIDTH, 100+3*BRICK_WIDTH, 100+4*BRICK_WIDTH,
             100+0*BRICK_WIDTH, 100+1*BRICK_WIDTH, 100+2*BRICK_WIDTH, 100+3*BRICK_WIDTH, 100+4*BRICK_WIDTH]
  brick_y = [200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT,
             200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT]
  
  #
  # init game
  #
  pygame.init()
  print('pygame.init succesfull')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  #
  # game loop
  #
  print('mygame is running')
  running = True
  while running:
    # do not use pygame.event.get() as it interferes with await later in the programm
    
    # move ball
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    if ball_x < 0 or ball_x + BALL_WIDTH > SCREEN_WIDTH:
      ball_speed_x = ball_speed_x * -1
    if ball_y < 0 or ball_y + BALL_HEIGHT> SCREEN_HEIGHT:
      ball_speed_y = ball_speed_y * -1

    # clear screen
    backgroundColor = (0, 0, 0) # black
    screen.fill(backgroundColor) 

    # draw bricks
    for i in range(0, len(brick_x)) : # TODO: do we want this? It is not typical python, but it is how it is done in Fundament
      screen.blit(brick_img, (brick_x[i], brick_y[i], BRICK_WIDTH, BRICK_HEIGHT))

    # draw ball
    screen.blit(ball_img, (ball_x, ball_y, BALL_WIDTH, BALL_HEIGHT))
   
    # show screen
    pygame.display.flip() 

    # Sleep untill another VSYNC occures (usually 60 times per second)
    await asyncio.sleep(0)  

# This is the program entry point:
asyncio.run(main()) # asyncio.run is non-blocking on pygame-wasm

# Do not add anything from here
