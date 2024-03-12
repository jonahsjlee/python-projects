'''
Jonah Lee
Computing ID: wkx9ff
'''

def gellish2(age):
    return 191.5 - (0.007 * (age*age))

def in_target_range(hr, age):
    hrmax = gellish2(age)
    boundary_lower  = hrmax * 0.65
    boundary_upper = hrmax * 0.85
    return hr >= boundary_lower and hr <= boundary_upper

