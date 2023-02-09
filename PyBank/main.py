'''
    PYBANK Main Code
    GT Boot Camp - Data Vizualization
    HW3 - Python Challenge
    Jason Hanlin

    For resources: python-challenge/PyBank/Resources

'''

import os   #import os module
import csv  #import csv module

#  Read File in python-challenge/Resources/budget_data.csv
csvFilePath = os.path.join("Resources", "budget_data.csv")

# Use with open command and csv.reader to read file
with open(csvFilePath, 'r') as dataFile:
    csvReader = csv.reader(dataFile, delimiter=',')
    header = next(csvReader)    #Store header as seperate variable
    data = list(csvReader)      #create a full list of all data without header
    profitLossData = []         #create an empty list to add profit and loss data to
    change = []                 #create an empty list to add change data for each row
    
    previousPL = 0
    maxIncrease = 0
    maxDecrease = 0

    for date, profitLoss in data:
        profitLossData.append(int(profitLoss))  #create list for profitLossData
        changeValue = (int(profitLoss) - int(previousPL))
        change.append(int(changeValue))
        
        if changeValue > maxIncrease:
            maxIncrease = changeValue
            increaseDate = date

        if changeValue < maxDecrease:
            maxDecrease = changeValue
            decreaseDate = date
        
        previousPL = profitLoss

    change.pop(0)  #remove the first element in the list since there was no change
#    print(change)
#    print(profitLossData)

    # perform calculations with profitLossData list
    total_months = int(len(profitLossData))
    total = sum(profitLossData)
    average_change = round(sum(change)/len(change), 2)

    # print results
    print()
    print('Financial Analysis\n')
    print('------------------------------------\n')
    print('Total Months:', total_months, '\n')
    print('Total:', '${:,.0f}'.format(total), '\n')
    print('Average Change:', '${:,.2f}'.format(average_change), '\n')
    print('Greatest Increase in Profits:', increaseDate,"(",'${:,.0f}'.format(maxIncrease),")", '\n')
    print('Greatest Decrease in Profits:', decreaseDate,"(",'${:,.0f}'.format(maxDecrease),")", '\n')

# Write ouput to the file anlysis/outputfile.txt
outputfilepath = os.path.join("analysis","outputfile.txt")

# Use with open command to write information to a file
with open(outputfilepath,'w') as txtOutput:
    txtOutput.write('')
    txtOutput.write('Financial Analysis\n\n')
    txtOutput.write('------------------------------------\n\n')
    txtOutput.write(f'Total Months: {total_months}\n\n')
    txtOutput.write(f'Total: ${total}\n\n')
    txtOutput.write(f'Average Change:  ${average_change}\n\n')
    txtOutput.write(f'Greatest Increase in Profits:  {increaseDate}  (${maxIncrease})\n\n')
    txtOutput.write(f'Greatest Decrease in Profits:  {decreaseDate}  (${maxDecrease})\n\n')

    












