from turtle import Screen, Turtle

# #timmy is the object and Turtle is the class
# timmy = Turtle()
# print(timmy)

# #using the . notation allows you to get the attribute associated with your declared object (timmy)
# my_screen = Screen()

# timmy.shape("turtle")
# timmy.color("red")

# timmy.position()
# timmy.forward(100)

# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"]) 
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)

