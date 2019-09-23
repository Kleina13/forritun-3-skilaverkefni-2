# SKILAVERKEFNI 2 TEST
# Ragnar Helgi B. Unnþórsson

from skilaverkefni_02_foll import *
from colorama import init, Fore
from time import sleep

init(autoreset=True)
line = f"{Fore.BLUE}\n>>>>>><<<<<<\n"

while True:
    print("1 - langhlið\n"
          "2 - margfeldi af\n"
          "3 - ferningur úr stjornum\n"
          "4 - er slétt tala\n"
          "5 - flatarmal hrings\n"
          "6 - bank bank\n"
          "7 - STOP\n")
    try:
        V = int(input("Input: "))
        print(line)
        if V == 1:
            try:
                print(langhlid(int(input("A: ")), int(input("B: "))))
            except:
                print("FOOOOOOOOL!")
            finally:
                print(line)

        elif V == 2:
            try:
                if margfeldi_af(int(input("X: ")), int(input("Y: "))):
                    print("TRUE")
                else:
                    print("FALSE")
            except ValueError:
                print("prump")
            finally:
                print(line)

        elif V == 3:
            try:
                ferning_ur_stjornum(int(input("Magn af sjörnum: ")))
            except:
                print("errpooor")
            finally:
                print(line)

        elif V == 4:
            try:
                ebix = int(input("Tala: "))
                if er_slett_tala(ebix):
                    print(f"talan {str(ebix)} er slétt")
                else:
                    print(f"talan {str(ebix)} er óslétt")
            except:
                print("WROOONG!")
            finally:
                print(line)

        elif V == 5:
            try:
                print(flatarmal_hrings(int(input("flatarmal: "))))
            except:
                print("FAILMAN")
            finally:
                print(line)

        elif V == 6:
            try:
                bank_bank(int(input("Sekondur: ")))
            except:
                print("LOOOL")
            finally:
                print(line)

        elif V == 7: break

    except ValueError:
        print(line, "\nYOU FOOOL\n", line)