#extracting first names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

#multiple of three
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)