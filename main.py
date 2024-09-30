import customtkinter

def button_callback():
    print("button clicked")

def main():
    app = customtkinter.CTk()
    app.geometry("800x400")

    customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
    customtkinter.set_appearance_mode("light")

    raadspel_button = customtkinter.CTkButton(app, text="Raadspel", command=button_callback)
    raadspel_button.pack(padx=20, pady=20)

    galgje_button = customtkinter.CTkButton(app, text="Galgje", command=button_callback)
    galgje_button.pack(padx=20, pady=20)

    dagboek_button = customtkinter.CTkButton(app, text="Dagboek", command=button_callback)
    dagboek_button.pack(padx=20, pady=20)

    app.mainloop()

if __name__ == "__main__":
    main()