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
        print("Options:\n1: Print label\n2: Inventory via ServiceNow \n3: Print label AND inventory")
        choice = input("\n>>>")
        if choice == "1":
            printLabel()
            cameraCheck()
        elif choice == "2":
            ... #TODO finish rebuilding inventory script.

        elif choice == "3":
            printLabel()
            cameraCheck()

            # TODO rebuild inventory script


def main():

    cameraCheck()

    parseInfo("info.txt", "info.json")
    build_label("info.json", "label.txt")
    convert("label.txt", "printReadyLabel.png")

    printFlag = input("Would you like to print a label? (y/n)\n")
    if printFlag.lower() == "y":
    #    printLabel()
        ...
main()