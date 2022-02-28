import pygame

BRUTEIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\brute.png")
CANNONIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\cannon.png")
ARCHERIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\archer.png")
BOXERIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\boxer.png")
SUPPORTIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\support.png")
DIAGONALIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\diagonal.png")
MIMICIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\mimic.png")
NINJAIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\ninja.png")
TRANSPORTERIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\transporter.png")
COMMONERIMAGE = pygame.image.load(r"C:\Users\mattf\OneDrive\Desktop\Fichter Gam 2.0\GOM-CODE\assets\commoner.png")

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