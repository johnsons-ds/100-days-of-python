##An introduction to the user to the program Dr. Khasan has created is displayed. It will provide a brief introduction and instructions.

print("******************************************************************************************************************************\n\nWelcome to the bmi calculator! It's so good to see you interested in understanding more about your health\n\n\tBefore we begin, there's a few things to note:\n\t\t1. Your family member, Reed, has given me all your weights and heights! So no need to run to get those measurements to calculate your bmi.\n\t\t2. I heard some of you prefer to see the numeric value of your bmi, the bmi classification or both as an output. You can do this by choosing the right option when prompted.\n\t\t3. If you want to know what everyone's bmi is, you can choose the 'all' option when prompted! (Shh! Don't tell Reed I added that feature in, he didn't ask for it.\n\t\t4. See everyone's BMI\n\nAll the best!!\n\n******************************************************************************************************************************".expandtabs(2))

bol = True

while bol == True:
    
#The values are stored within the while loop as values outside of it, have to be declared within the loop.
    dict =	{"reed": { "weight": 106,  "height": 1.73}, 
    "helena": {"weight": 74,"height": 1.63}, 
    "lukas": {"weight": 90,"height": 1.80}, 
    "tennyson": {"weight": 82,"height": 1.77}, 
    "cyriacus": {"weight": 98,"height": 1.75}, 
    "lubov": {"weight": 70,"height": 1.54}}

#The user enters their name instead of providing their weight and height as Reed has already given Dr. Khasan this information.
    sName = input("Welcome! Please tell me who I'm helping today - Reed, Helena, Lukas, Tennyson, Cyriacus or Lubov? ").lower()
    
#The user then chooses what they want to see as the output.
    intChoice = int(input("Please choose an option:\n\t1 - to see only the BMI calculation\n\t2 - to see only the BMI classification\n\t3 - to see both\n\t4 - to see everyone's BMI \n".expandtabs(2)))
    
#BMI calculation and classification to be stored into variables
    if sName == "reed" or sName == "helena" or sName == "lukas" or sName == "tennyson" or "cyriacus" or "lubov":
        
        bol = False
        
        intWeight =  dict[sName]['weight']
        intHeight = dict[sName]['height']
        
#Calculate all the values and store them for later use
        bmi = intWeight / (intHeight ** 2)
        if bmi < 18.5:
                classification = 'Underweight'
        elif bmi >= 18.5 and bmi < 25:
                classification = 'Healthy Weight'
        elif bmi > 24.9 and bmi < 30:
                classification = 'Overweight but not obese'
        elif bmi > 29.9 and bmi < 35:
                classification = 'Obese class I'
        elif bmi > 34.9 and bmi < 40:
                classification = 'Obese class II'
        else:
                classification = 'Obese class III'
        
        
        if intChoice == 1:
         print(f"Your BMI is, {round(bmi,1)}")
        
        elif intChoice == 2:
            print(classification)
        
        elif intChoice == 3:
          print(f"Your BMI is, {round(bmi,1)}, within the '{classification}' classification")
       
        elif intChoice == 4:
          for key in dict.keys():
              y = dict[key]['weight'] 
              z = dict[key]['height']
              bmi = round(y / (z **2))
            #   print(key)
            #   print(y)
            #   print(z)
              print(f"The BMI for {key} is {bmi}")

#Ask the user if they would like to make another calculation.
    choiceTWo = input("Would you like to check another person's BMI? (Y/N): \n").lower()

    if choiceTWo == 'y':
        bol = True

    else:
        bol = False

else:
   bol = True