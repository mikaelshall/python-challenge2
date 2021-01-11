# Import Modules/Dependencies 
import os 
import csv 

#Files to load 

infile = os.path.join('/Users/mikaelshall/Desktop/unc-peace-data-pt-08-2020-u-c/02-Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv')

outfile = os.path.join("analysis", "pybank.txt")

monthsTotal = 0
netTotal = 0
previousBudget = 0
changeTotal = 0
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseDate = ""
greatestDecreaseDate = ""

with open(infile) as csvFile:
    # print(csvFile.readline())
    # csv_header = next(rows)
    csvFile.readline()

    rows = csv.reader(csvFile)
    changeCount = 0
    change = 0

    for row in rows:
        monthsTotal += 1
        currentBudget = int(row[1])
        netTotal += currentBudget

        if previousBudget != 0:
            change = currentBudget - previousBudget
            changeTotal += change
            changeCount += 1
            print(change)

        previousBudget = currentBudget

        if change > greatestIncrease:
            greatestIncrease = change
            greatestIncreaseDate = row[0]

        if change < greatestDecrease:
            greatestDecrease = change
            greatestDecreaseDate = row[0]

    print(f"change count: {changeCount}")
    print(f"total of changes: {changeTotal}")
    # exit()

# print(monthsTotal)
# print(netTotal)
# print(greatestIncreaseDate,greatestIncrease)
# print(greatestDecreaseDate,greatestDecrease)

# def print_results(results):
#     print(results)

output = f"""
Financial Analysis
----------------------------
Total Months: {monthsTotal}
Total: ${netTotal:,}
Average  Change: ${changeTotal/changeCount:.2f}
Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease:,})
Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease:,})
"""

# Call def print_results(results)
# print_results(output)

print(output)