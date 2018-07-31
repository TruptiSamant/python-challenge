import os
import csv
import numpy
#import inspect
#print(os.listdir('Resources/'))
#
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Main Function
pyBank()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''
* pyBank(): Python script for analyzing the financial records of your company
'''
def pyBank():

    #Read file
    csv_lst = read_csvfile()
    #Get Totals
    totals = total(csv_lst)
    #Get Max
    max_values = find_min_max(csv_lst)
    #Print Result
    print_result(totals, max_values)
#total_revenue = 0


'''
 * read_csvfile(): Reads the budget_data.csv file
 * returns list
 '''
def read_csvfile():
    #Get the path of the file
    file_path = os.path.join('Resources','budget_data.csv')
    #Check point
    #print(file_path)

    #Calculate total revenue
    lst = []
    with open(file_path) as csv_file:
        #Read the File
        csv_reader = csv.reader(csv_file)

        #skip first line
        next(csv_reader)

        #Append everthing to the list to string and int with error check
        for row in csv_reader:
            try:
                lst.append([row[0], int(row[1])])
            except:
                continue

    return (lst)

'''
 * total():
 * The total number of months included in the dataset
 * The total net amount of "Profit/Losses" over the entire period *
 * retrns tuple of months and sum
'''
def total(csv_lst):
    total_months = len(csv_lst)
    #print(total_months)
    #Total sum
    total_sum = sum(i[1] for i in csv_lst)
    #print("Total : {}".format(total_sum))

    return ({"months": total_months, "sum": total_sum})

'''
* find_min_max()
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in losses (date and amount) over the entire period
'''
def find_min_max(csv_lst):
    #Zip up the list to find the average
    zip_average = zip(csv_lst[:-1], csv_lst[1:])

    #concatinate the zip to find differece between adjacent row
    list_average = [(((j[0] + ' ' + i[0]),(j[1] - i[1])) ) for i,j in zip_average]

    #The average change in "Profit/Losses" between months over the entire period
    avg_profitloss = sum(x[1] for x in list_average)/len(list_average)
    #print("Average : {}".format(avg_profitloss))

    #The greatest increase in profits (date and amount) over the entire period
    #max_profit = [x for x in diff if x[1] == max((x[1] for x in diff))]
    result = max(list_average, key = lambda t: t[1])
    max_profit = (result[0].split()[0], result[1])
    #print("Average : {}".format(max_profit))

    #The lowest increase in profits (date and amount) over the entire period
    #min_profit = [x for x in diff if x[1] == min((x[1] for x in diff))]
    result = min(list_average, key = lambda t: t[1])
    min_profit = (result[0].split()[0], result[1])
    #print("Average : {}".format(min_profit))

    return ({"profitloss": avg_profitloss, "max": max_profit, "min":min_profit})

'''
print_result()
params:
totals: Dictionary of total months and total total_sum
max_values: Dictionary of avarage, max and min profit/loss
'''
def print_result(totals, max_values):
    print("Financial Analysis")
    print("-----------------------------------\n")
    print("Total Months : {}".format(totals["months"]))
    print("Total : ${:,.2f}".format(totals["sum"]))
    print("Average profit/loss : ${:,.2f}".format(max_values["profitloss"]))
    print("Greatest Increase in Profits :{} (${:,.2f})".format(max_values["max"][0], max_values["max"][1]))
    print("Greatest Decrease in Profits :{} (${:,.2f})".format(max_values["min"][0], max_values["min"][1]))
