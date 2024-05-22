![screenshot](src/images/ironman_logo.png)

:swimming_man:  This is a regression case that aims to estimate the finish time of a half ironman based on the age, gender, and half-marathon time calculated with a known marathon average pace (as you don't run a half marathon alone as quickly as you run a half marathon after swimming and cycling).

:bike: The dataset consists of Ironman 70.3 race records around the world registered between 2010 and 2020, including as main columns the tri-athletes gender, age group, country of origin, the year and the location of the race, and the partial (swim, bike, run, transitions) and full race finish times (in seconds).
In total 795863 records from Ironman 70.3 PRO and recreational were used.
Several models were tested: Linear Regression, Ridge Regression, Lasso Regression, Random Forest, Gradient Boosting, and XGBoost.

:running: The best model was kept for prediction. 

Limits: no information on weather, elevation, number of supporters along the course, number of refueling sites on the course, and you have elites and amateur athletes mixed in the dataset.

[Link to the streamlit app](https://ironman703.streamlit.app)

