import random
import pygame
pygame.init()


#collision with





window = pygame.display.set_mode([1010, 570])

goingUp = False
goingDown = False
goingRight = False
goingLeft = False

pygame.font.init()
font = pygame.font.SysFont("comicsansms", 20)
font2 = pygame.font.SysFont("comicsansms", 30)
pygame.mixer.music.load("GameMusic.mp3")
startScreen = pygame.image.load("startScreen.png")
deadSnake = pygame.image.load("deadSnake.png")

textLine1 = font2.render("You Died!", True, (255,255,255))
textLine3 = font.render("(press space to restart)", True, (255,255,255))

c = pygame.time.Clock()


snake = [pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10)]

background = pygame.Rect(10,10,990,550)
border = pygame.Rect(0,0,1010,570)
timer = 0

fx = random.randint(0,99)*10
fy = random.randint(0,55)*10

food = pygame.Rect(fx, fy, 10, 10)

score = 0
x = 0
y = 0
rx = 0
ry = 0
ax = 0
ay = 0




with open('highScores.txt', 'a') as the_file:
    the_file.truncate()
    the_file.write('12')



drawing = True
moving = True
windowRect = pygame.Rect(0,0, 1010, 570)
snakeRect = pygame.Rect(100,100, 50, 100)

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            start = False
    window.blit(startScreen, windowRect)
    pygame.display.flip()

pygame.mixer.music.play(5)

while drawing:

    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                drawing = False
            if event.key == pygame.K_SPACE:
                rx = 500
                ry = 270
                for element in snake:
                    element.x = rx
                    element.y = ry
                goingUp = False
                goingDown = False
                goingRight = False
                goingLeft = False
                score = 0
                snake = [pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10),pygame.Rect(500, 260, 10, 10)]

                    
                moving = True
            if event.key == pygame.K_UP:
                if goingDown != True:
                    goingUp = True
                    goingDown = False
                    goingRight = False
                    goingLeft = False
                    print("up")
            if event.key == pygame.K_DOWN:
                if goingUp != True:
                    goingUp = False
                    goingDown = True
                    goingRight = False
                    goingLeft = False
                    print("down")
            if event.key == pygame.K_LEFT:
                if goingRight != True:
                    goingUp = False
                    goingDown = False
                    goingRight = False
                    goingLeft = True
                    print("left")
            if event.key == pygame.K_RIGHT:
                if goingLeft != True:
                    goingUp = False
                    goingDown = False
                    goingRight = True
                    goingLeft = False
                    print("right")
    
    timer += c.get_time()
    if timer > 50:
        x, y = snake[0].x, snake[0].y
        timer = 0
        if goingUp == True:
            snake[0].y -= 10
        if goingDown == True:
            snake[0].y += 10
        if goingRight == True:
            snake[0].x += 10
        if goingLeft == True:
            snake[0].x -= 10
        
        for i in range(1,len(snake)):
            ax = snake[i].x
            ay = snake[i].y
            
            snake[i].x = x
            snake[i].y = y
            x, y = ax, ay
            if snake[len(snake)-1].x !=snake[0].x and snake[len(snake)-1].y !=snake[0].y:
                if x == snake[0].x and y == snake[0].y:
                    moving = False
        
        if snake[0].x == food.x and snake[0].y == food.y:
            score += 1
            
            for i in range(0,20):
                snake.append(pygame.Rect(ax, ay, 10, 10))
            x = random.randint(1,99)*10
            y = random.randint(1,55)*10
            food.x = x
            food.y = y
            print(str(x) + ", " + str(y))
        if snake[0].x < 10 or snake[0].x > 990 or snake[0].y < 10 or snake[0].y > 550:
            moving = False
        a = 0
        ##for element in snake:
            ##if snake[len(snake)-1].x !=snake[0].x and snake[len(snake)-1].y !=snake[0].y:
                ##if element.x == snake[0].x and element.y == snake[0].y and a > 1:
                    ##moving = False
                    ##print("snake element " + str(a) + " colided with the head at element position (" + str(element.x) + ", " + str(element.y) + "). Head was at: (" + str(snake[0].x) + ", " + str(snake[0].y) + ")")           
            ##a += 1                    
            
        #for i in range(1, len(snake)):
            #if snake[len(snake)-2] != snake[len(snake)-1]:
                #if snake[i].x == snake[0].x or snake[i].y == snake[0].y:
                    #print("quit")
                    #drawing = False
            
    text = font.render("Score: " + str(score), True, (255,255,255))
        
        
    c.tick(30 + score*3)

    pygame.draw.rect(window, (255, 0, 0,), border)
    pygame.draw.rect(window, (0,0,0), background)
    if moving:
        for rectangle in snake:
            pygame.draw.ellipse(window, (255,255,255), rectangle)
    pygame.draw.ellipse(window, (255,0,0), food)
    window.blit(text, (910,530))
    if moving == False:
        textLine2 = font2.render("Your Score: " + str(score), True, (255,255,255))
        window.blit(textLine1, (400, 250))
        window.blit(textLine2, (400, 290))
        window.blit(textLine3, (400, 330))
        window.blit(deadSnake, snakeRect)
        
        
    pygame.display.flip()
