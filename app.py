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

        print(result)

        return render_template("vaccination-sites.html", message=result, showSites=True)

    return render_template("vaccination-sites.html")

@app.route('/covid-stat', methods=["POST", "GET"])
def getCovidStat():
    if request.method == "POST":

        state = request.form["state"]
        print("in app, state = " + state)
        total, new, date = func.getCovidStatusFunc(state)

        if (total==""):
            noResult = True
            showStat = False
        else:
            noResult = False
            showStat = True

        # message = "Status: " + str(result)
        # return render_template("index.html", stat=str(message), showStat=True)      

        return render_template("covid-stat.html", totalCases=total, newCases=new, date=date, showStat=showStat, noResult=noResult)    

    return render_template("covid-stat.html")


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

        print("hi")
        
        theCity = request.form["city"] #is this correct way to do it?
        thePostalCode = request.form["zip_code"]
        
        # if ((not theCity) or (not thePostalCode)):
        #     return render_template("places.html")
        
        result = func.getHotelsFunc(theCity, thePostalCode)

        return render_template("places.html", hotels=result, showHotels=True)
    
    return render_template("places.html")


if __name__ == '__main__':
   app.run(debug = True)