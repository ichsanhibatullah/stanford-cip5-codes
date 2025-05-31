from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

''' OWN CODE: SUCCESS BUILD, FAILED ON CHECK CORRECT'''
# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     # TODO, your code here
#     remaining_empty_base = CANVAS_WIDTH - (BRICKS_IN_BASE * BRICK_WIDTH)    
    
#     for i in range(BRICKS_IN_BASE):
#         current_bricks = BRICKS_IN_BASE - i

#         for j in range(current_bricks):
#             left_x = j * BRICK_WIDTH + (i * (BRICK_WIDTH / 2)) + (remaining_empty_base / 2)
#             top_y = CANVAS_HEIGHT - (i) * BRICK_HEIGHT
#             right_x = (j + 1) * BRICK_WIDTH + (i * (BRICK_WIDTH / 2)) + (remaining_empty_base / 2)
#             bottom_y = CANVAS_HEIGHT - (i + 1) * BRICK_HEIGHT

#             canvas.create_rectangle(
#                 left_x,
#                 top_y,
#                 right_x,
#                 bottom_y,
#                 "yellow",
#                 "black"
#             )

''' OWN-ADAPTED CODE: SUCCESS'''
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    base_width = BRICKS_IN_BASE * BRICK_WIDTH
    start_x = (CANVAS_WIDTH - base_width) // 2
    start_y = CANVAS_HEIGHT - BRICK_HEIGHT
    
    for row in range(BRICKS_IN_BASE):
        # Calculate the number of bricks in the current row
        bricks_in_row = BRICKS_IN_BASE - row

        # Calculate the starting x-coordinate for the current row
        row_start_x = start_x + (BRICKS_IN_BASE - bricks_in_row) * BRICK_WIDTH // 2

        # Draw each brick in the current row
        for brick in range(bricks_in_row):
            left_x = row_start_x + brick * BRICK_WIDTH
            top_y = start_y - row * BRICK_HEIGHT
            right_x = left_x + BRICK_WIDTH
            bottom_y = top_y + BRICK_HEIGHT

            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                "yellow",
                "black"
            )

# def draw_pyramid(canvas):
#     # Calculate the starting position of the first brick in the base row
#     base_width = BRICKS_IN_BASE * BRICK_WIDTH
#     start_x = (CANVAS_WIDTH - base_width) // 2
#     start_y = CANVAS_HEIGHT - BRICK_HEIGHT

#     for row in range(BRICKS_IN_BASE):
#         # Calculate the number of bricks in the current row
#         bricks_in_row = BRICKS_IN_BASE - row

#         # Calculate the starting x-coordinate for the current row
#         row_start_x = start_x + (BRICKS_IN_BASE - bricks_in_row) * BRICK_WIDTH // 2

#         # Draw each brick in the current row
#         for brick in range(bricks_in_row):
#             x1 = row_start_x + brick * BRICK_WIDTH
#             y1 = start_y - row * BRICK_HEIGHT
#             x2 = x1 + BRICK_WIDTH
#             y2 = y1 + BRICK_HEIGHT
#             canvas.create_rectangle(x1, y1, x2, y2, "yellow", "black")

# def random_color():
#     """Generate a random color."""
#     return "#%06x" % random.randint(0, 0xFFFFFF)

# def main():
#     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
#     draw_pyramid(canvas)

if __name__ == '__main__':
    main()