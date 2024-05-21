#!/bin/bash

rm info.txt
rm label.txt
rm info.json
rm printReadyLabel.png

./dataScrape.sh > info.txt

# Open FaceTime
open -a FaceTime
# Wait for 5 seconds
sleep 3
# Close FaceTime
killall FaceTime

./main

clear

echo "Printing label..."
cat label.txt