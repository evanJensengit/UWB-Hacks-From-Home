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
        return "No section found."

    r_json = r.json()[0]        # Get dictionary component of json

    result = "Result at WA state from " + previous_2_days.strftime("%Y-%m-%d %H:%M") + "\n"
    result += "Total cases: " + r_json["tot_cases"] + "\n"
    result += "New cases: " + r_json["new_case"] + "\n"

    print(result)

    return result

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