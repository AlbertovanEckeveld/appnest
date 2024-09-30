"""
Een functie die de gebruiker een getal laat raden, 
tot de gebruiker het heeft geraden of de pogingen voorbij zijn.

Bij difficulty makkelijk: mag de gebruiker 3 keer proberen om een getal te raden tussen 1 t/m 10.
Bij difficulty gemiddeld: mag de gebruiker 5 keer proberen om een getal te raden tussen 1 t/m 25.
Bij difficulty moeilijk: mag de gebruiker 10 keer proberen om een getal te raden tussen 1 t/m 100.

Argumenten:
    - difficulty (str) makkelijk, gemiddeld of moeilijk
"""

import customtkinter as ctk
import random

def start_game(difficulty):
    getal = get_Getal(difficulty)
    app_spel2 = create_window(f"Raadspel {difficulty}")
    raadspel_label2 = ctk.CTkLabel(app_spel2, text=f"Raadspel niveau: {difficulty}")
    raadspel_label2.pack(pady=2)

    app_spel2.lift()
    app_spel2.mainloop()


def get_Getal(difficulty):
    # moeilijkheidsgraad defineren
    if difficulty == "makkelijk":
        pogingen = 3
        getalstart = 1
        getalstop = 11
    elif difficulty == "gemiddeld":
        pogingen = 5
        getalstart = 1
        getalstop = 26
    elif difficulty == "moeilijk":
        pogingen = 10
        getalstart = 1
        getalstop = 101

    # Een random getal kiezen, geacht de moeilijkheidsgraad.
    getal = random.randrange(getalstart, getalstop)

    return getal


def create_window(title):
    window = ctk.CTk()
    window.geometry("800x400")
    window.title(title)
    return window


def start_button_callback():
    app_spel = create_window("Raadspel")
    raadspel_label = ctk.CTkLabel(app_spel, text="Kies de moeilijkheidsgraad")
    moeilijkheid_makkelijk_button = ctk.CTkButton(app_spel, text="Makkelijk", command=start_game("makkelijk"))
    moeilijkheid_gemiddeld_button = ctk.CTkButton(app_spel, text="Gemiddeld", command=start_game("gemiddeld"))
    moeilijkheid_moeilijk_button = ctk.CTkButton(app_spel, text="Moeilijk", command=start_game("moeilijk"))
    raadspel_label.pack(pady=2)
    moeilijkheid_makkelijk_button.pack(pady=3)
    moeilijkheid_gemiddeld_button.pack(pady=3)
    moeilijkheid_moeilijk_button.pack(pady=3)

    app_spel.lift()
    app_spel.mainloop()


application = create_window("Raadspel")

raadspel_button = ctk.CTkButton(application, text="Klik hier om te starten", command=start_button_callback)
raadspel_button.pack(padx=40, pady=40)

application.mainloop()

"""
difficulty = input("Kies de moeilijkheidsgraad: (makkelijk, gemiddeld, moeilijk) ")

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

"""