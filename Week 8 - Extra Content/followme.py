from graphics import Canvas
import time

CANVAS_SIZE = 400
BALL_DIAMETER = 50
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    ball = canvas.create_oval(
        0, 0,
        BALL_DIAMETER, 
        BALL_DIAMETER,
        'blue'
    )
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # TODO: Write your code here!! :)
        
        if mouse_x > 0 and mouse_y > 0:
            canvas.moveto(ball, mouse_x - BALL_DIAMETER/2, mouse_y - BALL_DIAMETER/2)
        
        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()