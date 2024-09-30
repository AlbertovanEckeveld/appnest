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
            pogingen=3
            getalstart=1
            getalstop=11
    elif difficulty == "gemiddeld":
            pogingen=5
            getalstart=1
            getalstop=26
    elif difficulty == "moeilijk":
            pogingen=10
            getalstart=1
            getalstop=101

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




