import customtkinter

# Zadanie 2
# W tym zadaniu warto wykazać się kreatywnością! Nasz Bank potrzebuje osobnego okna ustawień.
# Używając różnych elemntów takich jak: CTkSlider, CTkOptionMenu, CTkCheckBox, CTkSwitch, itd.
# stwórz okno, które pozwoli użytkownikowi dostosować ustawienia aplikacji do swoich potrzeb.
# (Wybrane ustawienia nie muszą nic zmieniać w aplikacji, w koncu poruszamy tylko temat GUI :P)
# Minimum 4 różne elementy, ale im więcej tym lepiej! Nie zapomnij też dodać odpowiedni label aby
# użytkownik wiedział co dany element zmienia.

# Linki do dokumentacji:
# Slider - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkSlider
# OptionMenu - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkOptionMenu
# CheckBox - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkCheckBox
# Switch - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkCTkSwitch

window = customtkinter.CTk()
window.geometry("420x740")
window.title("Zad2")

# Label "Ustawienia"
Setting_Label = customtkinter.CTkLabel(window, height=60, width=110, padx=10, pady=10, corner_radius=10,
                                          text="Ustawienia", font=("Arial", 30, "bold"), text_color="white", fg_color="#E62569")
Setting_Label.place(relx=0.5, rely=0.1, anchor="center")

window.mainloop()

