import pandas as pd
import time
import numpy as np

def substring(s, start, end):
    return s[start:end]

def date_update(data):
    for i in range(len(data)):
        string = data.loc[i, 'Date']

        month = substring(string, 0,3)
        day = substring(string, 4, 6)
        year = substring(string, 8, 12)

        if month == 'Jan':
            month = '01'
        if month == 'Feb':
            month = '02'
        if month == 'Mar':
            month = '03'
        if month == 'Apr':
            month = '04'
        if month == 'May':
            month = '05'
        if month == 'Jun':
            month = '06'
        if month == 'Jul':
            month = '07'                
        if month == 'Aug':
            month = '08'
        if month == 'Sep':
            month = '09'
        if month == 'Oct':
            month = '10'
        if month == 'Nov':
            month = '11'
        if month == 'Dec':
            month = '12'
            
        date = day + '/' + month + '/' + year
        data.loc[i, 'Date'] = date

    return data


def price_fix(data):
    for i in range(len(data)):
        price = data.loc[i, 'Price']
        open_price = data.loc[i, 'Open']
        high = data.loc[i, 'High']
        low = data.loc[i, 'Low']

        data.loc[i, 'Price'] = price.replace(',', '')
        data.loc[i, 'Open'] = open_price.replace(',', '')
        data.loc[i, 'High'] = high.replace(',', '')
        data.loc[i, 'Low'] = low.replace(',', '')

    return data

def volume_fix(data):
    for i in range(len(data)):
        price = str(data.loc[i, 'Vol.'])
        
        if "M" in data.loc[i, 'Vol.']:
            price = data.loc[i, 'Vol.'] + '0000'
            price = price.replace('M', '')
        if "K" in price:        
            price = data.loc[i, 'Vol.'] + '0'
            price = price.replace('K', '')
        
        temp = price.split('.')
        price = temp[0] + temp[1]
       
        data.loc[i, 'Vol.'] = price
            
    return data


def change_fix(data):
    for i in range(len(data)):
        price = data.loc[i, 'Change %']
        data.loc[i, 'Change %'] = price.replace('%', '')
    return data


def add_class(data, time):
    for i in range(len(data)):
        try:
            current = data.loc[i, 'Price']
            future = data.loc[i-time, 'Price']
            if current <= future:
                data.loc[i, 'Class'] = 'good'
            else:
                data.loc[i, 'Class'] = 'bad'
        except:
            data.loc[i, 'Class'] = np.nan
    return data

def clean(time):
    data = pd.read_csv("dataCopy.csv")
    #for i in range(len(data)):

    data = date_update(data)
    data = price_fix(data)
    data = volume_fix(data)
    data = change_fix(data)
    data = add_class(data, time)
    data.to_csv("new.csv", index=False)



