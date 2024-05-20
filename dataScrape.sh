#!/bin/bash

sysctl -n machdep.cpu.brand_string

# Function to get RAM size
get_ram() {
  sysctl -n hw.memsize | awk '{size=$1/1024/1024/1024; printf "%.2f GB\n", size}'
}

# Function to get available storage
get_total_storage() {
  df -h / | awk 'NR==2{print $2}'
}

full_serial=$(system_profiler SPHardwareDataType | awk '/Serial/ {print $4}')
# Get the last 4 characters of the serial number
short_serial=$(echo "$full_serial" | tail -c 5)

# Construct the URL with the serial number
url="https://support-sp.apple.com/sp/product?cc=$short_serial&lang=en_US"

# Call the functions
get_ram
get_total_storage
echo $full_serial
curl -o - "$url"


# Open FaceTime
open -a FaceTime

# Wait for 5 seconds
sleep 3

# Close FaceTime
killall FaceTime

python3 infoParse.py
python3 labelBuilder.py
python3 txtToPng.py

cat label.txt

# Prompt the user to print label
read -p "Do you want to print a label? (y/n): " print_label

if [[ $print_label == "y" ]]; then
    export BROTHER_QL_PRINTER=tcp://192.168.0.43
    export BROTHER_QL_MODEL=QL-710W
    brother_ql print -l 29 -r 90 printReadyLabel.png
fi