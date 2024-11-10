import pygame, random


def music_controller(path, state, volume=0.2):
    if not state:
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=-1)
    else:
        pygame.mixer.music.stop()


def random_ambiant_song():
    songs = ["./Musiques/Ambiant/HaggstromMinecraft.mp3", "./Musiques/Ambiant/MysteriousForest.mp3",
             "./Musiques/Ambiant/Stardew Valley The Deep Woods.mp3"]
    selected_song = random.choice(songs)
    return selected_song