text = ["Python"]
text2 = text
print(id(text))
print(id(text2))
print(text is text2)
print()

text += [" is awesome"]
print(id(text))
print(id(text2))
print(text is text2)
print()

print(text)
print(text2)

print('------------------------------------------------------------------------------------------')

text = "Python"
text2 = text
print(id(text))
print(id(text2))
print(text is text2)
print(type(text))
print()

text += " is awesome"
print(id(text))
print(id(text2))
print(text is text2)
print()

print(text)
print(text2)
print()

print('------------------------------------------------------------------------------------------')


numbers = [1, 2, 3]
numbers2 = [1, 2, 3]
print(numbers == numbers2)
print(numbers is numbers2)
print(type(numbers), type(numbers2))