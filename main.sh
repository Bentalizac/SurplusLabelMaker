#!/bin/bash

rm info.txt
rm label.txt
rm info.json
rm printReadyLabel.png

./dataScrape.sh > info.txt


#./main
python3 main.py

clear

echo "Printing label..."
cat label.txt