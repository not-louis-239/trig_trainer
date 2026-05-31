#!/usr/bin/env python3

# Copyright 2026 Louis Masarei-Boulton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from pathlib import Path

import pygame as pg

sys.path.insert(0, str(Path(__file__).parent / "src"))

from trig_trainer.trainer import TrigTrainer
from trig_trainer.constants import FPS

def main():
    pg.init()
    pg.key.start_text_input()

    screen = pg.display.set_mode((1100, 800))
    pg.display.set_caption("Trig Trainer")
    clock = pg.time.Clock()

    t = TrigTrainer()

    running = True
    while running:
        keys = pg.key.get_pressed()
        events = pg.event.get()
        dt_s = clock.tick(FPS) / 1_000
        t.game.take_input(keys=keys, events=events, dt_s=dt_s)

        for event in events:
            if event.type == pg.QUIT:
                running = False

        t.game.update(dt_s)
        t.game.draw(screen)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
