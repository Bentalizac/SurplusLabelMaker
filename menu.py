import subprocess
import time


from infoParse import parseInfo
from txtToPng import convert
from labelBuilder import build_label
from directPrint import printLabel
from serviceNowInterface import updateServiceNow

"""

This script runs all the pieces of Python code. It is OS-specific, so if you're looking at this code, this only works on Macs, and currently I don't know if it works on Apple Silicon

"""


def cameraCheck(): 
    subprocess.run(["open", "-a", "Facetime"], capture_output=True, text=True)
    time.sleep(3)
    subprocess.run(["killall", "FaceTime"])

def printPreview(jsonInfo):
    labelString = build_label(jsonInfo)
    print(labelString)

def menu(jsonInfo):
    subprocess.run(["clear"])
    while True:
        print("""
Options:
1: Print label
2: Inventory via ServiceNow
3: Print label AND inventory
4: Preview label
q: Quit
              """)
        choice = input(">>>")
        if choice == "1":
            printLabel()
            cameraCheck()

        elif choice == "2":
            updateServiceNow(jsonInfo)

        elif choice == "3":
            printLabel()
            cameraCheck()
            updateServiceNow(jsonInfo)

        elif choice == "4":
            printPreview(jsonInfo)

        elif choice.lower() == "q":
            break
    subprocess.run(["clear"])

def main():

    # TODO fix whatever in here is throwing bugs about files not existing at the right times.

    jsonInfo = parseInfo("info.txt", "info.json")
    labelString = build_label(jsonInfo)
    convert(labelString, "printReadyLabel.png")
 
    menu(jsonInfo)

main()