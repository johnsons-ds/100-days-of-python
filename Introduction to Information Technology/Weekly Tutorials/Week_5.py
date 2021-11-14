# print("What is your name?", end = '?\n') #\n means enter
# print("John")
# print("One\tTwo\tThree") #\t tab 8 spaces


##table

# print("State\tCapital".expandtabs(16)) #columns/headers
# print("New South Wales\tSydney".expandtabs(8))
# print("Victoria\tMelbourne".expandtabs(8))
# print("ACT\tCanberra".expandtabs(16))

#formatting ^ centre align; < left align; > right align
# print("{1:^10s} {2:^10s} {0:^10s}".format("one","two","Three"))

# print(False or True)

weights = [65, 82, 56, 110, 97]
# A simple for loop

# for weight in weights:
#     print(weight)
# # Same output, but using range() and indexing weight
# for i in range(5):
#     print(weights[i])
# # Same output, but using len() and indexing weight
# # len() returns the length of the list
# for i in range(len(weights)):
#     print(weights[i])

heights = [165, 178, 199, 182, 174]
for weight, height in zip(weights, heights):
    print(weight, height)


# for weight, height in zip(weights, heights):
#     bmi = weight / ((height)/100)**2 
#     print('BMI = ', bmi)