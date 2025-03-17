import math 
def paint_ned(height,weidth):

    final = math.ceil((height*weidth)/10)
    print(f"you need {final} number of cans")

height_wall = int(input("height of the wall="))

weidth_wall = int(input("weidth of the wall="))

paint_ned(height = height_wall,weidth = weidth_wall)