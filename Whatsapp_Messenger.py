import pywhatkit as kit # Library to send data through Whatsapp
import pandas as pd     # Library to represent data in tabular format
import datetime         # Library to fetch current date and time
import os               # Library to kill chrome task
import time             # Library to introduce time delay before killing chrome process


# Reading the .csv file first
reader = pd.read_csv('phone.csv')

# Creating Data Frame of the current file
df = pd.DataFrame(reader)

# Counting the number of rows (in this case, number of contacts)
r = df.index
 
for i in range(len(r)):

    # Reading and storing each entry in variable 'c'    
    c = df.loc[i][0]
    
    # Typecasting the entry into string
    c = str(c)
    k = "+91"
    # Concatenating "+91" to the phone number
    f = k + c
      
    # Fetching current date and time and storing in variables
    current = datetime.datetime.now()
    h = int(current.hour)
    m = int(current.minute)
    # Enter your message as follows:
    # For message on a single line, enter: msg = ["Message 1"]. This program will print the message on a single line.
    # For message on multiple lines, enter: msg = ["Message 1","Message 2","Message 3"] and so on. This program will print 3 messages on 3 lines.
    
    msg = ["Hello there! This message was sent through python programming!"]
    
    itr = 2 # Variable to manipulate time delay to send message.
    
    for j in range(len(msg)):
        # Using sendwhatmsg() to send message to the phone number
        # sendwhatmsg("Phone Number","Message to be send","Hours","Minutes")
        # Hours should be in 24 hr format
        # Adding m + itr as a small delay to open Whatsapp Web and send message
        
        kit.sendwhatmsg(f,msg[j],h,m+itr)
        itr += 1
        if (itr % 12 == 0):
            os.system("taskkill /im chrome.exe /f")
    
    i += 1
    #The chrome will shutdown after 30 seconds
    time.sleep(50)
    if (i % 10 == 0):
       os.system("taskkill /im chrome.exe /f")
    time.sleep(30)
 
