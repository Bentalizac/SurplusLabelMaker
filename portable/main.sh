#!/bin/bash

rm info.txt
rm label.txt
rm info.json
rm printReadyLabel.png

./dataScrape.sh > info.txt


#./menu
python3 menu.py

clear
