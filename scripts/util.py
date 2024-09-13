import os

import pygame

BASE_IMG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/images/')

def load_image(path):
    img = pygame.image.load(os.path.join(BASE_IMG_PATH, path)).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    full_path = os.path.join(BASE_IMG_PATH, path)
    try:
        for img_name in sorted(os.listdir(full_path)):
            images.append(load_image(os.path.join(path, img_name)))
    except FileNotFoundError:
        print(f"Error: The path '{full_path}' does not exist.")
    return images