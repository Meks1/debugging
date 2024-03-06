
# Mērķis: 
# iespēja konvertēt USD uz EUR un otrādi pēc 1.08 kursa

eur_to_usd_rate = 1.08

print("Choose command")
while True:
    print("=======")
    print("1 - convert EUR into USD")
    print("2 - convert USD into EUR")
    print("3 - exit")
    command = input("")

    if int(command) == 2:
        usd = input("Enter USD:")
        eur = float(usd) / eur_to_usd_rate
        print(usd, "USD equals EUR", eur)
    elif int(command) == 1:
        usd = input("Enter EUR:")
        eur = float(usd) * eur_to_usd_rate
        print(usd, "USD equals EUR", eur)
    else:
        break

# Kādas kļūdas izdevies atrast?
# while false never work
# Can't do math calculations with string
