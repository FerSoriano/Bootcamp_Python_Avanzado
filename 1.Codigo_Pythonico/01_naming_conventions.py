
# NO RECOMENDADO
x = "Fernando Soriano"
y, z = x.split()
print(y, z)

# RECOMENDADO - SE EXPLICITO
name = "Michelle Sanchez"
first_name, last_name = name.split()
print(name)

if (name.startswith("M") and name.endswith("z")):
    print("El nombre empieza con M y termina con Z")

if name.find("San") == 9:
    print(True)
