import asyncio

import time

import pygame

# Try explicitly to declare all your globals at once to facilitate compilation later.

# Do init here and load any assets right now to avoid lag at runtime or network errors.

async def main():
  pygame.init()
  width, height = 800, 600
  dvdLogoSpeed = [1, 1]
  backgroundColor = 0, 0, 0

  screen = pygame.display.set_mode((width, height))

  dvdLogo = pygame.image.load("img/dvd-logo-white.png")
  dvdLogoRect = dvdLogo.get_rect()

  while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop, maybe less on some mobile devices

        print(f"Hello[{COUNT_DOWN}] from Python")
        screen.fill(backgroundColor)

        screen.blit(dvdLogo, dvdLogoRect)
        dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

        if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
            dvdLogoSpeed[0] = -dvdLogoSpeed[0]
        if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
            dvdLogoSpeed[1] = -dvdLogoSpeed[1]

        pygame.display.flip()
        # time.sleep(10 / 1000)

        await asyncio.sleep(0)  # Very important, and keep it 0


# This is the program entry point:
asyncio.run(main())

# Do not add anything from here
# asyncio.run is non-blocking on pygame-wasm

