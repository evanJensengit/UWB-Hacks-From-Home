# Covid-19 Business Trip Planner

## Goals of the Project:
Create a website to allow users to easily plan business trips around the U.S. by having details of flights, restaurants, hotels and vaccine distribution centers all on the businesstripplanner website. 
We also combined features of helping to understand the current ongoing covid-19 cases in the designated areas, as well as areas for vaccine distribution sites that may be necessary prior from traveling. 
As a result, the goal of our project is to inform the covid-19 situations (and vaccine distribution sites) for our users who are flying across states and offering recommended resources available around them.

***
## Desired User Experience
* Ease-of-use control and navigation for the website
* Organized information details for listed resources


***
## Implementation Details
**Front-end**

*Tools Used*
* Figma


**Back-end**

*Tools Used*
* Azure - hosted website in the cloud to be publicly accesseble on Microsoft Azure 
* using their PaaS tools Resource groups and App services 
* VisualStudio
* Flask stack
* Amadeus API  

***
## Issues Encountered
**Bugs Fixed**
* Issue: had problem of getting data from Ardeus API 
* Solution: used SDK on Ardeus GitHub that specified how to get data from their API

* Issue: how to get relevant information from the text pulled from Ardeus API on hotels, flights and restaurants 
* Solution: Python would read in the text from Ardeus API as a dictionary data type which could be searched through using string matching with keys to obtain relevant information

* Issue: displaying relevant information in a consumable format
* Solution: using Flask framework to implement backend logic with python integrated with HTML/CSS


**Future Work to be Done**
* implement ML feature of showing the probability of user getting covid if they travel to city

