from flask import Flask, render_template, redirect, url_for, request
import func

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('intro.html')

@app.route('/vaccination-sites', methods=["POST", "GET"])
def findVaccinationSites():
    if request.method == "POST":

        state = request.form["state"]
        zip_code = request.form["zip_code"]

        result = func.findVacinationSiteFunc(state, zip_code)

        if (result==""):         # if no info is found
            noResult = True
            showSites = False
        else:                   # information found
            noResult = False
            showSites = True

        return render_template("vaccination-sites.html", message=result, showSites=showSites, noResult=noResult)

    return render_template("vaccination-sites.html")

@app.route('/covid-stat', methods=["POST", "GET"])
def getCovidStat():
    if request.method == "POST":

        state = request.form["state"]
        print("in app, state = " + state)
        total, new, date = func.getCovidStatusFunc(state)

        if (total==""):         # if no info is found
            noResult = True
            showStat = False
        else:                   # information found
            noResult = False
            showStat = True

        return render_template("covid-stat.html", totalCases=total, newCases=new, date=date, showStat=showStat, noResult=noResult)    

    return render_template("covid-stat.html")


@app.route('/flights', methods=["POST", "GET"])
def getFlights():

    if request.method == "POST":

        # input = request.form["input"]
        
        departCity = request.form["depart"]
        destCity = request.form["dest"]
      
        departCityCode = func.getCityCode(departCity)
        destCityCode = func.getCityCode(destCity)
        

        result = func.getCheapestFlight(departCityCode, destCityCode)
         
        if (result==""):         # if no info is found
            noResult = True
            showFlights = False
        else:                   # information found
            noResult = False
            showFlights = True
        message = "Status: " + str(result)

        return render_template("flights.html", flights=result, showFlights=True)
    return render_template("flights.html")

@app.route('/hotels', methods=["POST", "GET"])
def findPlaces():
    if request.method == "POST":
        
        theCity = request.form["city"]
        thePostalCode = request.form["zip_code"]

        # to display when no hotel is found
        input = theCity + " city at zip code" + thePostalCode
        
        # if ((not theCity) or (not thePostalCode)):
        #     return render_template("places.html")
        
        result = func.getHotelsFunc(theCity, thePostalCode)

        if (result==""):         # if no info is found
            noResult = True
            showHotels = False
        else:                   # information found
            noResult = False
            showHotels = True

        return render_template("hotels.html", hotels=result, showHotels=showHotels, noResult=noResult, input=input)
    
    return render_template("hotels.html")

@app.route('/rest', methods=["POST", "GET"])
def findRest():
    if request.method == "POST":
        thePostalCode = request.form["zip_code"]

        # to display when no hotel is found
        input = "zip code" + thePostalCode
        
        # if ((not theCity) or (not thePostalCode)):
        #     return render_template("places.html")
        
        result = func.getRestaurants(thePostalCode)
        print(result)

        if (result==""):         # if no info is found
            noResult = True
            showRes = False
        else:                   # information found
            noResult = False
            showRes = True

        return render_template("rest.html", res=result, showRes=showRes, noResult=noResult, input=input)
    
    return render_template("rest.html")


if __name__ == '__main__':
   app.run(debug = True)