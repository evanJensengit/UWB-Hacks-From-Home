import requests
import json
from amadeus import Client, ResponseError, Location

amadeus = Client(
        client_id='c53rrDvlC2Yn8FI8LUSPXsadNQEem0eP',
        client_secret='lJlC3bIQmL24AAZe'
    )

def findVacinationSiteFunc(state, zip_code):

    # https://www.vaccinespotter.org/api/

    url = "https://www.vaccinespotter.org/api/v0/states/" + state + ".json"

    response = requests.get(url)
    
    if (response.status_code == 404):      # Request returns a 404 error
        return "No section found."

    r_json = response.json()

    result = ""

    for item in r_json['features']:
        if (item['properties']['postal_code'] == str(zip_code)):
            result += "Provider: " + item['properties']['provider_brand_name'] + "<br/>"
            result += "Address: " + item['properties']['address'] + "<br/>"
            result += "&emsp;&emsp;&emsp;" + item['properties']['city'] + ", " + item['properties']['state'] + " " + item['properties']['postal_code'] + "<br/>"
            result += "See more at " + item['properties']['url'] + "<br/><br/>"

    return result


def getCovidStatusFunc():

    # https://covidtracking.com/data/api?

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/northamerica"

    headers = {
        'x-rapidapi-key': "03fdf0f62bmsh3bf01c57781f7e0p12f943jsnb2fe73b7d4b4",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
        }

    # response = requests.request("GET", url, headers=headers_str)

    r = requests.get(url, headers = headers)
    
    if (r.status_code == 404):      # Request returns a 404 error
        return "No section found."

    r_json = r.json()

    # parsed = json.loads(r_json)
    print(json.dumps(r_json, indent=3))

    result = json.dumps(r_json, indent=3)

    return result

def getFlightFunc():

    # https://aviationstack.com/documentation

    url = 'http://api.aviationstack.com/v1/flights'

    params = {
    'access_key': '6080d6c8612fe957573d69b0b0202675',
    'limit':'10'
    }

    api_result = requests.get(url, params)

    print(api_result)

    api_response = api_result.json()

    # for flight in api_response:
    #     if (flight['live']['is_ground'] is False):
    #         print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
    #             flight['airline']['name'],
    #             flight['flight']['iata'],
    #             flight['departure']['airport'],
    #             flight['departure']['iata'],
    #             flight['arrival']['airport'],
    #             flight['arrival']['iata']))

    # parsed = json.loads(r_json)
    # print(json.dumps(api_response, indent=3))

    # result = json.dumps(r_json, indent=3)

    return "Result"

def getCheapestFlight(depart, dest):
    try:
        '''
        Find cheapest dates from city to city.
        '''
        response = amadeus.shopping.flight_offers_search.get(originLocationCode=depart, destinationLocationCode=dest, departureDate='2021-04-10', returnDate='2021-04-18', adults=1, max=1)
        result = ""
        rangeFlight = len(response.data)
        for index in range(0, rangeFlight): 
            flight = response.data[index]
            data = flight["itineraries"]
            for item in data:
                segment = item["segments"][0]
                result += "Airline: " + segment["carrierCode"] + "<br/>"
                result += "From: " + segment["departure"]["iataCode"] + "<br/>"
                result += "Departure date: " + segment["departure"]["at"] + "<br/>"
                result += "To: " + segment["departure"]["iataCode"] + "<br/>"
                result += "Return date: " + segment["departure"]["at"] + "<br/>"
                result += "Airline: " + segment["carrierCode"] + "<br/>"
                result += "From: " + segment["departure"]["iataCode"] + "<br/>"
                result += "Departure date: " + segment["departure"]["at"] + "<br/>"
                result += "To: " + segment["departure"]["iataCode"] + "<br/>"
                result += "Return date: " + segment["departure"]["at"] + "<br/>"
                result += "-------------------------------"
        result += "Price: " + flight["price"]["total"]
        return result
    except ResponseError as error:
        raise error

def getCityCode(city):
    try:
        '''
        Return city code.
        '''
        response = amadeus.reference_data.locations.get(keyword=city,
                                                    subType=Location.CITY)
        result = ""
        for code in response.data:
            result += "Name: " + code["address"]["cityName"]
            result += "City code: " + code["address"]["cityCode"]
            result += code["geoCode"]["latitude"]
            result += code["geoCode"]["longitude"]
        return result
    except ResponseError as error:
        raise error

def getRestaurants(latitude, longitude, dist):
    lat = str(latitude)
    lon = str(longitude)
    distance = str(dist)

    url = "https://api.documenu.com/v2/restaurants/search/geo?lat=" + lat + "&lon=" + lon + "&distance=" + distance + "&key=1f3ce5158d4339dda48dc2ad0e051faa"

    header = {"x-api-key:" "1f3ce5158d4339dda48dc2ad0e051faa"}

    # params = {"lat": lat, "lon": long, "distance": 25 }

    r = requests.get(url)

    r_json = r.json()

    data = r_json["data"]
    result = ""

    for res in data:
        result += res["restaurant_name"]
        result += res["restaurant_website"]
        result += res["address"]["formatted"]
    print(r_json)
