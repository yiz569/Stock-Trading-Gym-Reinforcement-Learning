from dotenv import load_dotenv
import json
import os
import requests
import pandas as pd 
from datetime import datetime
import datetime

load_dotenv() 

apikey = str(os.environ.get("ALPHAVANTAGE_API_KEY"))

#intro Messages
print("--------------------------------------------------- ")
print(" ")
print("This application helps fetch real stock data from Alpha Vantage")
print(" ")
print("You can check the stock ticker of a company online")
print(" ")
print("E.G. The ticker for GOOGLE is GOOGL. The ticker for Amazon is AMZN.")
print(" ")
print("--------------------------------------------------- ")
print(" ")

#requesting ticker for the stock
while True:
    ticker = input("Please enter the ticker of your stock of choice: ") 
    
    if ticker.isdigit():
        print("Invalid entry: a stock ticker only uses characters - integers or symbols are not permitted")
    else:
        pull = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=full&apikey=" + apikey)
        
        if "Error" in pull.text:
            print("Error: stock either cannot be found or is not listed on Alpha Vantage - please enter another stock ticker")
        else:
            break  

j=pull.json()

#variables created for the date to be used later
time = datetime.datetime.now()
a = time.strftime("%Y")
b = time.strftime("%m")
c = time.strftime("%d")    
d = time.strftime("%I")
e = time.strftime("%M")
f = time.strftime("%p")

t,opn,h,l,close,vol = [],[],[],[],[],[]

#adds values pulled from Alpha Vantage
for lx, value in j["Time Series (Daily)"].items():
    t.append(lx)
    
    opn.append(float(value["1. open"]))

    h.append(float(value["2. high"]))
    
    l.append(float(value["3. low"]))
    
    close.append(float(value["4. close"]))
    
    vol.append(float(value["5. volume"]))

print(" ")
print("--------------------------------------------------- ")
print(" ")
print("Stock Ticker: " + ticker)
print(" ")
print("Program Run On: " + a + "-" + b + "-" + c + " " + d + ":" + e + " " + f)
print(" ")
print("...")
print(" ")
print("Now saving the requested information")
print(" ")
print("...")
print(" ")

#data headers are formatted in order to be put into a CSV
output = pd.DataFrame(
    {
        "Date":t, "Open":opn, "High": h, "Low":l, "Close":close, "Volume": vol,
    }
)

#rearrange the data from oldest to newest
idx = output.index.values
output = output.iloc[::-1]
output.index = idx

#deletes a file if it is named in the same way (the data would essentially be the same)
while True:
    if os.path.isfile("data/" +ticker + "_" + a + b  + c + ".csv"):
        os.remove("data/" + ticker + "_" + a + b  + c + ".csv")
    else:
        break

#data is pushed into a CSV file
output.to_csv("data/" + ticker + "_" + a + b  + c + ".csv")

print("File saved as " + ticker + "_" + a + b  + c + ".csv in the 'data' folder")
print(" ")
print("--------------------------------------------------- ")
print(" ")
print(" ")
print("CALCULATING BASIC RELEVANT DATA")
print(" ")
print("...")
print(" ")
print("LAST DAY OF AVAILABLE DATA: " + output.iloc[max(idx)]["Date"])
print("")