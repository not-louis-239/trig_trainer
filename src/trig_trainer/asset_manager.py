from pathlib import Path
import pygame as pg

ROOT_DIR = Path(__file__).parents[2]

ASSETS_DIR = ROOT_DIR / "assets"

FONT_DIR = ASSETS_DIR / "fonts"

class Assets:
    def __init__(self) -> None:
        self.font_path: Path = FONT_DIR / "SourceCodePro-VariableFont_wght.ttf"
