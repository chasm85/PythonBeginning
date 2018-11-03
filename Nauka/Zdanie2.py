print("Jak masz na imię?")
name = input()
print("Ile masz lat?")
age = input()
print("Podaj hasło:")
password = input()
if name == 'Marta':
    print("Witaj, Marta!")
    if password == "miecznik":
        print("Masz dostęp.")
    else:
        print("Nieprawidłowe hasło.")
elif 12 >= int(age):
    print("Nie jesteś Alicją. dzieciaku.")
elif int(age) > 12:
    print("Jesteś wampirem?")
elif int(age) > 100:
    print("dziadku")
else:
    print("Nie znamy się")
