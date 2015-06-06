#NepalEarthquake

A simple widget that fetches seismic activities from [seismonepal](http://www.seismonepal.gov.np) and converts the data in Nepali

The widget is being used in [himalkhabar](http://www.himalkhabar.com)

For further info visit: [rvibek.com.np/json-file-for-seismic-activities-in-nepal](http://rvibek.com.np/json-file-for-seismic-activities-in-nepal/) 

##File Intro
I have put these scripts in [OpenShift](http://openshift.com) The accompanying 

>getCSV.sh 
>earthquake.py
>earthquakeCSV2JSON.py

files are put in cron which updates CSVs and JSON every hour

##Process
* Run getCSV.sh to fetch latest earthquake.csv
* earthquake.py cleans the above csv and replaces English digits and place names to Nepali in earthquakenep.csv

##Additinal Process
A simple HTML widget displays the latest seismic activities in Nepali [Example](https://app-weather.rhcloud.com/data/earthquake/)
* earthquakeCSV2JSON.py converts CSV into earthquakeNE.json

##Widget Example
![NepalEarthquake Widget](https://github.com/rvibek/NepalEarthquake/blob/master/images/NepalEarthquake_Widget.png)