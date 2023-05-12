# Weather Impact on Crime Rates
An analysis of Crime Rates in the Greater Toronto Area with regard to the impact weather has on crime rates.

## Project Overview
Can weather be used to predict crime rates? Are changing weather patterns affecting crime rates?  
 
Weather plays a role in our daily lives, it shapes our choices and behaviors affecting when, where and how we choose to carry out our daily activities. Studies into the impact of weather on crime have been going on for decades but what about here and now? Forbes recently published an article “A Different Heatwave Warning: Online Hate—Like Violent Crime—Soars With High Temperatures”.   
We are taking a look at Toronto Crime rates from 2015 to 2018 to see if changes in weather have affected crime rates.

Outcome:  Can we predict higher precedence of crime based on weather forecasts?  Can Police Services use weather to predict higher staffing levels, increased surveillance in high crime areas based on the weather forecast?  If our climate is experiencing changes will these changes affect the long term police services needs and budget?

### Project Question
The purpose of this project is to analyze data to answer the following question:<br>
***Can changes in weather affect crime rates?***

### Outcome
Can we predict higher precedence of crime based on weather forecasts?  Provide Police services an interactive resource that can be used to evaluate the effect of weather on crime trends. Can Police Services use weather to predict higher staffing levels, increased surveillance in high crime areas based on the weather forecast?  If our climate is experiencing changes will these changes affect the long term police services needs and budget?

### Technologies

- Python
- Jupyter Notebooks
- Database (PostgreSQL), SQLAlchemy
- Machine Learning - Linear Regression model(s)
- Neural Networks, Keras
- Tableau

### Data Set - Initial Raw Data  (num of rows, size, )

#### Source Data

1. **Crime Data** 
The crime data used in this project comes from [The Toronto Police Service Data Catalogue](https://data.torontopolice.on.ca/pages/catalogue).

The data sets are: 
* Assault_Open_Data.csv
* Auto_Theft_Open_Data.csv
* Bicycle_Thefts_Open_Data.csv
* Break_and_Enter_Open_Data.csv
* Homicides_Open_Data_ASR_RC_TBL_002.csv
* Robbery_Open_Data.csv
* Shooting_and_Firearm_Discharges_Open_Data.csv
* Theft_From_Motor_Vehicle_Open_Data.csv
* Theft_Over_Open_Data.csv
* Traffic_Collisions_(ASR-T-TBL-001).csv

This data contained information in which was considered interesting to this project:
* EVENT_UNIQUE_ID
* OCC_DATE (***OCC** = Occurrence*)
* OCC_YEAR
* OCC_MONTH
* OCC_DAY
* OCC_DOW
* OCC_HOUR
* PREMISES_TYPE
* MCI_CATEGORY (***MCI** = Major Crime Indicators*)
* HOOD_140 (*This refers to the 140 neighbourhood division of Toronto*)
* NEIGHBOURHOOD_140 (*This refers to the 140 neighbourhood division of Toronto*)
* LONG_WGS84 (*Longitude*)
* LAT_WGS84 (*Latitude*)

2. **Weather Data:** The weather data used in this project comes from [toronto.weatherstats.com](https://toronto.weatherstats.ca/download.html).

weatherstats.com [quote](https://www.weatherstats.ca/faq/#data-source): *Data is collected over time from Environment and Climate Change Canada and from the Citizen Weather Observer Program (CWOP). Every individual location web site has several links on the "about page" so you can see where the information came from.*


### Data Set - Data Cleaning
* Cleaned Data files can be found here: [cleaned_data_2015_2018](https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/tree/main/cleaned_data_2015_2018)

### Data Exploration
https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/tree/main/Project_Notebooks/Data_Exploration

Crime dataset: 
The cleaned crime dataset has 480, 903 rows and 12 columns. There are 10 different crime types with traffic collisions comprising 60% of the dataset. 

<img width="500" height="400" alt="crimetypes" src="https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/assets/113721712/d1c81908-76a1-4cb0-a5e6-f5d3126e4347">

Since weather obviously has an impact on traffic collisions, we decided to remove this crime type from the analysis. 

We also see that crime is slightly increasing over time, pointing to a need to figure out how to reduce crime and prevent further increases. 

<img width="500" height="400" alt="crimeovertime" src="https://raw.githubusercontent.com/MickMarch/Weather_Impact_On_Crime_Rates/tash_update_readme/Doc_Assets/crimeovertime.png">

There are no null values within the dataset except for 1,811 rows (0.38% of the dataset) with no premise type (this is where the crime took place, i.e. an apartment, outside, etc). 

Weather dataset: 
There are 1,461 rows and 13 columns. This includes the date, max temp, min temp, max humidity, avg humidity, avg sea pressure, max wind speed, precipitation, rain, snow, snow on ground, daylight and avg cloud cover. During this time period, the max temperature in Toronto was 36 degrees and the min temperature was -26.3 degrees. 

### Data Pre-Processing


### Machine Learning 



### Neural Network Modelling

### Visualizations 
 https://public.tableau.com/app/profile/nitasha.gill/viz/Crime_Weather_16836768522530/CrimeDash?publish=yes





## Project Roles and Activities

* Focus areas:
    * Data cleaning - Michael 
    * Data base PostgreSQL - Susan
    * Visualization and data exploration - Nitasha
  
* Communication Protocols:
- branch management
- additional team meetings (MS Teams)
- Slack group
- Task management spreadsheet
- Each one owns tasks and updates status as task and deliverable are completed




### Segment 1 Deliverables
* Presentation      - mock-ups, README
* GitHub            - complete, branching in progress
* Machine Learning  - Data exploration
* Machine Learning models mock-up - [Model(s) Mock-up](https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/tree/main/NN_Model)
* Database          - [Postgress Mock-up](https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/tree/main/PosgreSQL)
    * [ERD Mock-up](https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/blob/main/PosgreSQL/ERD_mockup_Segment1.png)
* Dashboard         - [Dashboard Mock-up](https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/blob/main/Dashboard_Mockup.pptx)<br>
    ![Dashboard mock-up](Doc_Assets/Dashboard_Mockup.png)
    

