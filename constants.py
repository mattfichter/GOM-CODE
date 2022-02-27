import pygame

BRUTEIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/brute.png")
CANNONIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/cannon.png")
ARCHERIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/archer.png")
BOXERIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/boxer.png")
SUPPORTIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/support.png")
DIAGONALIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/diagonal.png")
MIMICIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/mimic.png")
NINJAIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/ninja.png")
TRANSPORTERIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/transporter.png")
COMMONERIMAGE = pygame.image.load("/Users/mattfichter/GOM_V2.0/assets/commoner.png")

IMAGELIST = [BRUTEIMAGE, CANNONIMAGE, ARCHERIMAGE, BOXERIMAGE, SUPPORTIMAGE, DIAGONALIMAGE, MIMICIMAGE, NINJAIMAGE, TRANSPORTERIMAGE, COMMONERIMAGE]

WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BOARDSTART = 600,180
BOARDEND = 1320,900
CHARACTERSTART = 360,930
ROWS = 6
COLS = 6
SQUARE_SIZE = 120
FPS = 60

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)