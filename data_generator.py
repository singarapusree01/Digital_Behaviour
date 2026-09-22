import random as r
import csv
import datetime
import numpy
days=20
r.seed()
rows=[]
for i in range(days):
  instamin=r.randint(1,2000)
  facebookmin=r.randint(1,200)
  ytmin=r.randint(1,2000)
  rows.append([instamin,facebookmin,ytmin])

with open(
  "digital_behaviour.csv",
  "w",
  newline="",
  encoding="utf-8"
)as f:

  writer=csv.writer(f)

  writer.writerow([
    "instamin",
    "facebookmin",
    "ytmin"
  ])

  writer.writerows(rows)

print("completed")