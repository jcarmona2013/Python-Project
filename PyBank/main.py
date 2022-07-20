import csv
data_to_Analyze = csv.DictReader(open('Resources/budget_data.csv'))
analysis = open('analysis/budget_analysis.txt','w')
months = 0
total = 0
pre_rev = 0
ch_avg = 0 
inc = ["",0]
dec = ["",0]

for i, row in enumerate(data_to_Analyze):
    rev = int(row['Profit/Losses'])
    months += 1
    total += rev
    
    if i == 0:
      pre_rev = rev

    change = rev - pre_rev
    ch_avg += change 
    pre_rev = rev 

    if change > inc[1]:
      inc[0] = row["Date"]
      inc[1] = change

    if dec[1] > change:
      dec[0] = row["Date"]
      dec[1] = change

output = f'''
  text
  Financial Analysis
  ----------------------------
  Total Months: {months}
  Total: ${total:,.0f}
  Average Change: {ch_avg/(months - 1):,.2f}
  Greatest Increase in Profits: {inc[0]} (${inc[1]:,.0f})
  Greatest Decrease in Profits: {dec[0]} (${dec[1]:,.0f})
'''

print(output)
analysis.write(output)
