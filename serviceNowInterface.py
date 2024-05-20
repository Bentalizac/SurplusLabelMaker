import json
import requests

# Open the JSON file
with open('info.json') as file:
    # Load the JSON data into a dictionary
    
    contents = file.read()
    data = json.loads(contents)

# Access the dictionary values
print(data)

def insert_icn(icn, contents):
    contents = contents[:-1] + f',"u_icn":"{icn}","name":"{icn}"' + "}"
    return contents

def device_exists(serial):
        # Set the request parameters
    url = f'https://byusandbox.service-now.com/api/now/table/u_cmdb_ci_computer_rental?sysparm_fields=u_icn&sysparm_limit=10&serial_number={serial}'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'comprental-ws'
    pwd = 'DD10rental'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers )

    # Check for HTTP codes other than 200
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    if len(data['result']) == 0:
        return False
    else:
        return True
    

def create_record(data):
        # Set the request parameters
    url = 'https://byusandbox.service-now.com/api/now/table/u_cmdb_ci_computer_rental?sysparm_fields=u_icn'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'comprental-ws'
    pwd = 'DD10rental'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=data)

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print("\nResponse:", data)

def fetch_record(serialNumber):
    url = f'https://byusandbox.service-now.com/api/now/table/u_cmdb_ci_computer_rental?sysparm_fields=u_icn,model_number&sysparm_limit=10&serial_number={serialNumber}'

    user = 'comprental-ws'
    pwd = 'DD10rental'

    headers = {"Content-Type":"application/json","Accept":"application/json"}

    response = requests.get(url, auth=(user, pwd), headers=headers)

    if response.status_code != 200:
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    data = response.json()
    return data

def parseJSON(data):
    #data = data['result'][0]
    records = []
    for item in data:
        
    return records

def run():
    print(fetch_record(data['serial_number']))
    if not device_exists("oompaLoompa"):
        assetTag = input("Device not found in ServiceNow.\nEnter the asset tag/ICN exactly as it appears, including '-'\n>>> ")
        data['u_icn'] = assetTag
        create_record(insert_icn(assetTag, contents))

    print("FETCHED: ", parseJSON(fetch_record(data['serial_number'])))
    

run()
