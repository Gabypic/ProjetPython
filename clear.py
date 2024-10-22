import os
import time

def clear_terminal(clear_time):
    time.sleep(clear_time)
    os.system('cls' if os.name == 'nt' else 'clear')