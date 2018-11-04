print("Jak masz na imię?")
name = str(input())
print("Ile masz lat ?")
age = int(input())

if name == "Marta":
    print("Cześć Marta!")
elif age < 12:
    print("Nie jesteś Martą, dzieciaku")
else:
    print("Nie jesteś ani Martą ani dzieciakiem")