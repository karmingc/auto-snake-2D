#pip install pygame==2.0.0.dev6
import pygame
import time
import random
from methods.semi_movements import movements
from methods.scikit import subfinder, distanceDiff
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 30, 80)
green = (0, 255, 0)

 
dis_width = 300
dis_height = 300
 
dis = pygame.display.set_mode((dis_width, dis_height))
 
clock = pygame.time.Clock()
 
car_block = 10
car_speed = 10
# points = 0; 

font_style = pygame.font.SysFont("bahnschrift", 18)
score_font = pygame.font.SysFont("comicsansms", 14)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [round(0), round(0)])
 
def our_car(car_block, car_list):
    pygame.draw.rect(dis, white, [round(car_list[0][0]), round(car_list[0][1]), car_block, car_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [round(dis_width / 6), round(dis_height / 3)])
 
def police(speed):
    policex = round(random.randrange(0, dis_width - car_block) / 10) * 10
    policey = round(random.randrange(0, dis_width - car_block) / 10) * 10
    return policex, policey, speed

 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    car_List = []
    current_score = 0
 
    # foodx = round(random.randrange(0, dis_width - car_block) / 10) * 10
    # foody = round(random.randrange(0, dis_height - car_block) / 10) * 10    
    foodx = 150
    foody = 150
    
 
    policex = dis_width/2
    policey = 30
    #speed
    increase = 1
    direction = 1
    # police_speed = 10

    #auto police
    policex2, policey2, police_speed = police(10)
    
    #track last 20 movements
    police_m = []
    car_m = []
    occurence = 0

    start_time = time.time()

    while not game_over:
 
        while game_close == True:
            dis.fill(black)        
            message("You lost, press q to quit, r to restart", white)    
            Your_score(current_score)
            pygame.display.update()                                            
            
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:                                                                     
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -car_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = car_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -car_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = car_block
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
        
        #auto car, while chasing for food q
        # movements    
        x1, y1, policex2, policey2, foodx, foody = movements(x1, y1, policex2, policey2, foodx, foody) 
        police_m.append([policex2, policey2])
        car_m.append([x1, y1])
        if len(police_m) > 100:
            del police_m[0]
        if len(car_m) > 100:
            del car_m[0]             
        # x1 += x1_change        
        # y1 += y1_change
        if len(police_m) > 25:
            # if subfinder(0,26, car_m, police_m) == 2:
                # car_diff, police_diff = distanceDiff(car_m, police_m, foodx, foody)                
                # print(car_diff)
                # if (car_m[0][0] != car_m[1][0]) and (car_m[0][1] == car_m[1][1]):
                #     y1 += 10                    
                # elif (car_m[0][1] != car_m[1][1]) and (car_m[0][0] == car_m[1][0]):
                #     y1 += 10
            #2 will give similar occurence       
            print(subfinder(0,26, car_m, police_m))

        
        dis.fill(black)
        
        #automatic police changer
        #need to set initial direction
        #once it hits the limits on one side, you switch the direction
        if policex == 30:
            direction = 1
        elif policex == 350:
            direction = -1
        policex += police_speed * direction * increase                

        #police chaser
        if x1 > policex2:
            policex2 += police_speed 
        if y1 > policey2:
            policey2 += police_speed
        if x1 < policex2:
            policex2 -= police_speed
        if y1 < policey2:
            policey2 -= police_speed
        
        
        pygame.draw.rect(dis, red, [round(foodx), round(foody), car_block, car_block])
        pygame.draw.rect(dis, yellow, [round(policex), round(policey), car_block, car_block])
        pygame.draw.rect(dis, yellow, [round(policex2), round(policey2), car_block, car_block])
        #always change the value of head as it goes
        car_Head = []
        car_Head.append(x1)
        car_Head.append(y1)
        car_List.append(car_Head)
        #array kept increasing when len(car_List) > current_score
        #the moment current score was the same, it did not delete the first one
        if len(car_List) > 1:
            del car_List[0]

        our_car(car_block, car_List)
        Your_score(current_score)
        pygame.display.update()
        # print("position of car: " + str(x1) + ", " + str(y1) + ", position of police: " + str(policex2) + ", " + str(policey2))
        #if it hits the police
        if (x1 == policex and y1 == policey) or (x1 == policex2 and y1 == policey2):                
            game_close = True
            end_time = time.time()
            # print("time: " + str(end_time - start_time), "score: " + str(current_score))  
            # print("caught! position of car: " + str(x1) + ", " + str(y1) + ", position of police: " + str(policex2) + ", " + str(policey2))

        # if (x1 >= policex - 10 and x1 <= policex + 10) and (y1 <= policey+20 and y1 >= policey):
        #     y1_change = 0        
            

        #if it touches the apple    
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - car_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - car_block) / 10.0) * 10.0                                    
            current_score += 1             
            # Length_of_car += 1
 
        clock.tick(car_speed)                   
    pygame.quit()
    quit()
 
 
gameLoop()
