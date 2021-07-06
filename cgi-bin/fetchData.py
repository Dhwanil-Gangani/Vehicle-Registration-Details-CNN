#!/usr/bin/python3

import cgi
import requests
import xmltodict
import json

print("content-type: text/html")
print()



data = cgi.FieldStorage()
plate_number = data.getvalue("plate_number")

def get_vehicle_info(plate_number):
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=ridham1".format(str(plate_number)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1


plate_number_data = get_vehicle_info(plate_number)

print("Owner Information        : ",plate_number_data["Owner"])
print("Model                    : ",plate_number_data["CarModel"]["CurrentTextValue"])
print("Company Name             : ",plate_number_data["CarMake"]["CurrentTextValue"])
print("Registration Year        : ",plate_number_data["RegistrationYear"])
print("Insurance Till Date      : ",plate_number_data["Insurance"])
print("Engine Number            : ",plate_number_data["EngineNumber"])
print("Fuel Type                : ",plate_number_data["FuelType"]["CurrentTextValue"])
print("Identification Number    : ",plate_number_data["VechileIdentificationNumber"])
print("Registration Date        : ",plate_number_data["RegistrationDate"])
print("Fitness Till Date        : ",plate_number_data["Fitness"])
print("Registration Location    : ",plate_number_data["Location"])
