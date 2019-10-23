import requests
import json
import csv
from io import StringIO

#Sets global base URL as per https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api

base_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country"

#Function that generates querry URL based on user requirements
def set_querry_url(measure_type,var_type,start_period,end_period,country_code,file_extension):
    querry_url = base_url+"/"+measure_type+"/"+var_type+"/"+start_period+"/"+end_period+"/"+country_code+"."+file_extension
    short_name = country_code+"_"+start_period+"_"+end_period+"_"+measure_type+"_"+var_type+"."+file_extension
    response = requests.get(querry_url)
    print("API Status Code:" + str(response.status_code))
    print(querry_url)
    return file_extension, short_name, response

#File downloader based on file format chosen by user during querry setup in set_querry_url   
def download_formatted_data(querry_response):
    if querry_response[0] == "json":
        json_data = querry_response[2].json()      
        with open(querry_response[1]+".json", 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
    else: 
        querry_response[0] == "csv"
        csv_data = querry_response[2].text
        csv_data_SIO = StringIO(csv_data)
        with open(querry_response[1]+".csv", 'w') as csv_file:
            for line in csv_data_SIO:
                csv_file.write(line)
    return True

if __name__ == '__main__':
    querry_response = set_querry_url("mavg","tas","2020","2039","LKA","csv")
    download_formatted_data(querry_response)
    