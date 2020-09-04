import asyncio

from itertools import cycle
from tools.sprites_tools import get_frames
from tools.curses_tools import draw_frame, read_controls, get_frame_size, await_for

SPACESHIP_FRAMES = get_frames('rocket')


async def animate_spaceship(canvas):
    canvas.nodelay(True)
    row_max, column_max = canvas.getmaxyx()
    frame_height, frame_width = get_frame_size(SPACESHIP_FRAMES[0])
    border_size = 1

    cur_row, cur_column = row_max // 2 - frame_height // 2, column_max // 2 - frame_width // 2
    for frame in cycle(SPACESHIP_FRAMES):
        draw_frame(canvas, cur_row, cur_column, frame)
        await asyncio.sleep(0)
        row_offset, column_offset, space_pressedsed = read_controls(canvas)
        draw_frame(canvas, cur_row, cur_column, frame, negative=True)

        cur_row = min(cur_row + row_offset, row_max - frame_height - border_size) if row_offset >= 0 \
            else max(cur_row + row_offset, border_size)
        cur_column = min(cur_column + column_offset, column_max - frame_width - border_size) if column_offset > 0 else \
            max(cur_column + column_offset, border_size)
