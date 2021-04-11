import requests
import json
from amadeus import Client, ResponseError, Location
import datetime
from datetime import timedelta
from datetime import datetime, time

amadeus = Client(
        client_id='c53rrDvlC2Yn8FI8LUSPXsadNQEem0eP',
        client_secret='lJlC3bIQmL24AAZe'
    )

def findVacinationSiteFunc(state, zip_code):

    # https://www.vaccinespotter.org/api/

    state = state.upper()
    url = "https://www.vaccinespotter.org/api/v0/states/" + state + ".json"

    response = requests.get(url)
    
    if (response.status_code == 404):      # Request returns a 404 error
        return ""

    r_json = response.json() #gets data from json

    result = ""

    message = []

    #iterate through sites and find properties and postal code that match the user query
    
    for item in r_json['features']:
        if (item['properties']['postal_code'] == str(zip_code)):
            result += "Provider: " + item['properties']['provider_brand_name'] + "<br/>"
            result += "Address: " + item['properties']['address'] + "<br/>"
            result += "&emsp;&emsp;&emsp;" + item['properties']['city'] + ", " + item['properties']['state'] + " " + item['properties']['postal_code'] + "<br/>"
            result += "See more at " + item['properties']['url'] + "<br/><br/>"
            message.append(result)
            result = ""

    return message


def getCovidStatusFunc(state):

    # https://dev.socrata.com/foundry/data.cdc.gov/9mfq-cb36
    
    url = "https://data.cdc.gov/resource/9mfq-cb36.json"

    midnight = datetime.combine(datetime.today(), time.min)
    previous_2_days = midnight - timedelta(days=2)
    query_time = previous_2_days.isoformat()

    params = {
        '$$app_token': "Tmqrq0AclkLQKJplMYuNs2Opi",
        'submission_date': query_time,
        'state': str(state.upper())
        }

    r = requests.get(url, params = params)
    
    if (r.status_code == 404):      # Request returns a 404 error
        return "", "", ""

    if (r.json() == []):
        return "", "", ""

    r_json = r.json()[0]        # Get dictionary component of json

    # result = "Result at " + state.upper() + " state from " + previous_2_days.strftime("%Y-%m-%d %H:%M") + "\n"
    # result += "Total cases: " + r_json["tot_cases"] + "\n"
    # result += "New cases: " + r_json["new_case"] + "\n"

    date = previous_2_days.strftime("%Y-%m-%d %H:%M")

    return r_json["tot_cases"], r_json["new_case"], date


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
            result = code["address"]["cityCode"]
        return result

    except ResponseError as error:
        raise error


def getHotelsFunc(city, postal_code):
    try:
        theCityCode = city[0 : 3]
        # Get list of Hotels by city code
        hotels_by_city = amadeus.shopping.hotel_offers.get(cityCode=theCityCode, postalCode = postal_code)
        
        result = ""
        message = []
        #print(hotels_by_city.data)
        
        for items in hotels_by_city.data:
           # if items["hotel"]["address"]:
                #for addressItems in items["hotel"]["address"]:
                    #result += "Address: " + str(addressItems[0][0])
                    #result += str(addressItems[1][0]) + str(addressItems[2][0]) +"<br/>"
                    
            result += "Hotel Name: " + str(items['hotel']['name']) + "<br/>"
            
            result += "Address: " + str(items['hotel']['address']['lines'][0]) + " "
            result += str(items['hotel']['address']['cityName']) + " "
            result += str(items['hotel']['address']['stateCode']) + " "
            result += str(items['hotel']['address']['postalCode']) + "<br/>"
            
            result += "Rating: " + str(items['hotel']['rating']) + "<br/>"
            
            result += '<a href="' + str(items['hotel']['media'][0]['uri']) + '">Link</a>' + "<br/><br/>"

            message.append(result)
            result = ""
            
        return message
    
        #print(hotels_by_city.data)
    except ResponseError as error:
        print("oh hey")
        return ""
        # raise error
    # return result

def getRestaurants(code):
    zipcode = str(code)

    url = "https://api.documenu.com/v2/restaurants/zip_code/" + zipcode + "?key=1f3ce5158d4339dda48dc2ad0e051faa"

    r = requests.get(url)

    r_json = r.json()

    data = r_json["data"]
    result = ""
    message = []

    for res in data:
        result += "Restaurant name: " + str(res["restaurant_name"]) + "</br>"
        result += "Address: " + str(res["address"]["formatted"]) + "</br>"
        result += '<a href="' + str(res["restaurant_website"]) + '"' + ">Link</a>"
        message.append(result)
        result = ""
    return message
