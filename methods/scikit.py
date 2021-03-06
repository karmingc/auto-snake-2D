from sklearn import linear_model
import matplotlib.pyplot as plt
import math
import numpy as np

# sample1 = [[230, 20], [240, 20], [250, 20], [260, 20], [270, 20], [280, 20], [290, 20], [280, 20], [270, 20], [260, 20], [250, 20], [240, 20], [230, 20], [220, 20], [210, 20], [200, 20], [190, 20], [180, 20], [170, 20], [160, 20], [150, 20], [140, 20], [130, 20], [120, 20], [110, 20], [100, 20], [90, 20], [80, 20], [70, 20], [60, 20], [50, 20], [40, 20], [30, 20], [20, 20], [30, 20], [40, 20], [50, 20], [60, 20], [70, 20], [80, 20], [90, 20], [100, 20], [110, 20], [120, 20], [130, 20], [140, 20], [150, 20], [160, 20], [170, 20], [180, 20], [190, 20], [200, 20], [210, 20], [220, 20], [230, 20], [240, 20], [250, 20], [260, 20], [270, 20], [280, 20], [290, 20], [280, 20], [270, 20], [260, 20], [250, 20], [240, 20], [230, 20], [220, 20], [210, 20], [200, 20], [190, 20], [180, 20], [170, 20], [160, 20], [150, 20], [140, 20], [130, 20], [120, 20], [110, 20], [100, 20], [90, 20], [80, 20], [70, 20], [60, 20], [50, 20], [40, 20], [30, 20], [20, 20], [30, 20], [40, 20], [50, 20], [60, 20], [70, 20], [80, 20], [90, 20], [100, 20], [110, 20], [120, 20], [130, 20], [140, 20], [150, 20], [160, 20], [170, 20], [180, 20], [190, 20], [200, 20], [210, 20], [220, 20], [230, 20], [240, 20], [250, 20], [260, 20], [270, 20], [280, 20], [290, 20], [280, 20], [270, 20], [260, 20], [250, 20], [240, 20], [230, 20], [220, 20], [210, 20], [200, 20], [190, 20], [180, 20], [170, 20], [160, 20], [150, 20], [140, 20], [130, 20], [120, 20], [110, 20], [100, 20], [90, 20], [80, 20], [70, 20], [60, 20], [50, 20], [40, 20], [30, 20], [20, 20], [30, 20], [40, 20], [50, 20], [60, 20], [70, 20], [80, 20], [90, 20], [100, 20], [110, 20], [120, 20], [130, 20], [140, 20], [150, 20], [160, 20], [170, 20], [180, 20], [190, 20], [200, 20], [210, 20], [220, 20], [230, 20], [240, 20], [250, 20], [260, 20], [270, 20], [280, 20], [290, 20], [280, 20], [270, 20], [260, 20], [250, 20], [240, 20], [230, 20], [220, 20], [210, 20], [200, 20], [190, 20], [180, 20], [170, 20], [160, 20], [150, 20], [140, 20], [130, 20], [120, 20], [110, 20], [100, 20], [90, 20], [80, 20], [70, 20], [60, 20], [50, 20], [40, 20], [30, 20], [20, 20], [30, 20], [40, 20], [50, 20], [60, 20]]
# sample2 = [[260, 20.0], [270, 20.0], [280, 20.0], [290, 20.0], [300, 20.0], [310, 20.0], [10, 20.0], [20, 20.0], [30, 20.0], [40, 20.0], [50, 20.0], [60, 20.0], [70, 20.0], [80, 20.0], [90, 20.0], [100, 20.0], [110, 20.0], [120, 20.0], [130, 20.0], [120, 20.0], [110, 20.0], [100, 20.0], [90, 20.0], [80, 20.0], [70, 20.0], [60, 20.0], [50, 20.0], [40, 20.0], [30, 20.0], [20, 20.0], [10, 20.0], [0, 20.0], [-10, 20.0], [290, 20.0], [280, 20.0], [270, 20.0], [260, 20.0], [250, 20.0], [240, 20.0], [230, 20.0], [220, 20.0], [210, 20.0], [200, 20.0], [190, 20.0], [180, 20.0], [170, 20.0], [180, 20.0], [190, 20.0], [200, 20.0], [210, 20.0], [220, 20.0], [230, 20.0], [240, 20.0], [250, 20.0], [260, 20.0], [270, 20.0], [280, 20.0], [290, 20.0], [300, 20.0], [310, 20.0], [10, 20.0], [20, 20.0], [30, 20.0], [40, 20.0], [50, 20.0], [60, 20.0], [70, 20.0], [80, 20.0], [90, 20.0], [100, 20.0], [110, 20.0], [120, 20.0], [130, 20.0], [120, 20.0], [110, 20.0], [100, 20.0], [90, 20.0], [80, 20.0], [70, 20.0], [60, 20.0], [50, 20.0], [40, 20.0], [30, 20.0], [20, 20.0], [10, 20.0], [0, 20.0], [-10, 20.0], [290, 20.0], [280, 20.0], [270, 20.0], [260, 20.0], [250, 20.0], [240, 20.0], [230, 20.0], [220, 20.0], [210, 20.0], [200, 20.0], [190, 20.0], [180, 20.0], [170, 20.0], [180, 20.0], [190, 20.0], [200, 20.0], [210, 20.0], [220, 20.0], [230, 20.0], [240, 20.0], [250, 20.0], [260, 20.0], [270, 20.0], [280, 20.0], [290, 20.0], [300, 20.0], [310, 20.0], [10, 20.0], [20, 20.0], [30, 20.0], [40, 20.0], [50, 20.0], [60, 20.0], [70, 20.0], [80, 20.0], [90, 20.0], [100, 20.0], [110, 20.0], [120, 20.0], [130, 20.0], [120, 20.0], [110, 20.0], [100, 20.0], [90, 20.0], [80, 20.0], [70, 20.0], [60, 20.0], [50, 20.0], [40, 20.0], [30, 20.0], [20, 20.0], [10, 20.0], [0, 20.0], [-10, 20.0], [290, 20.0], [280, 20.0], [270, 20.0], [260, 20.0], [250, 20.0], [240, 20.0], [230, 20.0], [220, 20.0], [210, 20.0], [200, 20.0], [190, 20.0], [180, 20.0], [170, 20.0], [180, 20.0], [190, 20.0], [200, 20.0], [210, 20.0], [220, 20.0], [230, 20.0], [240, 20.0], [250, 20.0], [260, 20.0], [270, 20.0], [280, 20.0], [290, 20.0], [300, 20.0], [310, 20.0], [10, 20.0], [20, 20.0], [30, 20.0], [40, 20.0], [50, 20.0], [60, 20.0], [70, 20.0], [80, 20.0], [90, 20.0], [100, 20.0], [110, 20.0], [120, 20.0], [130, 20.0], [120, 20.0], [110, 20.0], [100, 20.0], [90, 20.0], [80, 20.0], [70, 20.0], [60, 20.0], [50, 20.0], [40, 20.0], [30, 20.0], [20, 20.0], [10, 20.0], [0, 20.0], [-10, 20.0], [290, 20.0], [280, 20.0], [270, 20.0], [260, 20.0], [250, 20.0]]


# def findingXY(samplingList):
#     value_x = []
#     value_y = []    
#     for values in samplingList:
#         value_x.append(values[0])
#         value_y.append(values[1])
#     return value_x, value_y

def distance(s1, s2):    
    diff = []    
    for i in range(len(s1)):
        distance = ((s2[i][0] - s1[i][0])**2) + ((s2[i][1] - s1[i][1])**2)
        diff.append(math.sqrt(distance))    
    return diff    

# sample1_x, sample1_y = findingXY(sample1)
# sample2_x, sample2_y = findingXY(sample2)

def subfinder(start, size, car, police):
    diff = distance(car, police)
    mylist = diff
    pattern = diff[0:size]
    matches = []
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            matches.append(pattern)
    
    return len(matches)

def distanceDiff(car, police, appleX, appleY):
    car_diff = []
    police_diff = []
    for i in range(len(car)):
        distance1 = ((car[i][0] - appleX)**2) + ((car[i][1] - appleY)**2)
        distance2 = ((police[i][0] - appleX)**2) + ((police[i][1] - appleY)**2)
        car_diff.append(math.sqrt(distance1))   
        police_diff.append(math.sqrt(distance2))
    return car_diff, police_diff
# plt.plot(diff)
# plt.show()

