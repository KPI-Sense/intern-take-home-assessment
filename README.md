# KPI Sense Software Engineering Intern Assessment

### Description

Your day to day at KPI will envolve working with a mass amount of financial data. We ingest data through multiple sources in multiple formats. We use a robust ETL process to extract all that data, transform it into our standard data model, and load it into our data lake. This is an important step because without this process we would not be able to easily and effienctly onboard new clients and display our financial models to them without the data being in a standard format.

For this assessment you will be acting as an ETL developer whose job is to parse a demo company model and display some interesting insights back to the user.

### Goal

Create a command line script that when run parses the demo_model excel file and extracts the 3 rows listed belows and displays a stacked bar chart with a datetime x-axis and the Subscription and Services Revenue as the y-axis

script should be executed running

```
python main.py
```

##### Row details

row #4 Summary Financial Metrics -> this will be all the datetime rows. Each datetime should be set to the last day of the month reguardless of what is in the excel column

row #5 Subscription Revenue (empty values can be assumed 0)

row #6 Services Revenue (empty values can be assumed 0)

When parsing the data you can ignore the first column and only use the data values so for example for row #4 ignore the row title `Summary Financial Metrics` and only parse the datetimes and for row 5 and 6 only parse the money value.


#### Bonus
1) Add a command line argument date in the format of mm/yyyy which should be be executed with the below command
  ```
  python main.py 04/2018
  ```

  That only parses the the data from the excel file after this date and displays the same chart and information.
  
2) Add forcast plotting in (including with the above 1 time filter). A forcast value is considered to any value in the row whose date is past the current datetime. For example if the current date is June 6th 2019 then a normal value is anything before June 6th 2019 and a forcasted value is anything after June 6th 2019. A forcasted series should be plotted using different colors and labels to indicate that is a forecasted value.

`note when submitting bonus parts the assessment create a new python file name main_bonus_{bonus_number}.py and put all additonal code in here. Leave your origional assessment submission as is.`

### CodeSubmit

Please organize, design, test and document your code as if it were
going into production - then push your changes to a feature branch. After you have pushed your code, you may submit a pull request into master for code review.

All the best and happy coding,

The CodeSubmit Team
