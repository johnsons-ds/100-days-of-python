# #An introduction to the user to the program Dr. Khasan has created is displayed. It will provide a brief
# introduction and instructions.


print(
    "******************************************************************************************************************"
    "************\n\nWelcome to the bmi calculator! It's so good to see you interested in understanding more about your "
    "health\n\n\tBefore we begin, there's a few things to note:\n\t\t1. Your family member, Reed, has given me all your "
    "weights and heights! So no need to run to get those measurements to calculate your bmi.\n\t\t2. I heard some of you"
    " prefer to see the numeric value of your bmi, the bmi classification or both as an output. You can do this by "
    "choosing the right option when prompted.\n\t\t3. If you want to know what everyone's bmi is, you can choose the "
    "'all' option when prompted! (Shh! Don't tell Reed I added that feature in, he didn't ask for it.\n\t\t4. See "
    "everyone's BMI\n\nAll the best!!\n\n*****************************************************************************"
    "*************************************************".expandtabs(
        2))

all_bmi = {"reed": (106, 1.73),
           "helena": (74, 1.63),
           "lukas": (90, 1.80),
           "tennyson": (82, 1.77),
           "cyriacus": (98, 1.75),
           "lubov": (70, 1.54)}


# A bmi calculation function to be used by main()
def calc_bmi(weight, height):
    return weight / (height ** 2)


# A bmi classification function based on the calculated BMI value and the stored BMI classification parameters.
def bmi_classification(calculated_bmi):
    if calculated_bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= calculated_bmi < 25:
        return 'Healthy Weight'
    elif 24.9 < calculated_bmi < 30:
        return 'Overweight but not obese'
    elif 29.9 < calculated_bmi < 35:
        return 'Obese class I'
    elif 34.9 < calculated_bmi < 40:
        return 'Obese class II'
    else:
        return 'Obese class III'


# The main function to run within the while loop.
def main():
    # Check if the input name is in the stored dictionary. If the name is present, proceed with the function.
    if sName in all_bmi.keys():

        # Calculate all the values and store them for later use
        bmi = calc_bmi(intWeight, fHeight)
        classification = bmi_classification(bmi)

        # Create an empty output list to be used for choice 4
        output = []

        # From the user input 'intChoice', produce the selected output for the user.
        if intChoice == 1:
            print(f"Your BMI is, {round(bmi, 1)}")

        elif intChoice == 2:
            print(classification)

        elif intChoice == 3:
            print(f"Your BMI is, {round(bmi, 1)}, within the '{classification}' classification")

        elif intChoice == 4:

            # For each person, calculate their BMI and save it as variable 'bmi'
            for key in all_bmi.keys():
                # Each calculated BMI is stored as float, rounded to 1 decimal as the BMI given by the Department of
                # Health has 1 decimal - so it is relevant.
                each_persons_bmi = round(calc_bmi(all_bmi[key][0], all_bmi[key][1]), 1)

                # Store each value into the list output, to be written to a new file or overwrite existing file
                output.append(f"The BMI for {key.capitalize()} is {each_persons_bmi}\n")

            # From output list, write it to a new file for storage. This line of code satisfies requirement 25 of the
            # assignment
            with open('everyones_bmi_stored.txt', 'w') as file:
                file.writelines(output)

            # From new file 'everyones_bmi_stored.txt', read all values as requested by the user. This line of code
            # satisifies requirement 24 of the assignment.
            with open('everyones_bmi_stored.txt', 'r') as file:
                for line in file.readlines():
                    print(line.strip())


bol = True

while bol:
    # The user enters their name instead of providing their weight and height as Reed has already given Dr. Khasan
    # this information.
    sName = input(
        "Welcome! Please tell me who I'm helping today - Reed, Helena, Lukas, Tennyson, Cyriacus or Lubov? ").lower()

    # The user then chooses what they want to see as the output.
    intChoice = int(input(
        "Please choose an option:\n\t1 - to see only the BMI calculation\n\t2 - to see only the BMI "
        "classification\n\t3 - to see both\n\t4 - to see everyone's BMI \n".expandtabs(
            2)))

    # Get the weight and height from the dictionary and store it for later use in the code.
    intWeight = all_bmi[sName][0]
    fHeight = all_bmi[sName][1]

    main()

    # Ask the user if they would like to make another calculation.
    choiceTWo = input("Would you like to check another person's BMI? (Y/N): \n").lower()

    # Depending on their choice, the function can run again, otherwise, the function terminates and says by to the user.
    if choiceTWo == 'y':
        bol = True

    else:
        bol = False
        print("Thank you for checking your BMI. Have a lovely day!")
