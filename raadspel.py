import random

# Vragen aan de gebruiker met welke moeilijkheidsgraad hij het graag wild spelen.
difficulty = input("Kies de moeilijkheidsgraad: (makkelijk, gemiddeld, moeilijk) ")

"""
Een functie die de gebruiker een getal laat raden, 
tot de gebruiker het heeft geraden of de pogingen voorbij zijn.

Bij difficulty makkelijk: mag de gebruiker 3 keer proberen om een getal te raden tussen 1 t/m 10.
Bij difficulty gemiddeld: mag de gebruiker 5 keer proberen om een getal te raden tussen 1 t/m 25.
Bij difficulty moeilijk: mag de gebruiker 10 keer proberen om een getal te raden tussen 1 t/m 100.

Argumenten:
    - difficulty (str) makkelijk, gemiddeld of moeilijk
"""

def raden(difficulty):



    # for-loop om de pogingen bij te houden
    for i in range(pogingen):

        # De gebruiker vragen om een getal te kiezen.
        antwoord_gebruiker = int(input(f"Kies een getal tussen ({getalstart} t/m {(getalstop)-1}): "))

        # De gebruikers antwoord vergelijken met het willekeurige getal.
        # Heeft de gebruiker het goed? Dan wordt de loop verbroken.
        if antwoord_gebruiker == getal:
            print(f"Je hebt getal geraden! Het was: {getal}.")
            break

# Hier wordt de functie raden aangeroepen om het spel te starten.
raden(difficulty)