import pygame
import  random
import os
pygame.mixer.init()


x = pygame.init()

#coloures
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#creating window
screen_width = 700
screen_height = 400
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()



clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55)
def text_screen(text, colour , x,y):
    screen_text = font.render(text, True , colour)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow ,colour, snake_list, snake_size):                         #

    for x,y in snake_list:                                                          #
        pygame.draw.rect(gameWindow, colour , [x,y,snake_size , snake_size])#

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome in snake Game" , black , 120,100)
        text_screen("press Enter to start Game" , black , 120,140)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("bgmusic.mp3")
                    pygame.mixer.music.play()
                    gameloop()
            pygame.display.update()
            clock.tick(60)



def gameloop():
    # Game specific Variables
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    snake_size = 10

    velocity_x = 3
    velocity_y = 0
    init_velocity = 3

    fps = 30
    #checl if highscore file exists
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt" ,"r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width)
    food_y = random.randint(20, screen_height)
    score = 0

    snake_list = []
    snake_length = 1
    # creating a while loop
    while not exit_game:
        if game_over:

            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            text_screen("Game Over!!! Press Enter to restart", red, 30,200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("bgmusic.mp3")
                        pygame.mixer.music.play()
                        gameloop()



        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity

                    if event.key == pygame.K_a:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10

                if score > int(highscore):
                    highscore = score
                food_x = random.randint(20, screen_width)
                food_y = random.randint(20, screen_height)
                snake_length += 5

            gameWindow.fill(white)
            text_screen("Score:" + str(score) + "  Highscore:"+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("blast.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over= True
                pygame.mixer.music.load("blast.mp3")
                pygame.mixer.music.play()


            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snake_list, snake_size)
        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
    quit()
welcome()
gameloop()






