"""
Name: Jonah Lee
Computing ID: wkx9ff
"""

def fine(speed_limit, my_speed, zone = ""):
    total = 0
    miles_over_limit = my_speed - speed_limit
    if(miles_over_limit < -10):
        total += 30
    if(miles_over_limit >= 20):
        total += 350
    if(zone == "school" or zone == "work"):
        if(miles_over_limit >= 0):
            total += miles_over_limit*7
    elif(zone == "residential"):
        total += 200
        if(miles_over_limit >= 0):
            total += miles_over_limit*8
    elif(zone == ""):
        if (miles_over_limit >= 0):
            total += miles_over_limit*6
    return total

def demerits(speed_limit, my_speed):
    demerit_points = 0
    miles_over_limit = my_speed - speed_limit
    if(miles_over_limit >= 1 and miles_over_limit <= 9):
        demerit_points = 3
    elif (miles_over_limit >= 10 and miles_over_limit <= 19):
        demerit_points = 4
    elif (miles_over_limit >= 20):
        demerit_points = 6
    else:
        demerit_points = 0
    return demerit_points

