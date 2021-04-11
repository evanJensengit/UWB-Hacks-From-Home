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

        return render_template("vaccination-sites.html", message=result, showSites=True)

    return render_template("vaccination-sites.html")

#@app.route('/covid-stat', methods=["POST", "GET"])
#def getCovidStat():
    #if request.method == "POST":

        # input = request.form["input"]

        #result = func.getCovidStatusFunc()

        #message = "Status: " + str(result)

        #return render_template("index.html", stat=str(message), showStat=True)      

@app.route('/flights', methods=["POST", "GET"])
def getFlights():

    if request.method == "POST":

        # input = request.form["input"]

        result = func.getFlightFunc()

        message = "Status: " + str(result)

        return render_template("index.html", flights=str(message), showFlights=True)


@app.route('/places', methods=["POST", "GET"])
def findPlaces():

    if request.method == "POST":
        
        theCity = request.form["city"] #is this correct way to do it?
        thePostalCode = request.form["postalCode"]
        
        if ((not theCity) or (not thePostalCode)):
            return render_template("places.html")
        
        result = func.getHotelsFunc(theCity, thePostalCode)

        return render_template("index.html", hotels=message, showHotels=True)
    
    return render_template("places.html")


if __name__ == '__main__':
   app.run(debug = True)