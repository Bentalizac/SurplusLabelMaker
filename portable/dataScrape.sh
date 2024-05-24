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