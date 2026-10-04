import csv
#app name
APP ="Instagram"

minutes = []

with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))

#minutes[start:stop:step]

minutes[:7:1]
total=(int(sum(minutes)))
avg=total/len(minutes)
highest=max(minutes)
lowest=min(minutes)
count=0
for i in minutes:
    if i>avg:
        count+=1

print(f"App: {APP}, Average: {avg}, Highest: {highest}, Lowest: {lowest}, Count: {count}")  