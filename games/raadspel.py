import customtkinter as ctk
#import importlib
import random

from main import GUI

class Raadspel:

#============= Initialiseren van de Raadspel klas =============#

    def __init__(self):
        self.app = GUI().main()
        self.app.title(f'AppNest - Raadspel')
        self.app.geometry('1200x800')
        #self.app.protocol('WM_DELETE_WINDOW', self.close_window())

        ctk.CTkLabel(self.app, text='Raadspel', font=('Helvetica', 30)).pack(pady=10)

        self.difficulty_easy = 'easy'
        self.difficulty_medium = 'medium'
        self.difficulty_difficult = 'difficult'
        self.difficulty = ''

        self.number = 0
        self.attempts = 0
        self.max_attempts = 0
        self.stop_number = 0

        self.start_window()


#============= Window logica =============#


    def start_window(self):
        """
        Deze methode laat de gebruiker een moeilijkheidsgraad kiezen

        param: Geen
        return: Geen
        """

        self.clear_window()

        difficulties = [self.difficulty_easy, self.difficulty_medium, self.difficulty_difficult]
        ctk.CTkLabel(self.app, text='Kies een moeilijkheidsgraad:', font=('Helvetica', 15)).pack(pady=10)

        for difficulty in difficulties:
            difficulty_button = ctk.CTkButton(self.app, text=difficulty.capitalize(), font=('Helvetica', 15), command=lambda m=difficulty: self.set_difficulty(m))
            difficulty_button.pack(pady=5)

        self.app.update()


    def go_back(self):
        GUI().app.mainloop()
        self.app.quit()


    def clear_window(self):
        for element in self.app.winfo_children()[1:]:
            element.destroy()


    def close_window(self):
        self.app.quit()
        exit()


#============= spel logica =============#


    def set_difficulty(self, difficulty):
        """
        Deze methode stel de moeilijkheidsgraad in

        param difficulty: str: De difficulty gekozen door de gebruiker
        return: Geen
        """

        if difficulty == self.difficulty_easy:
            self.max_attempts = 3
            self.stop_number = 11
        elif difficulty == self.difficulty_medium:
            self.max_attempts = 5
            self.stop_number = 26
        elif difficulty == self.difficulty_difficult:
            self.max_attempts = 10
            self.stop_number = 101
        else:
            return

        self.difficulty = difficulty
        self.number = self.get_number(self.stop_number)
        self.attempts = 0
        self.start_game()


    @staticmethod
    def get_number(stop_number):
        """
        Deze methode pakt een willekeurig getal

        param stop_number: int: eind van random range
        return: int: een willekeurig getal
        """

        return random.randrange(1, stop_number)


    def start_game(self):
        """
        Deze methode start het spel

        param: Geen
        return: Geen
        """

        self.clear_window()

        ctk.CTkLabel(self.app, text=f'Pogingen: {self.get_attempts_remaining()}', font=('Helvetica', 15)).pack(pady=5)
        ctk.CTkLabel(self.app, text=f'range: 1 t/m {self.stop_number-1}', font=('Helvetica', 15)).pack(pady=5)

        choice_text_field = ctk.CTkEntry(self.app, font=('Helvetica', 15))
        choice_text_field.pack(pady=10)

        choice_button = ctk.CTkButton(self.app, text='Raad', font=('Helvetica', 15), command=lambda: self.check_choice(choice_text_field.get()))
        choice_button.pack()

        self.app.update()


    def get_attempts_remaining(self):
        return f'{self.attempts} / {self.max_attempts}'


    def check_choice(self, choice):
        """
        Deze methode controleert de gok van de gebruiker

        param choice: str: de gok van de gebruiker
        return: Geen
        """

        choice = int(choice)
        self.attempts += 1

        if choice == self.number:
            self.successfully_guessed()
        elif self.attempts == self.max_attempts:
            self.out_of_attempts()
        else:
            self.start_game()


    def out_of_attempts(self):
        """
        Deze methode laat aan de gebruiker weten dat de gebruiker door zijn pogingen is

        param: Geen
        return: Geen
        """

        self.clear_window()

        ctk.CTkLabel(self.app, text=f'Helaas! Je bent door je pogingen heen.\n \n Het getal was: {self.number}', font=('Helvetica', 15), text_color='red').pack()

        play_again_button = ctk.CTkButton(self.app, text='Speel opnieuw', font=('Helvetica', 15), command=lambda: self.start_game())
        play_again_button.pack(pady=5)

        go_back_button = ctk.CTkButton(self.app, text='Terug', font=('Helvetica', 15), command=lambda: self.go_back())
        go_back_button.pack(pady=5)


    def successfully_guessed(self):
        """
        Deze methode laat aan de gebruiker weten dat hij het getal geraden heeft

        param: Geen
        return: Geen
        """

        self.clear_window()

        ctk.CTkLabel(self.app, text='Gefeliciteerd! Je hebt het getal succesvol geraden.', font=('Helvetica', 15), text_color='green').pack()

        play_again_button = ctk.CTkButton(self.app, text='Speel opnieuw', font=('Helvetica', 15), command=lambda: self.start_window())
        play_again_button.pack(pady=5)

        go_back_button = ctk.CTkButton(self.app, text='Terug', font=('Helvetica', 15), command=lambda: self.go_back())
        go_back_button.pack(pady=5)


if __name__ == '__main__':
    GUI().app.mainloop()