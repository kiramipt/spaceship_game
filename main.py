import time
import random
import curses
import animations.fire as fire
import animations.star as star
import animations.spaceship as spaceship

TIC_TIMEOUT = 0.1
STAR_SYMBOLS = '+*.:'
STARS_COUNT = 150


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    canvas.nodelay(True)

    row_max, column_max = canvas.getmaxyx()
    row_center, column_center = row_max // 2, column_max // 2

    coroutines = []
    for _ in range(STARS_COUNT):
        coroutines.append(
            star.blink(
                canvas=canvas,
                row=random.randint(1, row_max - 1),
                column=random.randint(1, column_max - 1),
                symbol=random.choice(STAR_SYMBOLS))
        )

    coroutines.append(fire.fire(canvas, row_center, column_center))
    coroutines.append(spaceship.animate_spaceship(canvas))

    # main event loop
    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        if len(coroutines) == 0:
            break
        time.sleep(TIC_TIMEOUT)
        canvas.refresh()


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
