import brother_ql
# Example arguments, replace these with your actual values
printer_address = "tcp://192.168.0.43"
label_image_path = "printReadyLabel.png"

# Call the print_cmd function with the appropriate arguments
print_cmd(image=[open(label_image_path, 'rb')], printer=printer_address, label='29x90')
