import curses
import random
from tools.curses_tools import await_for


async def blink(canvas, row, column, symbol='*'):
    while True:
        random_delay = random.randint(0, 10)
        await await_for(random_delay)

        canvas.addstr(row, column, symbol, curses.A_DIM)
        await await_for(20)

        canvas.addstr(row, column, symbol)
        await await_for(3)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await await_for(5)

        canvas.addstr(row, column, symbol)
        await await_for(3)
