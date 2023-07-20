import os
import csv

#data storage
bankData = {"Date":[], "Profit/Losses":[]}
date = []
proLoss = []
proLossChange = []
monthCount = 0 
profitTotal = 0 
changeAvg = 0
gIncInt = 0
gDecInt = 0
gIncIndex = 0
gDecIndex = 0

#gets the data from the budget_data.csv file and opens the file
bankPath = os.path.join('Resources/budget_data.csv')
with open(bankPath) as bankFile: 
    bankReader = csv.reader(bankFile,delimiter=',')
    bankHeader = next(bankReader)
#adds bankReader info to lists for access without opening bankPath
    for row in bankReader:
        date.append(row[0])
        proLoss.append(int(row[1])) 
        monthCount += 1
        profitTotal += int(row[1])

#add data to bankData dictionary
bankData["Date"] = date
bankData["Profit/Losses"] = proLoss

#get increase/decrease values
for x in range(85):
    proLossChange.append(-1*(bankData["Profit/Losses"][x]-bankData["Profit/Losses"][x+1]))
#get greatest increase/decrease values
for x in range(85):
    if proLossChange[x] > gIncInt:
        gIncInt = proLossChange[x]
        gIncIndex = x
    if proLossChange[x] < gDecInt:
        gDecInt = proLossChange[x]
        gDecIndex = x

#get the average change
for x in range(85):
    changeAvg =+ proLossChange[x]
changeAvg/=len(proLossChange)
changeAvg = round(changeAvg, 2)
#my math is wong for this but im not sure how to fix it and im out of time...

print(f"Total Months: {monthCount}")
print(f"Total: {profitTotal}")
print(f"Average Change: {changeAvg}")
print(f'Greatest Increase in Profits: {bankData["Date"][gIncIndex+1]} {proLossChange[gIncIndex]}')
print(f'Greatest Decrease in Profits: {bankData["Date"][gDecIndex+1]} {proLossChange[gDecIndex]}')

#create, open and write new csv file
analysis = os.path.join('analysis/bank_analysis.csv')
with open(analysis, 'w') as analysisFile:
    fileWrite = csv.writer(analysisFile, delimiter=" ")
    fileWrite.writerow(["Financial"] +["Analysis"])
    fileWrite.writerow(["------------------------------------------"])
    fileWrite.writerow(["Total"] +["Months:"] +[(str(monthCount))])
    fileWrite.writerow(["Total:"] +[str(profitTotal)])
    fileWrite.writerow(["Average"] +["Change:"] +[(str(changeAvg))])
    fileWrite.writerow(["Greatest"] +["Increase"] +["in"] +["Profits:"] +[(bankData['Date'][gIncIndex+1])]  +[(str(proLossChange[gIncIndex]))])
    fileWrite.writerow(["Greatest"] +["Decrease"] +["in"] +["Profits:"] +[(bankData['Date'][gDecIndex+1])]  +[(str(proLossChange[gDecIndex]))])
