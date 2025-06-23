from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # TODO: your code here
    player_x = 0; player_y = 0  # Starting position
    
    player = canvas.create_rectangle(player_x, player_y, SIZE, SIZE, "blue")
    goal = canvas.create_rectangle(360, 360, 360 + SIZE, 360 + SIZE, "salmon")

    while True:
        x = canvas.get_left_x(player)
        y = canvas.get_top_y(player)

        if (x < 0) or (x + SIZE > CANVAS_WIDTH) or (y < 0) or (y + SIZE > CANVAS_HEIGHT):
            break

        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            # print('left arrow pressed!')
            player_x -= SIZE
        if key == 'ArrowRight':
            # print('right arrow pressed!')
            player_x += SIZE
        if key == 'ArrowUp':
            # print('up arrow pressed!')
            player_y -= SIZE
        if key == 'ArrowDown':
            # print('down arrow pressed!')
            player_y += SIZE
    
        canvas.moveto(player, player_x, player_y)

        # if True:
        #     rand_goal_x = random.randint(0, CANVAS_WIDTH - SIZE)
        #     rand_goal_y = random.randint(0, CANVAS_HEIGHT - SIZE)
        #     canvas.moveto(goal, rand_goal_x, rand_goal_y)

        # sleep
        time.sleep(DELAY)    

if __name__ == '__main__':
    main()