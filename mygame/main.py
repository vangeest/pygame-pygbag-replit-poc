import asyncio

import pygame

# TODO: fix framerate issues
#  framerate is determined by VSYNC (display refresh rate), 
#  causing different speeds of the game on different systems
#  (mac with powerplug 2xfaster then on battery)

# TODO: do we move constants and images into main?
#  it is not recommended by pygbag (don't understand why, 
#  it has something to do with blocking code)
#  but it does work and look easier to understand

#
# define constants 
# constants are variables of which the value does not change
# convention is to use uppercase for naming constants
# TODO: do we want to keep this convention? It seems a little less readable
#
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BRICK_WIDTH = 96
BRICK_HEIGHT = 32
BALL_WIDTH = 16
BALL_HEIGHT = 16
PADDLE_WIDTH = 144
PADDLE_HEIGHT = 32

#
# read images
#
spritesheet = pygame.image.load('img/Breakout_Tile_Free.png').convert_alpha() # convert_alpha increases speed of blit and keeps transparancy of .png

# TODO: do we want to use tuples?
#  lists are less common, but are part of the Fundament course
#  alternative with lists: brick_img = pygame.Surface([384, 128])
brick_img = pygame.Surface((384, 128)) # create new image
brick_img.blit(spritesheet, (0, 0), (772, 390, 384, 128)) # copy part of sheet to image
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT)) # resize image

ball_img = pygame.Surface((64, 64))
ball_img.blit(spritesheet, (0, 0), (1403, 652, 64, 64))
ball_img = pygame.transform.scale(ball_img, (BALL_WIDTH, BALL_HEIGHT))

paddle_img = pygame.Surface((243, 64))
paddle_img.blit(spritesheet, (0, 0), (1158, 396, 243, 64))
paddle_img = pygame.transform.scale(paddle_img, (PADDLE_WIDTH, PADDLE_HEIGHT))

