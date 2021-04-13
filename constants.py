#screen parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
X_BOUNDARY = SCREEN_WIDTH/2 -20
Y_BOUNDARY = SCREEN_HEIGHT/2 -20

#Text Parameters
ALIGNMENT = "center"
FONT = ("Courier",10, "normal")

#snake movement parameters
SPEED = 0.1 #update time in ms, lower the number higher the speed
MOVE_DISTANCE = 20

#coordinates for snake and obstacles
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
OBS_LOCATION = [[(0,0),(-20,0),(-40,0)], 
                [(200,0),(200,-20),(200,-40)],
                [(-200,0),(-200,20),(-200,40)],
                [(0,200),(0,220),(0,240)],
                [(0,-200),(0,-220),(0,-240)] ]