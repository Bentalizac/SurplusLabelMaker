import re
import platform
import time
import xml.etree.ElementTree as ET
import json
# Read the text file

with open('info.txt', 'r') as file:
    text = file.read()

info = text.split('\n')
cpuInfo = info[0].split()
ramInfo = info[1]
diskInfo = info[2]
serialNumber = info[3]
xml = info[4]

def getStorage(diskInfo):
    number, characters = re.match(r'(\d+)(\D+)', diskInfo).groups()
    if characters == "Gi":
        characters = "GB"
    elif characters == "Ti":
        characters = "GB"
        number = int(number) * 1000
    return str(number) + " " + characters


def get_MacOs_Name():
    MacOs_names = {'16': 'Sierra', '17': 'High Sierra', '18': 'Mojave', '19': 'Catalina (10.15)', '20':'Big Sur (11.0)', '21':'Monterey (12)', '22':'Ventura (13)', '23':'Sonoma (14)'}
    darwin_Ver = platform.release()
    darwin_Rel = darwin_Ver.split('.')[0]
    return MacOs_names[darwin_Rel]

def parseXML(xml):
    xml_tree = ET.ElementTree(ET.fromstring(xml))
    model_name = xml_tree.find('.//configCode').text
    return model_name

def getYear(model_name):
        # Regular expression pattern to match the year in the format "(YYYY)" or "YYYY)"
    pattern = r'\(?(\d{4})\)?'
    match = re.search(pattern, model_name)
    if match:
        return match.group(1)
    else:
        return None

def getScreenSize(model_name):
    screen_size = model_name.split()[-2]
    return screen_size[1:-1]

def parseRAM(ramInfo):
    ram = ramInfo.split()
    if ram[1] == "GB":
        ram[0] = int(float(ram[0])) * 1000
    return str(ram[0])

def parseCPUSpeed(cpuInfo):
    number, characters = re.match(r'(\d+)(\D+)', cpuInfo).groups()
    if characters == "GHz":
        characters = "MHz"
        number = int(number) * 1000
    return str(number)

def getCategory(model_name):
    if 'ook' in model_name:
        return "macLaptop"
    elif 'iMac' in model_name:
        return "macDesktop"
    elif 'mini' in model_name:
        return "macDesktop"

def buildJSON():
    data = {}
    data["model_number"] = parseXML(xml)
    data['os'] = get_MacOs_Name()
    data['u_year'] = getYear(parseXML(xml))
    data['serial_number'] = serialNumber
    data['u_monitor_size'] = getScreenSize(parseXML(xml)).split("-")[0]
    data['u_processor_type'] = cpuInfo[2].split("-")[0]
    data["processor_generation"] = cpuInfo[2].split("-")[1]
    data['cpu_speed'] = parseCPUSpeed(cpuInfo[-1])
    data['ram'] = parseRAM(ramInfo)
    data['disk_space'] = getStorage(diskInfo)
    #data['date'] = time.strftime("%m/%d/%Y") Removed for servicenow pickiness
    data['u_category'] = getCategory(parseXML(xml))
    data["u_device_name"] = "Rental-" + serialNumber
    data["manufacturer"] = "Apple"
    with open('info.json', 'w') as file:
        json.dump(data, file)

buildJSON()