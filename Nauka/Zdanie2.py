print("Jak masz na imię?")
name = input()
print("Ile masz lat?")
age = input()
age = int(age)
print("Podaj hasło:")
password = input()
if name == 'Marta':
    print("Witaj, Marta!")
    if password == "miecznik":
        print("Masz dostęp.")
    else:
        print("Nieprawidłowe hasło.")
elif 12 <= age:
    print("Nie jesteś Alicją. dzieciaku.")
elif age > 12 and age < 100:
    print("Jesteś wampirem?")
elif age > 100:
    print("dziadku")
else:
    print("Nie znamy się")
