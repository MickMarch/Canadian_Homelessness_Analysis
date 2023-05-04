-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/dlKkBe
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


-- Columns common
-- Year, Month, Day, DayOfWeek are ll Occurance (OCC) values
-- For Premises Type, see legend using LOCATION_TYPE column descriptions
-- Offence detail (Offence) may be too much information, perhaps use "Offence_Category" only
-- Hoot158 is a code for each neighbourhood string, Hood148 is not included(odler version of categories)
CREATE TABLE"assult" (
    "Event_Unique_ID" varchar(18) NOT NULL,
    "OCC_Date" date NOT NULL,
    "Year" int NOT NULL,
    "Month" varchr(10) NOT NULL,
    "Day" int NOT NULL,
    "DayOfWeek" varchar(10) NOT NULL,
    "Hour"  int NOT NULL,
    "DayOfYear" int NOT NULL,
    "Police_Division" varchar(5) NOT NULL,
    "Premises_Type" varchar NOT NULL,
    "Offence" varchar NOT NULL,
    "Offence_Category" varchar NOT NULL,
    "Neighbourhood" varchar NOT NULL,
    "Hood158" varchar(5),
    "Long" int NOT NULL,
    "Lat" int NOT NUll,
    CONSTRAINT "pk_assults?" PRIMARY Key(
        "Year",
        "Month",
        "Day",
        "Hour"
    )
);

CREATE TABLE"assult" (
    "EVENT_UNIQUE_ID" varchar(18) NOT NULL,
    "OBJECTID" varchar NOT NULL,
    --"OCC_DATE" date NOT NULL,
    "OCC_YEAR" int NOT NULL,
    "OCC_MONTH" varchar(10) NOT NULL,
    "OCC_DAY" int NOT NULL,
    "OCC_HOUR"  int NOT NULL,
    "OCC_DOW" varchar(10) NOT NULL,
    "OCC_DOY" int NOT NULL,
    "DIVISION" varchar(5) NOT NULL,
    "PREMISES_TYPE" varchar NOT NULL,
    "MCI_CATEGORY" varchar NOT NULL,
    "OFFENCE" varchar NOT NULL,
    "NEIGHBOURHOOD_158" varchar NOT NULL,
    "HOOD_158" varchar(5),
    "LONG_WGS84" int NOT NULL,
    "LAT_WGS84" int NOT NUll,
    CONSTRAINT "pk_assults" PRIMARY Key(
        "OCC_YEAR",
        "OCC_MONTH",
        "OCC_DAY",
        "OCC_HOUR"
    )
);

CREATE TABLE"auto_theft" (
    "EVENT_UNIQUE_ID" varchar(18) NOT NULL,
    "OBJECTID" varchar NOT NULL,
    --"OCC_DATE" date NOT NULL,
    "OCC_YEAR" int NOT NULL,
    "OCC_MONTH" varchar(10) NOT NULL,
    "OCC_DAY" int NOT NULL,
    "OCC_HOUR"  int NOT NULL,
    "OCC_DOW" varchar(10) NOT NULL,
    "OCC_DOY" int NOT NULL,
    "DIVISION" varchar(5) NOT NULL,
    "PREMISES_TYPE" varchar NOT NULL,
    "MCI_CATEGORY" varchar NOT NULL,
    "OFFENCE" varchar NOT NULL,
    "NEIGHBOURHOOD_158" varchar NOT NULL,
    "HOOD_158" varchar(5),
    "LONG_WGS84" int NOT NULL,
    "LAT_WGS84" int NOT NUll,
    CONSTRAINT "pk_auto_theft" PRIMARY Key(
        "OCC_YEAR",
        "OCC_MONTH",
        "OCC_DAY",
        "OCC_HOUR"
    )
);

-- Remove columnsREPORT_MONTH
-- X, Y, REPORT_DATE, REPORT_YEAR, REPORT_MONTH, REPORT_DAY, 
-- REPORT_DOY, REPORT_DOW, REPORT_HOUR, LOCATION_TYPE, UCR_CODE, UCR_EXT
-- HOOD_140, NEIGHBOURHOOD_140



