import numpy as np
import csv
insta_list=[]
study_time=[]

with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_time.append(int(row["Study_Minutes"]))

insta_list[:7:1]
study_time[:7:1]

insta_array=np.array(insta_list)
study_array=np.array(study_time)

total=insta_array.sum()
avg=insta_array.mean()
highest=insta_array.max()
lowest=insta_array.min()
print(f"Total: {total}, Average: {avg}, Highest: {highest}, Lowest: {lowest}")
print(insta_array[0])
print(study_array[-1])
print(insta_array[2])

print(insta_array[0:3])
print(study_array[-2:])
print(insta_array[2:4:])

hours=insta_array/60

diff=insta_array-study_array

greater_than=insta_array>100

print(greater_than.sum())

above_avg=insta_array>avg
print(above_avg.sum())