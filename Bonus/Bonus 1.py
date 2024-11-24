#created a dictionary in qs.json
#it contains a list of lisys

import json

with open("qs.json") as file:
    content = file.read()
data=json.loads(content)
print(type(content))#string its useless
print(type(data))#list so its mutable

print(data) #list of dicttionaries

#important info
#you can create a dictionary
#you can add swperate keys
a={}
a["b"]=1
print(a)
a["c"] =2
print(a)

for question in data: #question is the current dictionary
    print(question["Question"])  # Print the question key
    for index,alternative in enumerate(question["Alternatives"]):  # Iterate through alternatives
        print(index+1,"-",alternative)
    user_choice = int(input("Please enter your choice: "))
    question["User Choice"] = user_choice


total=0
for index,question in enumerate(data):
    if question["User Choice"] == int(question["Correct Answer"]):
        total =total+1
        result ="Correct Answer"
    else:
        result="Wrong Answer"
    row =f"{index+1}-{result}. You chose {question["User Choice"]}. The correct answer is {question["Correct Answer"]}"
    print(row)
print(f"Your score is {total}/{len(data)}")