import pygame


def music_controller(path, state, volume=0.4):
    if not state:
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=-1)
    else:
        pygame.mixer.music.stop()
