import asyncio

from itertools import cycle
from tools.sprites_tools import get_frames
from tools.curses_tools import draw_frame

SPACESHIP_FRAMES = get_frames('rocket')


async def animate_spaceship(canvas, row, column):
    for frame in cycle(SPACESHIP_FRAMES):
        draw_frame(canvas, row, column, frame)
        await asyncio.sleep(0)
        draw_frame(canvas, row, column, frame, negative=True)