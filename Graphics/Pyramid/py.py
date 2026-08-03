from graphics import Canvas

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 300
BRICK_WIDTH = 30
BRICK_HEIGHT = 12
BRICKS_IN_BASE = 14

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        row_width = bricks_in_row * BRICK_WIDTH
        start_x = (CANVAS_WIDTH - row_width) / 2
        row_y = CANVAS_HEIGHT - (row + 1) * BRICK_HEIGHT

        for i in range(bricks_in_row):
            
            x1 = start_x + (i * BRICK_WIDTH)
            y1 = row_y
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT
            
            canvas.create_rectangle(x1, y1, x2, y2)

if __name__ == '__main__':
    main()
