import subprocess
import time


from infoParse import parseInfo
from txtToPng import convert
from labelBuilder import build_label
from directPrint import printLabel

"""

This script runs all the pieces of Python code. It is OS-specific, so if you're looking at this code, this only works on Macs, and currently I don't know if it works on Apple Silicon

"""


def cameraCheck(): 
    subprocess.run(["open", "-a", "Facetime"], capture_output=True, text=True)
    time.sleep(3)
    subprocess.run(["killall", "FaceTime"])

def menu():
    while True:
        print("""
              Options:\n
              1: Print label\n
              2: Inventory via ServiceNow \n
              3: Print label AND inventory\n 
              q: Quit
              """)
        choice = input(">>>")
        if choice == "1":
            printLabel()
            cameraCheck()

        elif choice == "2":
            print("INVENTORY NOT IMPLEMENTED")
            # TODO rebuild inventory script

        elif choice == "3":
            printLabel()
            cameraCheck()
            print("INVENTORY NOT IMPLEMENTED")
            # TODO rebuild inventory script

        elif choice.lower() == "q":
            break


def main():
    parseInfo("info.txt", "info.json")
    build_label("info.json", "label.txt")
    convert("label.txt", "printReadyLabel.png")

    menu()

main()