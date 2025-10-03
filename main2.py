fruit = "pomme, banane fraise, figue, melon"
aliment = fruit.split()
print(aliment)
new_fruit = aliment [0:3]
print(new_fruit)
aliment.append("mangue")
print(aliment)
aliment.pop(1)
print(aliment)
aliment.sort()
print(aliment)


print(18 > 160)
print("18" > "160")

colors = ("blue", "red", "green", "green", "red")
numbers = (4, 6, 9)
print(colors)
print(colors.count("blue"))
print(colors.count("green"))
print(colors.count("red"))
print(colors.index("blue"))
tuple3 = colors + numbers
print(tuple3)

test = ("blue", 26, 6.8)
print(test)


person = {"name": "Lili",
"age": "24",
"city": "paris"}
person["occupation"] = "engineer"
person["hobbies"] = "reading", "traveling", "swimming"
print(person)

books = [{"title": "L'affaire Alaska Sanders", "author": "Joel Dicker", "year": "2022"}, 
{"title": "Ne le dit à personne", "author": "Harlan Coben", "year": "2007"}, {"title": "Ceux qui vont mourir te saluent", "author": "Fred Vargas", "year": "2005"}]
print(books)

