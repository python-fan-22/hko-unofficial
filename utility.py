import requests
import json

districts = [
    'Central & Western District',
    'Eastern District',
    'Kwai Tsing',
    'Islands District',
    'North District',
    'Sai Kung',
    'Sha Tin',
    'Southern District',
    'Tai Po',
    'Tsuen Wan',
    'Tuen Mun',
    'Wan Chai',
    'Yuen Long',
    'Yau Tsim Mong',
    'Sham Shui Po',
    'Kowloon City',
    'Wong Tai Sin',
    'Kwun Tong'
]


def query_district():
    for i in districts:
        print(i)


def take_input():
    command = input(">")
    return command


def current_temp(district):
    url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
    if district in districts:
        request = requests.get(url)
        weather_data = json.loads(request.text)
        temperature_dict = []
        for item in weather_data['rainfall']['data']:
            temporary_dict = {'place': item['place'], 'temperature': item['max']}
            temperature_dict.append(temporary_dict)
            district_temp = temperature_dict[district]
            return district_temp
        else:
            print("error: how did this break!?")
    else:
        print('error: district not found :(. try, "district-list" for a list of all valid districts')


def download(file_name):
    url = r"https://raw.githubusercontent.com/python-fan-22/hko-unofficial/main/" + file_name
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode("utf-8")
        return content
