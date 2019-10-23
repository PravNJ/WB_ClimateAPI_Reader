# The World Bank REST Climate API Reader

[The World Bank Climate API](https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api) is a REST API that provides historical and projected climate data by country using the [General Circulation Models](https://www.ipcc-data.org/guidelines/pages/gcm_guide.html) used by the Intergovernmental Panel on Climate Change - IPCC, 4th Assesment Report found [here](https://www.ipcc.ch/report/ar4/syr/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

The project is currently a simple python script that requires Python 3.7 

### Running

The inputs required to obtain data from the API can be modified in the main function as follows:

```
if __name__ == '__main__':
    querry_response = set_querry_url("mavg","tas","2020","2039","LKA","csv")
    download_formatted_data(querry_response)
```

The inputs to the function set_querry_url correspond to the inputs of the GET method used by the REST API to acccess the data based on the following [pattern](https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api).

For example, to obtain the annual average temperature in Celsius, for the forecasted period 2020 -2039 for Sri Lanka the script can be modifed as follows:

```
if __name__ == '__main__':
    querry_response = set_querry_url("annualavg","tas","2020","2039","LKA","csv")
    download_formatted_data(querry_response)
```
The final term, "csv" is required and will write the data directly to a csv file. Currently the script supports JSON and CSV. 



On Linux and Mac the script wb_climateapi_reader.py can be run be evoking Python as:

```
<directory>python wb_climateapi_reader.py
```

On Windows, Powershell can be used to run the script as follows:

```
<path of python 3.7>python.exe "<file path>world_bank_climate_reader.py"
```

## Authors

* **Praveen Jayasuriya** - *Initial work* - [praveenjayasuriya.com](https://praveenjayasuriya.com)

## License

This project is licensed under the MIT License

