
import json
import time

def build_label(inputJSON):


    data = inputJSON
    # 'data' now contains the contents of the JSON file as a dictionary
    print(data)

    def build_line_one(data):
        os = data['os'].split()[0]

        cpu_info = data["u_processor_type"] + "-" 
        cpu_info += data["processor_generation"] + " " +data["cpu_speed"] + " GHz"
        return os + " " + cpu_info + "\n"

    def build_line_two(data):
        ram = str(float(data["ram"])/1000) + "GB"
        storage = data["disk_space"]
        return "RAM: " + ram + " \nStorage: " + storage + "\n"

    def build_line_three(data):
        return "B: [   ] W: [   ] C: [   ]\n"

    def build_line_four():
        return "R4R: " +  time.strftime("%m/%d/%Y") + "\n"

    def make_label(data):
        return build_line_one(data) + build_line_two(data) +  build_line_three(data) + build_line_four()

    print(make_label(data))

    return make_label(data)