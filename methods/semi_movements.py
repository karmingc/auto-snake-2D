def movements(x, y, police_x, police_y, food_x, food_y):
        if x > food_x:  
            if (x+30 >= police_x and police_x > x) and (y+30 >= police_y and y-30 < police_y):
                x -= 10                
            elif (x-30 <= police_x and police_x < x) and (y+30 >= police_y and y-30 < police_y):
                x += 10                
            else:
                x -= 10
        elif x < food_x:
            if (x+30 >= police_x and police_x > x) and (y+30 >= police_y and y-30 < police_y):
                x -= 10                
            elif (x-30 <= police_x and police_x < x) and (y+30 >= police_y and y-30 < police_y):
                x += 10                
            else:
                x += 10    
        else:
            if (x+30 >= police_x and police_x > x) and (y+30 >= police_y and y-30 < police_y):
                x -= 10                
            elif (x-30 <= police_x and police_x < x) and (y+30 >= police_y and y-30 < police_y):
                x += 10     
        # vertical movements             
        if y > food_y:
            if (y+30 >= police_y and police_y > y) and (x+30 >= police_x and x-30 < police_x):
                y -= 10                
            elif (y-30 <= police_y and police_y < y) and (x+30 >= police_x and x-30 < police_x):
                y += 10                
            else:
                y -= 10        
        elif y < food_y:
            if (y+30 >= police_y and police_y > y) and (x+30 >= police_x and x-30 < police_x):
                y -= 10
                # print('closed from top')
            elif (y-30 <= police_y and police_y < y) and (x+30 >= police_x and x-30 < police_x):
                y += 10
                # print('closed from bot')
            else:
                y += 10   
        else:
            if (y+30 >= police_y and police_y > y) and (x+30 >= police_x and x-30 < police_x):
                y -= 10
                # print('closed from top')
            elif (y-30 <= police_y and police_y < y) and (x+30 >= police_x and x-30 < police_x):
                y += 10                       
        return x, y, police_x, police_y, food_x, food_y