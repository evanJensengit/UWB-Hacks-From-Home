import requests
import json
import func
from amadeus import Client, ResponseError
# from amadeus import Client, ResponseError

def main():
    # findVacinationSiteFunc("WA", 98144)
    # testAmadeus()
    # func.getCheapestFlight("SEA", "LAX")
    # func.getCityCode('Los Angeles')
    func.getRestaurants(47.44889, -122.3094, 10)
    func.getCovidStatusFunc("WA")

def testAmadeus():
    amadeus = Client(
        client_id='C9uBehZwr9GRWCwz0eNF0TSMHn1hVv2x',
        client_secret='gLkTCL8V32aLUOdV'
    )

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode='SYD',
            destinationLocationCode='BKK',
            departureDate='2021-04-01',
            adults=1)
        print(response.json())
    except ResponseError as error:
        print(error)

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
            result += "Provider: " + item['properties']['provider_brand_name'] + "<br/> \n"
            result += "Address: " + item['properties']['address'] + "<br/> \n"
            result += "See more at " + item['properties']['url'] + "<br/><br/> \n\n"

    print(result)

if __name__ == "__main__":
    # execute only if run as a script
    main()