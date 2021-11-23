print("\tWelcome to the Favorite Teachers Program")
profes = []

for i in range(1,5):
    profe = input(f"\tWho is your number {i} favorite teacher:\t").title()
    profes.append(profe)

print(f"\n\tYour favorite teachers ranked are: {profes}")
print(f"\tYour favorite teachers alphabetically order are: {sorted(profes)}")
print(f"\tYour favorite teachers in reverse alphabetically order are: {sorted(profes, reverse=True)}")
print(f"\tYour top two teachers are: {profes[:2]}")
print(f"\tYour next two teachers are: {profes[2:4]}")
print(f"\tYour last favorite teacher is: {profes[len(profes)-1]}")
print(f"\tYour have a total of 4 favorite teachers.")
print(f"\tOops, {profes[0]} is no longer your favorite teacher.")

profe_nuevo  = input("\tWho is your new FAVORITE teacher:\t").title()

profes.insert(0,profe_nuevo)
print(f"\tYour top two teachers are: {profes[:2]}")
print(f"\tYour next two teachers are: {profes[2:4]}")
print(f"\tYour last favorite teacher is: {profes[len(profes)-1]}")
print(f"\tYour have a total of 5 favorite teachers.")

print(f"\tYou've decided you no longer like a teacher.")

borrar_profe  = input("\tWhich teacher would you like to remove from your list:\t").title()

profes.remove(borrar_profe)
print(f"\n\tYour favorite teachers ranked are: {profes}")
print(f"\tYour favorite teachers alphabetically order are: {sorted(profes)}")
print(f"\tYour favorite teachers in reverse alphabetically order are: {sorted(profes, reverse=True)}")
print(f"\tYour top two teachers are: {profes[:2]}")
print(f"\tYour next two teachers are: {profes[2:4]}")
print(f"\tYour last favorite teacher is: {profes[len(profes)-1]}")
print(f"\tYour have a total of 4 favorite teachers.")