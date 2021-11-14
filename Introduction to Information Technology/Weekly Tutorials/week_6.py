# thisdict =	[{
#   "name": "Reed",
#   "model": "Mustang",
#   "year": 1964
# }, 
# {
#   "name": "Lukas",
#   "model": "Mustang",
#   "year": 1964
# }, 
# {
#   "name": "Helen",
#   "model": "Mustang",
#   "year": 1964
# }]
# i = 0
# for x in thisdict:
#   print(thisdict[i])
#   i += 1

# thisdict =	{"Reed": {
#   "model": "Mustang",
#   "year": 1964
# }}, 
# {"Lukas": {
#   "model": "Mustang",
#   "year": 1964
# }}, 
# {"Helen": {
#   "model": "Mustang",
#   "year": 1964
# }}
# x = 0
# for i in thisdict:
#     # print(thisdict[x["Reed"]])
#     print(thisdict[x])
#     x =+ 1

# d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}

# for i in d['dict1']:
#     print(i)
#     print(d['dict1'][i])
    # for j in d[i].keys():
    #     print(j)

# a_dict = {'apple':'red', 'grass':'green', 'sky':'blue'}
# for key in a_dict:
#   print(key) # for the keys
#   print(a_dict[key]) # for the values

dict =	{"Reed": { "weight": 106,  "height": 1.73}, 
"Lukas": {"model": "Mustang","year": 1964}, 
"Helen": {"model": "Mustang","year": 1964}}

val = True
while val == True:
    dict =	{"reed": { "weight": 106,  "height": 1.73}, 
    "helena": {"weight": "Mustang","height": 1964}, 
    "helen": {"weight": "Mustang","height": 1964}}

    name_o = input("What is your name? ").lower()
    if name_o == "reed" or name_o == "lukas" or name_o == "helen":
        val = False

        # name = name_o
        # for i in dict[name_o]:
        # print(i)
        #  print(dict[name_o]['weight'], dict[name_o]['height'])
        intWeight =  dict[name_o]['weight']
        intHeight = dict[name_o]['height']
        print(intHeight)
        print(intWeight)
        BMI = intWeight / (intHeight ** 2)
        if BMI < 18.5:
             classification = 'Underweight'
        elif BMI >= 18.5 and BMI < 25:
            classification = 'Healthy Weight'
        elif BMI > 24.9 and BMI < 30:
            classification = 'Overweight but not obese'
        elif BMI > 29.9 and BMI < 35:
            classification = 'Obese class I'
        elif BMI > 34.9 and BMI < 40:
            classification = 'Obese class II'
        else:
            classification = 'Obese class III'
        print(BMI)
        print(classification) 
    # x =+ 1
    else:
       val = True
 