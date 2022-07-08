import requests
import pprint
import pandas as pd
import csv

geo_radius = "Any Distance"

url = f"https://www.hertzcarsales.com/apis/widget/INVENTORY_LISTING_GRID_AUTO_ALL:inventory-data-bus1/getInventory?compositeType=certified%2C%20Rent2Buy&geoZip=73301&geoRadius={geo_radius}&start=36"

headers = {
      'Cookie': 'DDC.postalCode=73301; JSESSIONID=2EB15E68E97C67A2BD8F6CE8C4CEB1CC; locale=en_US'
}

response = requests.request("GET", url, headers=headers).json()

for car in response["pageInfo"]["trackingData"]:
    asking_price = car["askingPrice"]
    doors = car["doors"]
    city_fuel_efficiency = car["cityFuelEfficiency"]
    miles = car["odometer"]

    header = ["Price", "Doors", "Fuel Efficiency", "Miles"]
    data = [asking_price, doors, city_fuel_efficiency, miles]

    with open("Car_Data_v2.csv", "a+", newline = "", encoding = "UTF-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)

#read the csv in, turn the doors column to the number of doors and not a string, run a regression model to predict the price.
        
