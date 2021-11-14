# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = open("Input/Names/invited_names.txt", "r")

for i in names_list:
    #Open starting_letter
    with open("Input/Letters/starting_letter.txt", "r") as file:
        contents = file.read()
        #Replace [name] with i
        new_letter = contents.replace("[name]", i)
        # print(new_letter)
        new_file = open(f'Output/ReadyToSend/letter_for_{i}.txt', 'w')
        new_file.write(new_letter)
    #Save file as i_letter.txt
    # print(i)

# print(names_list.readlines())


# text.replace()  # Use this function to replace the [name] placeholder with the names found in invited_names.txt

# 1. Open 'starting_letter' in write mode

# 2.
