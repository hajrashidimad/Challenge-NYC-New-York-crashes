# Challenge-NYC-New-York-crashes
![n-y-c](https://dataladder.com/wp-content/uploads/2020/03/data-cleaning-tool.jpg)

## Why
before enter the data in our ml module, we should do an important steps, (cleaning,  processing, ....ect).
## When
normally, this stuff should realized during three days.
## Usage
To begin your mission, you will need:\
python3 (or python)
\

Certain library:\
-Pandas\
-Numpy\

you will find in the data folder a csv file which you can use or download it [here](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95) .

## How
 This project will clean errors, NaN value etc...and create new file csv which have the cleaned data, and you find more explication in the comments with python code.

 ## notice
 
 | Content | Description |
 |---|---|
 cleaned_data.csv| the result after a normal cleaning
 hard_cleaned_data.csv| if you use this file for training you module, you should creat an onother script that transfer the location to real adresse
you can also get the address from any location by using *geopy* package

```bash
pip install geopy
```
you find more information in the link below:\
![Read the Docs](https://geopy.readthedocs.io/en/latest/)


## Team
Copyright (C) 11.12.2020 by : HajRashid IMAD