CREATE TABLE"weather" (
    "date_time_local" varchar(18) NOT NULL,
    "unixtime" int NOT NULL,
    "pressure_station" float NOT NULL,
    "pressure_sea" float NOT NULL,
    "wind_dir" varchar NOT NULL,
    "wind_speed" int NOT NULL,
    "relative_humidity" int NOT NULL,
    "dew_point"  int NOT NULL,
    "temperature" float NOT NULL,
    "windchill" int,
    "humidex" int,
    "visibility" int NOT NULL,
    "health_index" int,
    "cloud_cover_4" int,
    "cloud_cover_8" int NOT NULL,
    "max_air_temp_pst1hr" float NOT NULL,
    "min_air_temp_pst1hr" float NOT NULL,
    CONSTRAINT "pk_weather" PRIMARY Key(
        "date_time_local"
    )
);

-- Removed:  wind_gust, cloud_cover_4, cloud_cover_10, solar_radiation


-- For trial purposed I used
CREATE TABLE"auto_theft" (
    "EVENT_UNIQUE_ID" varchar(18),
    "OBJECTID" varchar,
    --"OCC_DATE" date,
    "OCC_YEAR" int,
    "OCC_MONTH" varchar(10),
    "OCC_DAY" int,
    "OCC_HOUR"  int,
    "OCC_DOW" varchar(10),
    "OCC_DOY" int,
    "DIVISION" varchar(5),
    "PREMISES_TYPE" varchar,
    "MCI_CATEGORY" varchar,
    "OFFENCE" varchar,
	"HOOD_158" varchar(5),
    "NEIGHBOURHOOD_158" varchar,
    "LONG_WGS84" varchar,
    "LAT_WGS84" varchar,
    CONSTRAINT "pk_auto_theft" PRIMARY Key(
		"EVENT_UNIQUE_ID"
    )
);

SELECT * FROM assault;

CREATE TABLE"auto_theft" (
    "EVENT_UNIQUE_ID" varchar(18),
    "OBJECTID" varchar,
    --"OCC_DATE" date ,
    "OCC_YEAR" int,
    "OCC_MONTH" varchar(10),
    "OCC_DAY" int NOT NULL,
    "OCC_HOUR"  int NOT NULL,
    "OCC_DOW" varchar(10) NOT NULL,
    "OCC_DOY" int NOT NULL,
    "DIVISION" varchar(5) NOT NULL,
    "PREMISES_TYPE" varchar NOT NULL,
    "MCI_CATEGORY" varchar NOT NULL,
    "OFFENCE" varchar NOT NULL,
    "NEIGHBOURHOOD_158" varchar NOT NULL,
    "HOOD_158" varchar(5),
    "LONG_WGS84" int NOT NULL,
    "LAT_WGS84" int NOT NUll,
    CONSTRAINT "pk_auto_theft" PRIMARY Key(
        "OCC_YEAR",
        "OCC_MONTH",
        "OCC_DAY",
        "OCC_HOUR"
    )
);



CREATE TABLE"weather" (
    "date_time_local" varchar(18),
    "unixtime" int,
    "pressure_station" float,
    "pressure_sea" float,
    "wind_dir" varchar,
    "wind_speed" int,
    "relative_humidity" int,
    "dew_point" int,
    "temperature" float,
    "windchill" int,
    "humidex" int,
    "visibility" int,
    "health_index" int,
    "cloud_cover_4" int,
    "cloud_cover_8" int,
    "max_air_temp_pst1hr" float,
    "min_air_temp_pst1hr" float,
    CONSTRAINT "pk_weather" PRIMARY Key(
        "date_time_local"
    )
);





-- Old Samples as a reference
--############################################







CREATE TABLE "category" (
    "category_id" varchar(10)   NOT NULL,
    "category_name" varchar(50)   NOT NULL,
    CONSTRAINT "pk_category" PRIMARY KEY (
        "category_id"
     )
);

CREATE TABLE "subcategory" (
    "subcategory_id" varchar(10)   NOT NULL,
    "subcategory_name" varchar(50)   NOT NULL,
    CONSTRAINT "pk_subcategory" PRIMARY KEY (
        "subcategory_id"
     )
);

