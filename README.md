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

* Cleaned Data files can be found here: [cleaned_data_2015_2018](https://github.com/MickMarch/Weather_Impact_On_Crime_Rates/tree/main/cleaned_data_2015_2018)

* Source: Data has been sourced from the Toronto Police Service Data Catalogue. [cleaned_data_2015_2018](https://data.torontopolice.on.ca/pages/catalogue)
    * Source raw data can be found here: The exception is the Major Crimes CSV (over 100 M).  Download the file here : [Raw Data - Major Crimes Indicators](https://data.torontopolice.on.ca/datasets/TorontoPS::major-crime-indicators-open-data/about)


### Data Set - Data Cleaning

### Data Exploration


### Data Pre-Processing


### Machine Learning 
Initial investigation into machine learning delivered interesting insights into how different types of weather events effect different types of crime.  

For each Linear Regression model preprocessing of the data was performed.
* data pulled from PostgreSQL tables; All Crime table and Weather table
* 'crime' column was grouped by date and day of the week (occ_dow) and split into seperate columns containing the individual crime types, and crime events were totalal by type/date.
* crime data and weather data was merged into a single data set
     ![All Data Columns](Doc_Assets/MachineLearning/ml_total_dataset.png)
* each crime type was isolated and tested against the weather feature focused in the notebook. A scatter diagram, and correlation matrix was built for each crime type

### Linear Regression
Several Linear Regression notebooks were created targeting specific weather events; 
- Max Temp (maximum temperfature during a given day), 
- Percipitation (includes rain or snow), 
- Pressure (average sea level pressure at the reading station), and 
- Snow on the Ground (snow accumulation).

<b>Precipitation :</b><br>
Although one might think initially that this would have a high effect on crime, it turned out the be the least of the 4 weather types.  Not surprisingly bicycle theft did have a significant decline as percipitation increased.  However the overall slope was negligable.<br>
![Precipitation Scatter](Doc_Assets/MachineLearning/ml_reg_precipitation.png)

<b>Air Pressure :</b><br>
It has been noted that on many levels changes in air pressure can effect the human body from the sounds we hear to our emotions such as irritability.  A lower air pressure has a consistent relation to an increase in certain types of crime.<br>
![Air Pressure](Doc_Assets/MachineLearning/ml_pressure.png)

<b>Higher Temperature :<b><br>
Temperature as well can effect the human condition.  High temperatures had the strongest effect on increases in crime.  <br>

![High Temperature](Doc_Assets/MachineLearning/ml_high_temp.png)

<b>Snow on the Ground :<b><br>
While precipitation itself didn't show a significant correlation accumulation of snow on the ground had a higher relationship to certain crimes.   <br>

![Snow accumulation](Doc_Assets/MachineLearning/ml_snow.png)

### <b>Correlation Matrix </b><br>
A correlation matrix was run in each of the weather feature Linear Regression notebooks by crime type.  Also a Correlation Matrix was run on groupings of crime types.<br>

<b>Bicycle theft, Theft from a motor vehicle and Theft Over:</b><br>
A clear picture shows a high correlation between max temperature and bicycle theft confirming that connection.  Also a correlation between max temp and theft from a motor vehicle.

![Correlattion - theft](Doc_Assets/MachineLearning/corr_bicycle_theft.png)

<b>Auto Theft, Brean and Enter, and Robbery:</b><br>
These type had a common correlation level between the key weather features.  Through the correlation matrix below and regression modelling these had consistenly higher relevance.

![Major Theft](Doc_Assets/MachineLearning/corr_autoTheft_BandE_robbery.png)

<b>Assault, Homicide and Shoortings:</b><br>
The correlation matrix shows some correlation to these more serious events with max temperature and assault having the highest correlation.  Homicide however consistently has a lower correlation and regression predictability and with shooting (firearms events)

![High Temperature](Doc_Assets/MachineLearning/corr_assault_homicide_shooting.png)

### Machine Learning Summary
Between the Linear Regression and Correlation matrices it was clear that certain types of crime did not have a clear correlation to weather.  Homicide for example was consistently flat in the linear regression and very low in the corrleation matrix. 

This machine learning analysis can be used to focus the Neural Network tuning to ensure a cleaner and more effective model.  There were 5 types of crime that were consistently higher in correleation:
* Thefts: Bicycle Theft, Theft from an Auto, Auto Theft, Robbery, Break and Enter.



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
    

