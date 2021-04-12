# Covid-19 Business Trip Planner
Visit our website at http://businesstripfinder.azurewebsites.net/.<br/>

This is a project for the <a href="https://uwbhacks-from-home.devpost.com/">UWB Hacks From Home</a> - the fourth annual (and second virtual!) hackathon at the University of Washington, Bothell. You can find more details about our site at <a href="https://devpost.com/software/business-trip-planner.">Devpost.</a><br/>

Check out the demo video of our website: https://www.youtube.com/watch?v=lTEepG5xxQY.


## Goals of the Project:
Our website allows users to easily plan business trips around the U.S. by having details of flights, restaurants, and hotels. We also combined features of helping to understand the current ongoing COVID-19 cases in the designated areas, as well as areas for vaccine distribution sites that may be necessary prior from traveling. As a result, the goal of our project is to inform the COVID-19 situations (and vaccine distribution sites) for our users who are flying across states and offering recommended resources available around them.

***
## Desired User Experience
* Ease-of-use control and navigation for the website
* Organized information details for listed resources


***
## Implementation Details
**Front-end**
We came up with the design and created the wireframes for every page using Figma. We then utilized HTML, CSS, and JavaScript to build our website.

**Back-end**
*Azure - hosted website in the cloud to be publicly accessible on Microsoft Azure
*Python - the main programming language
*Flask - web application framework
*Using their PaaS tools Resource groups and App services
*APIs: CDC, Amadeus, Documenu

***
## Issues Encountered
**Bugs Fixed**
* Issue: had problem of getting data from Ardeus API 
* Solution: used SDK on Ardeus GitHub that specified how to get data from their API

* Issue: how to get relevant information from the text pulled from Ardeus API on hotels, flights and restaurants 
* Solution: Python would read in the text from Ardeus API as a dictionary data type which could be searched through using string matching with keys to obtain relevant information

* Issue: displaying relevant information in a consumable format
* Solution: using Flask framework to implement backend logic with python integrated with HTML/CSS

* Issue: trouble with preprocessing CDC covid data
* Solution: to create appropriate class labels so that Naive Bayes model can predict class

**Future Work to be Done**
* Finish implementing Naive Bayes model for estimating COVID infection given being in a state