async def main():
  #
  # variables
  #
  game_status_msg = "PLAY- STUDENT USE [A][D] - TUTOR USE [SPACE]"
  
  ball_x = 0
  ball_y = 0
  ball_speed_x = 6
  ball_speed_y = 10

  brick_x = [100+0*BRICK_WIDTH, 100+1*BRICK_WIDTH, 100+2*BRICK_WIDTH, 
             1180-1*BRICK_WIDTH, 1180-2*BRICK_WIDTH, 1180-3*BRICK_WIDTH,
             100+0*BRICK_WIDTH, 100+1*BRICK_WIDTH, 100+2*BRICK_WIDTH, 
             1180-1*BRICK_WIDTH, 1180-2*BRICK_WIDTH, 1180-3*BRICK_WIDTH]
  brick_y = [200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT, 
             200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT, 200+0*BRICK_HEIGHT, 
             200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT, 
             200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT, 200+1*BRICK_HEIGHT]

  paddle_x = SCREEN_WIDTH / 2 - PADDLE_WIDTH / 2
  paddle_y = SCREEN_HEIGHT - 2 * PADDLE_HEIGHT

  #
  # init game
  #
  pygame.init()
  print('pygame.init succesfull')
  font = pygame.font.SysFont('default', 64)
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

    # bounce ball against edges of screen
    if ball_x < 0 or ball_x + BALL_WIDTH > SCREEN_WIDTH:
      ball_speed_x = ball_speed_x * -1
    if ball_y < 0 or ball_y + BALL_HEIGHT> SCREEN_HEIGHT:
      ball_speed_y = ball_speed_y * -1

    # move paddle using A and D keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a] : # left arrow or a key is down
      paddle_x = paddle_x - 10
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] : # right arrow or d key is down
      paddle_x = paddle_x + 10

    # move paddle using tutor mode (press SPACE)
    if keys[pygame.K_SPACE] : # space key is down
      paddle_x = ball_x + BALL_WIDTH / 2 - PADDLE_WIDTH / 2
  
    # stop paddle at edge of screen
    if paddle_x < 0 : # paddle touches left edge of screen
      paddle_x = 0
    if paddle_x + PADDLE_WIDTH > SCREEN_WIDTH :  # paddle touches right edge of screen
      paddle_x = SCREEN_WIDTH - PADDLE_WIDTH

    # bouche ball against paddle
    # tip: use () to allow multiline expressions for better readability
    if ( ball_x + BALL_WIDTH > paddle_x and 
         ball_x < paddle_x + PADDLE_WIDTH and
         ball_y + BALL_HEIGHT > paddle_y and
         ball_y < paddle_y + PADDLE_HEIGHT) : # ball collides with paddle
      ball_speed_y = ball_speed_y * -1 # bounce

    # handle collision of ball with bricks
    # TODO: do we want to loop like this? 
    #  for i in range(len(brick_x)-1, -1, -1) : 
    #  is not typical python, but it is closest to how it is done in Fundament
    #  backwards count needed to prevent a OutOfRange error when removing bricks from the array
    # more python like solution: 
    #  for i, x in enumerate(brick_x) : # ignore warning 'x not used within loop body'
    # even more python like solutione: 
    #  use a list of key:value pairs like this 
    #  [{'x': 150, 'y': 200}, {'x': 300, 'y': 200}]
    #  to store bricks
    for i in range(len(brick_x)-1, -1, -1) : 
      # tip: use () to allow multiline expressions for better readability
      if ( ball_x + BALL_WIDTH > brick_x[i] and 
           ball_x < brick_x[i] + BRICK_WIDTH and
           ball_y + BALL_HEIGHT > brick_y[i] and
           ball_y < brick_y[i] + BRICK_HEIGHT ) : # ball collides with brick
        # bounce
        if ( ball_speed_x > 0 and ball_x < brick_x[i] or # right side of ball is outside brick, so ball hits left side of brick
             ball_speed_x < 0 and ball_x + BALL_WIDTH > brick_x[i] + BRICK_WIDTH ) : # left side of ball is outside brick, so ball hits right side of brick
          ball_speed_x = ball_speed_x * -1
        if ( ball_speed_y > 0 and ball_y < brick_y[i] or # top side of ball is outside brick, so ball hits top side of brick
             ball_speed_y < 0 and ball_y + BALL_HEIGHT > brick_y[i] + BRICK_HEIGHT ) : # bottom side of ball is outside brick, so ball hits bottom side of brick
          ball_speed_y = ball_speed_y * -1
        # remove brick 
        brick_x.pop(i)
        brick_y.pop(i)

    # check if you win
    if len(brick_x) == 0 : # no bricks left
      game_status_msg = 'YOU WIN'
      # freeze ball
      ball_speed_x = 0
      ball_speed_y = 0
      
    # check if you're dead
    if ball_y > paddle_y + PADDLE_HEIGHT : # ball below paddle
      game_status_msg = 'YOU ARE DEAD'
      # freeze ball
      ball_speed_x = 0
      ball_speed_y = 0
    
    # clear screen
    screen.fill('black') 

    # draw bricks
    for i in range(0, len(brick_x)) : # TODO: do we want this? It is not typical python, but it is how it is done in Fundament
      screen.blit(brick_img, (brick_x[i], brick_y[i]))

    # draw ball
    screen.blit(ball_img, (ball_x, ball_y))

    # draw paddle
    screen.blit(paddle_img, (paddle_x, paddle_y))

    # draw game status message
    game_status_img = font.render(game_status_msg, True, 'green')
    screen.blit(game_status_img, ((SCREEN_WIDTH - game_status_img.get_width())/2, 0))
    
    # show screen
    pygame.display.flip() 

    # Sleep untill another VSYNC occures (usually 60 times per second)
    await asyncio.sleep(0)  

# This is the program entry point:
asyncio.run(main()) # asyncio.run is non-blocking on pygame-wasm

# Do not add anything from here
