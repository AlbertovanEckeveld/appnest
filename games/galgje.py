"""
De requirements van galgje:

Denk na over een goede structuur van je code. Maak gebruik van functies zoals in de les is uitgelegd.                               (Gedaan)
Deze nieuwe kennis pas je ook toe in het eerder gemaakte nummer raad spel.                                                          (Gedaan)              
Kies met behulp van de module random een woord uit een tekstbestand. Dit bestand maak jezelf en voeg je toe aan je project.         (Gedaan)
Vraag de gebruiker om diens naam                                                                                                    (Gedaan)
Bepaal hoe vaak de gebruiker mag raden                                                                                              (Gedaan)
Geef terugkoppeling: wat is de status van het woord, welke letters zijn goed geraden, hoeveel keer mag de gebruiker nog raden?      (Gedaan)

Nano XL:

Categoriseer de te raden woorden op makkelijk, gemiddeld, moeilijk en laat de gebruiker hierin kiezen                               (Gedaan)
Noteer in een tekstbestand de naam van de gebruiker, of de gebruiker het woord heeft geraden, het aantal keer raden en de datum     (Gedaan)

"""

import random
from datetime import datetime

datum = datetime.now().strftime("%Y-%m-%d %H:%M")
naam_gebruiker = input("Wat is je naam? ")
geraden_letters = []
aantal_pogingen = 10

def getWillekeurigWoord(moeilijkheid):
    """
        args:
            moeilijkheid:           int, 0 t/m 2

        returns:
            woord uit een lijst:    str met een woord
    """

    if moeilijkheid == 0:
        length = 5
    elif moeilijkheid == 1:
        length = 10
    elif moeilijkheid == 2:
        length = 15

    with open("../data/galgje/woorden.txt", "r") as woord_in_bestand:
        woorden = []
        for woord in woord_in_bestand:
            woord = woord.strip()

            if length >= 15 and len(woord) >= 15:
                woorden.append(woord)
            elif 10 <= length < 15 and 10 <= len(woord) <= 15:
                woorden.append(woord)
            elif 0 < length < 10 and len(woord) < 10:
                woorden.append(woord)
        
        return woorden[random.randrange(0, len(woorden))]

woord = getWillekeurigWoord(int(input("Op welke moelijkheid wil je het spelen? Makkelijk = 0, Gemiddeld = 1 en Moelijk = 2 ")))

def GetWoordStatus(woord, geraden_letters):
    """
        args:
            woord:              str met 1 letter of een woord
            geraden_letters:    lijst met door de gebruiker geraden letters

        returns:
            status van woord van de geraden letters: str met letters en lage streepjes.
    """

    tekst = ''
    for letter in woord:
        if letter in geraden_letters:
            tekst = tekst + letter
        else: 
            tekst = tekst + "_"
    
    return tekst

def getKeuzeGebruiker(poging):
    """
    args:
        poging      str met 1 letter of een woord

    returns:
       -1          betekent geraden
        0           betekent ongeldige input
        1           betekent dubbel geraden letter
        anders      betekent de status van het woord
    """

    if len(poging) == 1:
        if poging in geraden_letters:
            return 1

        if poging in woord and not poging in geraden_letters and (poging != '' or  ' '):
            geraden_letters.append(poging)
            if len(geraden_letters) == len(woord) or GetWoordStatus(woord, geraden_letters) == woord:
                return -1
    else:
        if poging == woord:
            return -1
        
        return 0
    
    return GetWoordStatus(woord, geraden_letters)

def main():
    """
        args:
            None

        returns:
            resultaat gebruiker na spelen:  str met gebruiker en de aantal pogingen
    """
        
    print(f"\nWelkom {naam_gebruiker}, leuk dat je galgje speelt.\nJe hebt in totaal {aantal_pogingen} pogingen om het woord te raden.")
    print(GetWoordStatus(woord, geraden_letters))
    for i in range(aantal_pogingen):
        poging = getKeuzeGebruiker(input("\nDoe een gok: "))
        
        match poging:
            case -1:
                print((f"Je hebt het woord: {woord} goed geraden! Gefeliciteerd {naam_gebruiker}"))
                return (f"{naam_gebruiker};{i+1}/{aantal_pogingen}")
            case 0:
                print("Kies 1 letter of probeer het woord te raden.")
                poging = getKeuzeGebruiker(input("\nDoe opnieuw een gok: "))
            case 1:
                print("De letter heb je al geraden.")
                poging = getKeuzeGebruiker(input("\nDoe opnieuw een gok: "))

        print("\n" + str(poging))
        print(f"\nPogingen: {i+1} / {aantal_pogingen}")
    
    print(f"Helaas zit het spel er op, het woord was: {woord}")
    return (f"{naam_gebruiker};{i+1}/{aantal_pogingen}")
        

def log(content):
    """
        args:
            content:    str met 1 speler en resultaat

        returns:
            None
    """

    content_log = content.split(";")

    if content_log[1] == "10/10":
        content_log[1] = content_log[1] + " - Mislukt"
    else: content_log[1] = content_log[1] + " - Gelukt"

    with open("../data/galgje/log.txt", "a") as log:
        log.write(f"\n{datum} - {content_log[0]} - {content_log[1]}")

log(main())