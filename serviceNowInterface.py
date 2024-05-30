import json
import requests
import subprocess

# Open the JSON file

with open('credentials.json') as auth:
    creds = json.loads(auth.read())

def insert_icn(icn, contents):
    print(contents)
    contents = contents[:-1] + f',"u_icn":"{icn}","name":"{icn}"' + "}"
    return contents

def device_exists(serial):
        # Set the request parameters
    url = f'https://byusandbox.service-now.com/api/now/table/u_cmdb_ci_computer_rental?sysparm_fields=u_icn&sysparm_limit=10&serial_number={serial}'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = creds['user']
    pwd = creds['pwd']

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
    user = creds['user']
    pwd = creds['pwd']

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=data)

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print("\nResponse:", data)

def fetch_record(serialNumber):
    url = f'https://byusandbox.service-now.com/api/now/table/u_cmdb_ci_computer_rental?sysparm_fields=u_icn,model_number,serial_number&sysparm_limit=10&serial_number={serialNumber}'

    user = creds['user']
    pwd = creds['pwd']

    headers = {"Content-Type":"application/json","Accept":"application/json"}

    response = requests.get(url, auth=(user, pwd), headers=headers)

    if response.status_code != 200:
        #print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    data = response.json()
    return data

def verifyRecords(data):
    if len(data['result']) > 1:
        print("The following records exist with the same serial number.\nYou need to manually go to ServiceNow and either delete or merge the duplicate records")
        for item in data['result']:
            print("------------------------------")
            for field in item:
                print("    " + field + " : " + item[field])            
        confirm = input("Enter y to acknowledge that you need to fix this problem that you might have made.\n>>> ")
        if confirm == "quit":
            return
        if confirm.lower() != 'y':
            subprocess.run(["clear"])
            verifyRecords(data)
    else:
        print("The following record exists in ServiceNow:")
        for item in data['result']:
            print("------------------------------")
            for field in item:
                print("    " + field + " : " + item[field])            
        
def updateServiceNow(data):

    with open('_internal/credentials.json') as auth:
        creds = json.loads(auth.read())

    if not device_exists(data['serial_number']):
        assetTag = input("Device not found in ServiceNow.\nEnter the asset tag/ICN exactly as it appears, including '-'\n>>> ")
        data['u_icn'] = assetTag
        json_data = json.dumps(data, indent = 4)
        print(json_data)
        create_record(json_data)
    else:
        print("Device already exists in ServiceNow.")
    result = fetch_record(data['serial_number'])
    verifyRecords(result)