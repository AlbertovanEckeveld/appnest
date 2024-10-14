import customtkinter as ctk
from _datetime import datetime
import random

from main import GUI

class Galgje:

#============= Initialiseren van de Galgje klas =============#

    def __init__(self):
        self.app = GUI().main()
        self.app.title('AppNest - Galgje')
        self.app.geometry('1200x800')
        #self.app.protocol('WM_DELETE_WINDOW', self.close_window())

        self.datum = datetime.now().strftime("%Y-%m-%d %H:%M")

        ctk.CTkLabel(self.app, text='Galgje', font=('Helvetica', 30)).pack(pady=10)

        self.difficulty_easy = 'easy'
        self.difficulty_medium = 'medium'
        self.difficulty_difficult = 'difficult'
        self.difficulty = ''

        self.username = ''
        self.attempts = 0
        self.max_attempts = 10
        self.guessed_letters = []
        self.word = ''

        self.start_window()


#============= Window logica =============#


    def start_window(self):
        """
        Deze methode laat de gebruiker een moeilijkheidsgraad kiezen

        param: Geen
        return: Geen
        """

        self.clear_window()

        username_entry = ctk.CTkEntry(self.app, font=('Helvetica', 15))
        username_entry.pack(pady=10)
        submit_username = ctk.CTkButton(self.app, text='Submit', font=('Helvetica', 15), command=lambda: self.get_username(username_entry.get()))
        submit_username.pack(pady=5)

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


    def get_username(self, username):
        self.username = username


    def set_difficulty(self, difficulty):
        """
        Deze methode stel de moeilijkheidsgraad in

        param moeilijkheidsgraad: str: De moeilijkheidsgraad gekozen door de gebruiker
        return: Geen
        """

        self.difficulty = difficulty
        self.word = self.get_word(self.difficulty)
        self.attempts = 0
        self.start_game()


    def get_word(self, difficulty):
        """
        Deze methode pakt een willekeurig woord

        param stop_getal: str: difficulty
        return: str: een willekeurig woord
        """

        length = 0

        if difficulty == self.difficulty_easy:
            length = 5
        elif difficulty == self.difficulty_medium:
            length = 10
        elif difficulty == self.difficulty_difficult:
            length = 15
        elif length == 0:
            return
        else: return



        with open("data/galgje/woorden.txt", "r") as words_in_file:
            words = []
            for word in words_in_file:
                woord = word.strip()

                if length >= 15 and len(word) >= 15:
                    words.append(woord)
                elif 10 <= length < 15 and 10 <= len(word) <= 15:
                    words.append(woord)
                elif 0 < length < 10 and len(word) < 10:
                    words.append(woord)

            return words[random.randrange(0, len(words))]


    def start_game(self):
        """
        Deze methode start het spel

        param: Geen
        return: Geen
        """

        self.clear_window()

        ctk.CTkLabel(self.app, text=f'Speler: {self.username}', font=('Helvetica', 15)).pack(pady=5)
        ctk.CTkLabel(self.app, text=f'Pogingen: {self.get_attempts_remaining()}', font=('Helvetica', 15)).pack(pady=5)
        ctk.CTkLabel(self.app, text=f'Woord: {self.get_word_status()}', font=('Helvetica', 15)).pack(pady=5)

        choice_text_field = ctk.CTkEntry(self.app, font=('Helvetica', 15))
        choice_text_field.pack(pady=10)

        choice_button = ctk.CTkButton(self.app, text='Raad', font=('Helvetica', 15), command=lambda: self.check_choice(choice_text_field.get()))
        choice_button.pack()
        self.app.update()


    def get_attempts_remaining(self):
        return f'{self.attempts} / {self.max_attempts}'


    def get_word_status(self):
        """
        Krijg de status van het woord, met behulp van de geraden woorden lijst
        en de lengte van het woord

        param: Geen
        return: str: status van het woord
        """

        text = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                text = text + letter
            else:
                text = text + "_"

        return text


    def check_choice(self, gok):
        """
        Deze methode controleert de gok van de gebruiker

        param gok: str: de gok van de gebruiker
        return: Geen
        """

        gok = str(gok).lower()

        if gok in self.word and not gok in self.guessed_letters and (gok != '' or  ' '):
            self.guessed_letters.append(gok)

        self.attempts += 1

        if gok == self.word or self.get_word_status() == self.word:
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

        self.log(f'{self.username};{self.get_attempts_remaining()}')

        self.clear_window()

        ctk.CTkLabel(self.app, text=f'Helaas! Je bent door je pogingen heen.\n \n Het woord was: {self.word}', font=('Helvetica', 15), text_color='red').pack()

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

        self.log(f'{self.username};{self.get_attempts_remaining()}')

        self.clear_window()

        ctk.CTkLabel(self.app, text='Gefeliciteerd! Je hebt het woord succesvol geraden.', font=('Helvetica', 15), text_color='green').pack()

        play_again_button = ctk.CTkButton(self.app, text='Speel opnieuw', font=('Helvetica', 15), command=lambda: self.start_window())
        play_again_button.pack(pady=5)

        go_back_button = ctk.CTkButton(self.app, text='Terug', font=('Helvetica', 15), command=lambda: self.go_back())
        go_back_button.pack(pady=5)


    def log(self, content):
        """
        Deze methode logt de resultaten van de speler

        param: content str: met 1 speler en resultaat
        return: Geen
        """

        content_log = content.split(';')

        if content_log[1] == '10/10':
            content_log[1] = content_log[1] + ' - Mislukt'
        else:
            content_log[1] = content_log[1] + ' - Gelukt'

        with open('data/galgje/log.txt', 'a') as log:
            log.write(f'\n{self.datum} - {content_log[0]} - {content_log[1]}')


if __name__ == '__main__':
    GUI().app.mainloop()