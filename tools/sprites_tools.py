import os


def get_frames(sprite_directory):
    sprites = []
    for file in os.listdir(f"sprites/{sprite_directory}"):
        with open(f"sprites/{sprite_directory}/{file}") as f:
            sprites.append(f.read())
    return sprites
