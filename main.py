import csv
import requests


def load_data_from_csv():
    addresses = []
    with open ('csv.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            addresses.append(row[0])

    return addresses

def fetch_lat_lng(address):
    formatted_street_address = address.replace(" ", "+")
    url = str.format('https://maps.googleapis.com/maps/api/geocode/json?address={},+Swansea,+MA&key=AIzaSyC4eoP9c45aAZXyQmROqF9rph35HVStJH0', formatted_street_address)
    response = requests.get(url).json()
    latitude = response['results'][0]['geometry']['location']['lat']
    longitude = response['results'][0]['geometry']['location']['lng']
    
    return {'lat': latitude, 'lng': longitude}

def build_lat_lng_dict(address_list):
    lat_lng_dict = {}
    for address in address_list:
        lat_lng_dict[address] = fetch_lat_lng(address)
    
    return lat_lng_dict

def print_generated_html(lat_lng_dict):
    for x in lat_lng_dict:
        lat = lat_lng_dict[x]['lat']
        lng = lat_lng_dict[x]['lng']
        formatted_html_string = str.format("var marker = new google.maps.Marker({{position: {{lat:{}, lng:{}}}, map: map, title: '{}'}});", lat, lng, x)
        print(formatted_html_string)

def main():
    lat_lng_dict = build_lat_lng_dict(load_data_from_csv())
    print_generated_html(lat_lng_dict)
    

if __name__== "__main__":
    main()
