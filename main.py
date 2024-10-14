import os
import re
import importlib
import customtkinter as ctk

class Minigame:

    def __init__(self, path, name, class_name):
        self.path = path
        self.name = name
        self.class_name = class_name


class GUI:

    def __init__(self):
        self.app_name = 'AppNest'
        self.app_version = '1.0.1'

        self.app = ctk.CTk()
        self.app.title(f'{self.app_name} - v. {self.app_version}')
        self.app.geometry("1200x800")
        #self.app.protocol('WM_DELETE_WINDOW', self.close_window())
        self.app_frame_grid_rows = 4

        self.minigames_folder = 'games/'
        self.minigames = []

        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('green')

        self.show_start_screen()


    def main(self):
        return self.app


    def show_start_screen(self):
        ctk.CTkLabel(self.app, text=f'{self.app_name}', font=('Helvetica', 30)).pack()
        ctk.CTkLabel(self.app, text=f'\nVersie: {self.app_version}').pack(pady=10)

        frame = ctk.CTkFrame(self.app)
        frame.pack()

        self.get_minigames()

        for index, app in enumerate(self.minigames):
            minigame_button = ctk.CTkButton(frame, text=app.name.capitalize(), command=lambda i=index: self.start_minigame(i))

            row = index // self.app_frame_grid_rows
            col = index % self.app_frame_grid_rows
            minigame_button.grid(row=row, column=col, padx=5, pady=5)


    def get_minigames(self):
        """
        Deze methode haalt alle minigames op vanuit de folder: games/

        return: Geen
        """

        for file in os.listdir(self.minigames_folder):
            if file.endswith('.py'):
                name = re.sub(r'\.py', '', file)
                self.minigames.append(Minigame(path=f'games.{name}', name=name, class_name=name.capitalize()))


    def start_minigame(self, index):
        """
        Deze methode start de gekozen minigame

        param: int: index
        return: Geen
        """

        app = self.minigames[index]
        try:
            module = importlib.import_module(app.path)
            if hasattr(module, app.class_name):
                self.app.withdraw()
                app_class = getattr(module, app.class_name)
                app_class()

            else:
                print(f'Error: Class {app.class_name} niet gevonden in {app.path}.')
        except Exception as e:
            print(f'Error openen {app.name}: {e}')


    def clear_window(self):
        for element in self.app.winfo_children()[1:]:
            element.destroy()


    def close_window(self):
        self.app.quit()
        exit()


    def __str__(self):
        return self.app_name


if __name__ == '__main__':
    GUI().app.mainloop()
