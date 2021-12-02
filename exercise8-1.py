from math import *

def paint_calc(height, width, cover):
    area = height * width 
    cans = area / cover
    return ceil(cans)

test_h = int(input('Enter the height: '))
test_w = int(input('Enter the width: '))
coverage = 5

print(f"You'll need {paint_calc(test_h, test_w, 5)} cans of paint.")