import sys, pygame
pygame.init()

size = width, height = 800, 600
black = 0,0,0

screen = pygame.display.set_mode(size)
rectangle = pygame.Rect(0,50,100,100)
rectangle2 = pygame.Rect(width,50,100,100)

def moveRect1():
    rectangle.left +=1

def moveRect2():
    rectangle2.left +=1

def drawScreen():
    screen.fill(pygame.Color(255,0,0,255))
    pygame.draw.rect(screen,black,rectangle,5)
    pygame.draw.rect(screen,black,rectangle2,0)
    pygame.display.flip()

def updateLogic():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if rectangle.right == width:
        moveRect1()
        rectangle2.right = 0
    elif rectangle.left <= width:
        moveRect1()
        moveRect2()
    elif rectangle2.right < width:
        moveRect2()
    elif rectangle2.right == width:
        moveRect2()
        rectangle.right = 0
    else:
        moveRect2()
        moveRect1()

while 1:
        drawScreen()
        updateLogic()