# SKILAVERKEFNI 2 FÖLL
# Ragnar Helgi B. Unnþórsson

from math import pi
from time import sleep, time
from colorama import Fore

# LIÐUR 1
def langhlid(a, b):
    return a**2 + b**2

# LIÐUR 2
def margfeldi_af(x, y):
    if x % y == 0:
        return True
    else:
        return False

# LIÐUR 3
def ferning_ur_stjornum(x):
    for _ in range(x): print("*" * x)

# LIÐUR 4
def er_slett_tala(x):
    if x % 2 == 0:
        return True
    else:
        return False

# LIÐUR 5
def flatarmal_hrings(x):
    return x ** 2 * pi

# LIÐUR 6
def bank_bank(x):
    timeout = time() + x
    while True:
        print(f"{Fore.RED}BÁNK BÁNK WELCOME TO THE RICE FIELDS MOTHER FRICKER")
        if time() >= timeout: break
        sleep(.2)