CREATE TABLE "contacts" (
    "contact_id" int   NOT NULL,
    "first_name" varchar(50)   NOT NULL,
    "last_name" varchar(50)   NOT NULL,
    "email" varchar(100)   NOT NULL,
    CONSTRAINT "pk_contacts" PRIMARY KEY (
        "contact_id"
     )
);


ALTER TABLE "campaign" ADD CONSTRAINT "fk_campaign_contact_id" FOREIGN KEY("contact_id")
REFERENCES "contacts" ("contact_id");

ALTER TABLE "campaign" ADD CONSTRAINT "fk_campaign_category_id" FOREIGN KEY("category_id")
REFERENCES "category" ("category_id");

ALTER TABLE "campaign" ADD CONSTRAINT "fk_campaign_subcategory_id" FOREIGN KEY("subcategory_id")
REFERENCES "subcategory" ("subcategory_id");

SELECT * FROM contacts

SELECT * FROM subcategory

SELECT * FROM category

SELECT * FROM campaign


-- Module 8 Challenge
-- Create Backers schema
CREATE TABLE "backers" (
    "backer_id" varchar(5)   NOT NULL,
	"cf_id" int   NOT NULL,
    "first_name" varchar(50)   NOT NULL,
    "last_name" varchar(50)   NOT NULL,
    "email" varchar(100)   NOT NULL,
    CONSTRAINT "cf_id" PRIMARY KEY (
        "backer_id"
     )
);

ALTER TABLE "backers" ADD CONSTRAINT "fk_backers_cf_id" FOREIGN KEY("cf_id")
REFERENCES "campaign" ("cf_id");

SELECT * FROM backers


-- Challenge 
-- Deliverable 4: SQL Analysis, Step 2
-- Join Campaign and Backer,live events
SELECT c.cf_id,
    c.outcome,
	b.backer_id
INTO backer_campaigns
FROM campaign as c
LEFT JOIN backers as b
ON c.cf_id = b.cf_id
WHERE c.outcome = ('live')

SELECT * FROM backer_campaigns


-- Count Backers per campaign based on join
SELECT COUNT(bc.backer_id), bc.cf_id
INTO backer_campain_count
FROM backer_campaigns as bc
GROUP BY bc.cf_id
ORDER BY bc.count DESC;

SELECT * FROM backer_campain_count



-- Challenge - Deliverable 4: SQL Analysis, Step 3
-- Validate assumption using backers table - Total match
SELECT COUNT(b.backer_id), b.cf_id
INTO backer_count_backers
FROM backers as b
GROUP BY b.cf_id
ORDER BY b.count DESC;

SELECT * FROM backer_count_backers

--Challenge - Deliverable 4: SQL Analysis, Step 4
-- New table with first_name, last_name, email and remaining goal amount
-- in descending order for each live campaign
SELECT c.goal,
	c.pledged,
	ct.first_name,
	ct.last_name,
	ct.email
INTO goal_remaining
FROM campaign as c
INNER JOIN contacts as ct
ON c.contact_id = ct.contact_id
WHERE c.outcome = ('live')

SELECT * FROM goal_remaining

-- Get delta of goal outstanding
SELECT gr.first_name,
	gr.last_name,
	gr.email,
	(gr.goal - gr.pledged) AS goal_remaining
INTO email_contacts_remaining_goal
FROM goal_remaining as gr
ORDER BY goal_remaining DESC;

SELECT * FROM email_contacts_remaining_goal


--Challenge - Deliverable 4: SQL Analysis, Step 5
-- New table with backer emails DESC, first_name, last_name, cf_ID, company name
-- description, end_date of the campaign and remaining amount from goal.
SELECT b.email,
	b.first_name,
	b.last_name,
	b.cf_id,
	c.company_name,
	c.description,
	c.end_date,
	(c.goal - c.pledged) AS "Left of Goal"
INTO email_backers_remaining_goal_amount
FROM backers as b
INNER JOIN campaign as c
ON b.cf_id = c.cf_id
ORDER BY email DESC;

SELECT * FROM email_backers_remaining_goal_amount

