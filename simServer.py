#!/usr/bin/env python3
# ==============================================================
# SINGAPORE POLYTECHNIC                                        |
# SCHOOL OF COMPUTING                                          |
# ST2411                                                       |
# PROGRAMMING IN PYTHON AND C                                  |
# NAME: ALEK KWEK                                              |
# CLASS: DISM/FT/1A/23                                         |
# ADMIN NO: 1804247                                            |
# YEAR: 2019                                                   |
# ==============================================================

# IMPORT
import socket
import os
import re as r
import operator

#    It maintains the client session (and keep echos back the message to the client),
#   until the client sends in a 'x'.
#   The client request handling is now refactored into an independent
#   function, handler.
#   After this refactoring, this handler function can be easily utilizing
#   threading model to hanlde muliple echo requests from more than one client.
#   At this version, however, it remains handling one client at a time.
totalItems = 0 # global variable to store 
totalSales = 0 # global variable
item_dict = {}
sorted_list = []        
output = ""
def GenerateReport(cityName):
    #city stores the content of cityName.title()
    #the function title() converts the first character of every word to uppercase
    #e.g "singapore polytechnic" is now "Singapore Polytechnic"
    #It stores the updated string into the variable city
    city = cityName.title()
    #statementSpacing is a function that produces an apporiate spacing so that the items and the money is organised
    #======================================================
    #DVDs                                         2369572.76   -> giving the right number of spacing is 
    #CDs                                          2303437.88   important 
    #Sporting Goods                               2303015.72
    #======================================================
    #[item][remaining][amount]
    def statementSpacing(word_string):
        space = " " # The variable speed is defined with " "
        length = len(word_string) # The length of items is calculated using len ans stores in length
        max_length = 44 # The max_length states the maximum number of spacing is allowed. The max number is 44 * space
        remaining = max_length - length # The variable remaining stores the difference between the 
        # the length of items and max_length. This variable stores the value to create the value * spaces
        for i in range(0,remaining): # For loop is used from 0 to the remaining
            space = space + " " # Space is added with new space for each iteration of the for loop
        return space # After the for loop has been completed, it returns the number of spaces 
    # Sorting sorts the dictonary based on the key value       
    def sorting(dict_data):
        #To sort the dictionary, convert it to a list with turples
        dict_items = dict_data.items()
        #Covert to a list with tuples
        dict_item_list = list(dict_items)
        #Now our data is stored in a list we can order by the amount
        #by the operator itemgetter(1) where 1 is the second element in the list which is amount in float numbers
        #reverse = True reverse the order from ascending to descending order
        sorted_list = sorted(dict_item_list,key = operator.itemgetter(1), reverse = True)
        return sorted_list # returns the sorted list 
    #extractItems is a function that uses regular expression(regex) to extract out the item's name e.g computer, toys, clothing    
    def extractItems(sales_lines):
        #For demostration, I will be using this sales data
        #2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
        #r.findall uses regex [\D]+[\W]+ to extract out the city name and item name
        #[\D]+[\W]+ : [\D\]+ Matches between one and unlimited times, as many times as possible, giving back as needed
        #\D matches any character that's not a digit (equal to [^0-9])
        #[\W]+ Matches between one and unlimited times, as many times as possible, giving back as needed
        #\W matches any non-word character (equal to [^a-zA-Z0-9_])
        #Using the regex, the extracted data from
        #2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
        #is 
        #	Fort Worth	Women's Clothing	
        #This extracted data is then stored in firstLayer as objects
        #SecondLayer stores the string firstLayer[0]
        firstLayer = r.findall("[\D]+[\W]+",sales_lines)
        secondLayer = firstLayer[0]
        #The variable pattern is used to search for the city name
        #1st Alternative \t[a-zA-Z]\s*[a-zA-Z]*\t
        #\t matches a tab character (ASCII 9)
        #Match a single character present in the list below [a-zA-Z]
        #a-z a single character in the range between a (index 97) and z (index 122) (case sensitive)
        #A-Z a single character in the range between A (index 65) and Z (index 90) (case sensitive)
        #\s* matches any whitespace character (equal to [\r\n\t\f\v ])
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #Match a single character present in the list below [a-zA-Z]*
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #a-z a single character in the range between a (index 97) and z (index 122) (case sensitive)
        #A-Z a single character in the range between A (index 65) and Z (index 90) (case sensitive)
        #\t matches a tab character (ASCII 9)
        #2nd Alternative \t[a-zA-Z]+\s*[a-zA-z]*\t
        #\t matches a tab character (ASCII 9)
        #Match a single character present in the list below [a-zA-Z]+
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #a-z a single character in the range between a (index 97) and z (index 122) (case sensitive)
        #A-Z a single character in the range between A (index 65) and Z (index 90) (case sensitive)
        #\s* matches any whitespace character (equal to [\r\n\t\f\v ])
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #Match a single character present in the list below [a-zA-z]*
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #a-z a single character in the range between a (index 97) and z (index 122) (case sensitive)
        #A-z a single character in the range between A (index 65) and z (index 122) (case sensitive)
        #\t matches a tab character (ASCII 9)
        #3rd Alternative \t\w+\.+\-*\s*\w*\t
        #\t matches a tab character (ASCII 9)
        #\w+ matches any word character (equal to [a-zA-Z0-9_])
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #\.+ matches the character . literally (case sensitive)
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #\-* matches the character - literally (case sensitive)
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #\s* matches any whitespace character (equal to [\r\n\t\f\v ])
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #\w* matches any word character (equal to [a-zA-Z0-9_])
        #\t matches a tab character (ASCII 9)
        #4th Alternative \t\w*\–*\w+\s?\w?\t
        #\t matches a tab character (ASCII 9)
        #\w* matches any word character (equal to [a-zA-Z0-9_])
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #\–* matches the character – literally (case sensitive)
        #* Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #\w+ matches any word character (equal to [a-zA-Z0-9_])
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #\s? matches any whitespace character (equal to [\r\n\t\f\v ])
        #\w? matches any word character (equal to [a-zA-Z0-9_])
        #\t matches a tab character (ASCII 9)
        #5th Alternative \t\w+\s*\w*\s*\w*\t
        #\t matches a tab character (ASCII 9)
        #\w+ matches any word character (equal to [a-zA-Z0-9_])
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #\s* matches any whitespace character (equal to [\r\n\t\f\v ])
        # * Quantifier — Matches between zero and unlimited times, as many times as possible, giving back as needed (greedy)
        #\w* matches any word character (equal to [a-zA-Z0-9_])
        # \s* matches any whitespace character (equal to [\r\n\t\f\v ])
        #\w* matches any word character (equal to [a-zA-Z0-9_])
        #\t matches a tab character (ASCII 9)
        #The reason why this regex is so complex is because there are different types of wording of cities
        #There are one word cities, Madison
        #There are two words cities, New York
        #There are special character word cities. St. Petersburg.txt and Winston–Salem.txt
        #Hence, various regex are needed to extract out all these types of wordings
        pattern = r"(\t[a-zA-Z]\s*[a-zA-Z]*\t|\t[a-zA-Z]+\s*[a-zA-z]*\t|\t\w+\.+\-*\s*\w*\t|\t\w*\–*\w+\s?\w?\t|\t\w+\s*\w*\s*\w*\t)"
        #r.sub finds the secondLayer with the pattern
        #it replaces the the said pattern with "\t" and pass the value to thirdLayer
        #Hence, the value is changed from
        #	Fort Worth	Women's Clothing	
        #to this
        #\tWomen's Clothing\t
        thirdLayer = r.sub(pattern,r"\t",secondLayer)
        #Another sub function is used to replace "\t" with "" and pass to itemtype
        #The value changed from
        #\tWomen's Clothing\t
        #to
        #Women's Clothing
        #Hence, the item's name is extracted from the sales data
        itemType = r.sub("\t","",thirdLayer)
        return itemType #returns item name
    #extractSales is a function that uses regular expression(regex) to extract out sales figure    
    def extractSales(sales_lines):
        #For demostration, I will be using this sales data
        #2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
        #the regex (\d+\.\d+|\t\d+\t)
        #1st Alternative \d+\.\d+
        #\d+ matches a digit (equal to [0-9])
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #\. matches the character . literally (case sensitive)
        #\d+ matches a digit (equal to [0-9])
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #2nd Alternative \t\d+\t
        #\t matches a tab character (ASCII 9)
        #\d+ matches a digit (equal to [0-9])
        #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
        #\t matches a tab character (ASCII 9)
        #Hence, the data extracted from
        #2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
        #is 153.57 and is stored as object in firstLayer
        firstLayer = r.findall("(\d+\.\d+|\t\d+\t)",sales_lines)
        #strsales stores the content of firstLayer[0] which is a string data type
        strsales = firstLayer[0]
        sales = float(strsales) #float converts strsales to a float value and pass to sales
        return sales# return sales
    #findFIles is a function that serach for the text file and determine if it exists.
    #If it doesn't exist, then the function will output a statement saying the file name is invalid
    #If the file exist, then extraction of items and sales is started
    def findFiles(city):
        # keyword global helps to reference to the global variable and does not create a local variable
        global totalItems 
        global totalSales
        global sorted_list
        global item_dict
        messages = "" #store statement
        city_exist = 0 #set city exist to 0 
        fileName = "" 
        citytext = city + ".txt" #append .txt to cityname e.g city=New York -> city + ".txt" : New York.txt
        # use for loop to find the file to match with with citytext starting at the reports/ directory 
        # reprts/ is a directory that has all the city files that is made by a C program
        for root, dirs, files in os.walk("/home/st2411/myCprog/C Assignment/PYC-ASSIGNMENT-1-master/reports/"):
            for file in files:
                if file.endswith(citytext): #if file name matches            
                     fileName = os.path.join(root, file)
                     #pass the location of the file to fileName
                     city_exist = 1 #set city_exist bit to 1 to indicate the city is valid
                     break#stop the for loop
        # If city exist             
        if (city_exist == 1):             
           datafile = open(fileName,"r") #do a file operation to open and read the contents of the file
           #perform a for loop operation to process a line of sales file until the END OF LINE
           for i in datafile: 
                    items = extractItems(i) #extract out the item's name
                    sales = extractSales(i) #extract out the item's sales figure
                    #This condition is only valid at the start of the processing when the total items in the dictonary is 0
                    if(totalItems == 0): 
                        item_dict[items] = sales #store the key which is sales to the item in item_dict
                        totalItems += 1 #once added to dict, increment the number of items by 1
                        totalSales = sales #let the totalSales be the sales at the beginning
                    else:
                      if items in item_dict: #check if items is only in the item_dict
                      #if it does exist...
                            item_dict[items] = item_dict[items] + sales#increment sales figure from new data with the same item type to the existing sales data in the item dict
                            totalSales += sales#increment the new sales data to the main total sales
                      else:
                      #if it does not exist...    
                        item_dict[items] = sales #store the key which is sales to the item in item_dict
                        totalItems += 1 #once added to dict, increment the number of items by 1
                        totalSales = sales #let the totalSales be the sales
           sorted_list = sorting(item_dict) #sort the dict and return the sorted list
           messages = statement() #call statement function and store the output into messages
           datafile.close() #close the file after processing has been completed
           return messages #return the message that will be displayed to client
        else:
                messages = "\nInvalid City Name. Please Try Again\n" #display message to client
                return messages #return the message that will be displayed to client
    def average_sales(): 
        #average sales is calculated by the total sales divided by the number of items
        mean_sales = totalSales/totalItems
        return mean_sales

    #if the file exist, this function will print to the client 
    #example
    #Total sales from New York is     40326944.93
    #The Average Sales From    18 Item Categories:
    #                                             2240385.83
    #
    #Top Three Item Categories
    #======================================================
    #DVDs                                         2369572.76
    #CDs                                          2303437.88
    #Sporting Goods                               2303015.72
    #======================================================
    #Bottom Three Item Categories
    #======================================================
    #Cameras                                      2179139.24
    #Music                                        2135497.64
    #Women's Clothing                             2095923.28
    #======================================================    
    def statement():
        # keyword global helps to reference to the global variable and does not create a local variable
        global totalItems
        global totalSales
        global sorted_list
        length_of_list = len(sorted_list)  #find the length of the sorted_list with len and store the length to length_of_list      
        statement = "Total sales from {} is     {:.2f}".format(city,totalSales) 
        statement += "\nThe Average Sales From    {} Item Categories:".format(totalItems)
        statement += "\n                                             {:.2f}\n".format(average_sales())
        statement += "\nTop Three Item Categories"
        statement += "\n======================================================"
        #For loop prints the top three item categoires
        for i in range(0,3):
                #Here is a visualisation of a list
                # [("New York","500.0"),("San Jose","300"),...]
                # sorted_list[i][0] is the item
                # sorted_list[i][1] is the amount
                item = sorted_list[i][0]
                amount = sorted_list[i][1]
                statement += "\n{}".format(item) + statementSpacing(item) +"{:.2f}".format(amount)
        statement += "\n======================================================"
        statement += "\nBottom Three Item Categories"
        statement += "\n======================================================"
        #For loop prints the bottom three item categoires
        for i in range(length_of_list-3,length_of_list):
                #Here is a visualisation of a list
                # [("New York","500.0"),("San Jose","300"),...]
                # sorted_list[i][0] is the item
                # sorted_list[i][1] is the amount
                item = sorted_list[i][0]
                amount = sorted_list[i][1]
                statement += "\n{}".format(item) + statementSpacing(item) +"{:.2f}".format(amount)  
        statement += "\n======================================================"
        return statement    
    
    output = findFiles(city) #message is passed to output
    return output
def handler(con):
    while True:
        buf = con.recv(5000) # buf is of the type of byte
        if len(buf) > 0:
            print("\nUSER INPUT:",buf.decode())  # decode with system default encoding scheme
            if buf == b"q" or buf == b"x":
                break
            else:
                #decode client's input
                cityName = buf.decode()
                #process the input and return a statement
                report = GenerateReport(cityName)
                #these print statement is only for the IT admin to see
                print("USER OUTPUT")
                print(report)
                print("\nEND OF USER OUTPUT")
                #encode the statement and send it back to the client
                buf = report.encode()
                # echo back the same byte sequence to client
                con.sendall(buf)

        else: # 0 length buf implies client has dropped the con.
            return ""  # quit this handler immediately and return ""  
    con.close() #exit from the loop when client sent q or x
    return buf.decode()
# MAIN PROGRAM STARTS HERE    
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections
while True:
    print("waiting a new call at accept()")
    connection, address = serversocket.accept()
    if handler(connection) == 'x':
        break; 
serversocket.close()
print("Server stops")
