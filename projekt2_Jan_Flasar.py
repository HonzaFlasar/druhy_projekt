"""
projekt2_Jan_Flasar.py druhý projekt do Engeto online Python Akademie

autor: Jan Flašar
email: honza.flasar@volny.cz
discord: Honza #2485
"""

# Co dělá tento program:
# Vygeneruje náhodné čtyřmístné číslo, které je složeno z unikátních číslic a nezačíná nulou.
# Vyzve hráče k napsání tipu, zkontroluje splnění podmínek a případně ohlásí jejich nesplnění.
# Po každém tipu ohlásí počet bull(s) a cow(s) se zohledněním jednotného/množného čísla.
# Po uhodnutí čísla uvede počet kol a slovní hodnocení výkonu.
# Zobrazí historii výsledků.
# Nabídne novou hru.

historie = list() # zaznamenává všechny výsledky
while True:
    # import náhodných čísel
    pocitac = list()
    import random
    nahodny = (random.randint(1, 9)) # první číslo nemůže být nula
    pocitac.append(nahodny)

    while len(pocitac) != 4:
        nahodny = (random.randint(0, 9))
        if nahodny not in pocitac:
            pocitac.append(nahodny)
        else:
            continue # pokračuje v cyklu tak dlouho, dokud nemá 4 unikátní číslice
    # print(pocitac) při testování vypsat!

    # definice proměnných
    hrac = str
    hodnoceni = str
    bull = int
    cow = int
    pokus = 0

    # úvodní text
    #os.system("cls")
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
    print("-" * 47)

    # začátek cyklu tipování
    while bull != 4:
        bull = 0
        cow = 0

        # zadání hráčova tipu
        hrac = input("Enter a number: ")
        pokus += 1

        #kontrola hráčova typu - číslo, délka, nula
        if hrac.isnumeric() and len(hrac) == 4 and int(hrac[0]) != 0:
            # print("Číslo vyhovuje pravidlům hry.")

            # hledáme bulls
            if int(hrac[0]) == pocitac[0]: # hrac je string, proto před porovnáním nutný převod na int
                bull += 1
            if int(hrac[1]) == pocitac[1]:
                bull += 1
            if int(hrac[2]) == pocitac[2]:
                bull += 1
            if int(hrac[3]) == pocitac[3]:
                bull += 1
            else:
                pass

            # hledáme cows
            for cislo in hrac:
                if cislo in str(pocitac): # hrac je str, pocitac int, proto převod
                    cow = cow + 1
                else:
                    pass

            # úprava cow (odečtení bulls)
            cow = cow - bull

        # výpis výsledku se zohledněním množného čísla

            if bull > 1 and cow > 1:
                print(f"Bulls: ", bull, "Cows: ", cow)
            elif bull > 1 and cow <2:
                print(f"Bulls: ", bull, "Cow: ", cow)
            elif bull < 2 and cow > 1:
                print(f"Bull: ", bull, "Cows: ", cow)
            else:
                print(f"Bull: ", bull, "Cow: ", cow)
            print("***")

            # slovní hodnocení
            if bull == 4:
                if pokus < 4:
                    hodnoceni = "amazing!"
                elif pokus < 8:
                    hodnoceni = "good."
                elif pokus < 12:
                    hodnoceni = "average."
                elif pokus < 16:
                    hodnoceni = "not so good."
                else:
                    hodnoceni = "terrible."
                print("Correct, you've guessed the right number in", pokus, "guesses!")
                print("That's", hodnoceni)
            else:
                pass
        else:
            print("Incorrect number!")

    historie.append(pokus)
    print("Guesses in the previous games: ", historie)
    print("***")

    nova_hra = input("Next game? Press 'y' or quit the game. ")
    if nova_hra == "y":
        continue
    else:
        break