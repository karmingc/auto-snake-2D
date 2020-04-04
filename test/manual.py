import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

 
dis_width = 400
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 10
# points = 0; 

font_style = pygame.font.SysFont("bahnschrift", 14)
score_font = pygame.font.SysFont("comicsansms", 14)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    pygame.draw.rect(dis, white, [snake_list[0][0], snake_list[0][1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
def shortestPath(police_x, police_y, snake_x, snake_y):
    return 2
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    current_score = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    policex = dis_width/2
    policey = 50
    #speed
    increase = 1
    direction = 1
    police_speed = 10

    while not game_over:
 
        while game_close == True:
            dis.fill(black)        
            message("You lost", white)    
            Your_score(current_score)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        #the borders are not limits
        if x1 > dis_width:
            x1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 > dis_height:
            y1 = 0
        if y1 < 0:
            y1 = dis_height
        #adjust the x,y changes    
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        
        #automatic police changer
        #need to set initial direction
        #once it hits the limits on one side, you switch the direction
        if policex == 50:
            direction = 1
        elif policex == 350:
            direction = -1
        policex += police_speed * direction * increase
        print(policex)


        
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, yellow, [policex, policey, snake_block, snake_block])
        #always change the value of head as it goes
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        #array kept increasing when len(snake_List) > current_score
        #the moment current score was the same, it did not delete the first one
        if len(snake_List) > 1:
            del snake_List[0]
            
 
        # for x in snake_List[:-1]:
        #     if x == snake_Head:
        #         game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(current_score)
 
        pygame.display.update()

        #if it hits the police
        if x1 == policex and y1 == policey:
            game_close = True

        #if it touches the apple    
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0            
            if police_speed < 0:
                police_speed -= 10
                print(police_speed)
            else:
                police_speed += 10
                print(police_speed)
            current_score += 1
            # Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()