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

#
# read images
#
sheet = pygame.image.load('img/Breakout_Tile_Free.png').convert_alpha() # convert increases speed of blit and alpha keeps transparancy of .png
sheet_width_new = sheet.get_width() * BRICK_WIDTH / 384
sheet_height_new = sheet.get_height() * BRICK_HEIGHT / 128
sheet = pygame.transform.scale(sheet, (sheet_width_new, sheet_height_new))
brick_img = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
brick_img.blit(sheet, (0, 0), (0, 0, BRICK_WIDTH, BRICK_HEIGHT))

async def main():
  #
  # variables
  #
  ball_x = 0
  ball_y = 0
  ball_speed_x = 1
  ball_speed_y = 1

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

    if ball_x < 0 or ball_x > SCREEN_WIDTH:
      ball_speed_x = ball_speed_x * -1
    if ball_y < 0 or ball_y > SCREEN_HEIGHT:
      ball_speed_y = ball_speed_y * -1

    # draw everything
    backgroundColor = (0, 0, 0) # black
    screen.fill(backgroundColor) # clear screen
    screen.blit(brick_img, (ball_x, ball_y, BRICK_WIDTH, BRICK_HEIGHT))
    pygame.display.flip() # show all changes on the screen

    # Sleep untill another VSYNC occures (usually 60 times per second)
    await asyncio.sleep(0)  

# This is the program entry point:
asyncio.run(main()) # asyncio.run is non-blocking on pygame-wasm

# Do not add anything from here
