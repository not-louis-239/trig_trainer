import pygame as pg

def main():
    scr = pg.Surface((800, 600))
    clock = pg.time.Clock()

    while True:
        events = pg.event.get()
        dt_s = clock.tick(60) / 1_000

        for event in events:
            if event.type == pg.QUIT:
                return

        scr.fill((255, 255, 255))
        pg.display.flip()

if __name__ == "__main__":
    main()
