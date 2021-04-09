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

    r_json = response.json() #gets data from json

    result = ""

    #iterate through sites and find properties and postal code that match the user query
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

def getCheapestFlight():
    try:
        '''
        Find cheapest dates from city to city.
        '''
        response = amadeus.shopping.flight_dates.get(origin='MAD', destination='MUC')
        for flight in response.data: 
            print("Departure date: " + flight["departureDate"])
            print("Return date: " + flight["returnDate"])
            print("Price: " + flight["price"]["total"])
    except ResponseError as error:
        raise error

def getCityCode():
    try:
        '''
        Return city code.
        '''
        response = amadeus.reference_data.locations.get(keyword='London',
                                                    subType=Location.CITY)
        for code in response.data:
            print("Name: " + code["address"]["cityName"])
            print("City code: " + code["address"]["cityCode"])
    except ResponseError as error:
        raise error


def getHotelsFunc():
    try:
        # Get list of Hotels by city code
        hotels_by_city = amadeus.shopping.hotel_offers.get(cityCode='PAR')
        print(hotels_by_city.data)
    except ResponseError as error:
        raise error
    
    return "incomplete"