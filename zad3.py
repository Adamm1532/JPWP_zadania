import PIL as pil
from PIL import Image, ImageOps
import customtkinter as ctk
# Zadanie3:
# Bank potrzebuje funkcjonalności zdjęcia w profilu użytkownika
# W pliku obraz.py napisz metodę My_Upload tak aby:
# Wyświetlał się obraz urzytkownik.py(co jest już zrobione)
# Po kliknięciu w obraz wyświetlało się okno do uploadowania obrazu z komputera uzytkownika
# Obraz zostal obcięty do kształtu koła
# Obraz zapisywał się jako uzytkownik.py
# Na ekranie pokazal sie nowy plik uzytkownik.py

# Pisz tylko w funkcji upload


# hints: 
# wycinanie obrazu tak aby zostało kółko: https://stackoverflow.com/questions/30602460/create-circular-image-pil-tkinter
# upload obrazu: https://youtu.be/d4L1J9ABhD8?t=1573
# do zmiany obrazka w objekcie button najłatwiej użyć 
# self.Profile_Button.configure(tu wpisujemy co chcemy zmienić)
# inne pomocne metody/funckje:
# .askopenfilenape()
# .save()
# .open()
window = ctk.CTk()
window.title("Profil")
window.geometry("420x740+700+20")

Background_Frame = ctk.CTkFrame(window, width=420, height=740)
Background_Frame.place(relx=0, rely=0, anchor="nw")

# Funkcja do wczytywania obrazka
def My_Upload():
    mask = Image.open('mask.png').convert('L')
    pass



Profile_Img = ctk.CTkImage(dark_image=pil.Image.open("uzytkownik.png"), size=(200, 200))
Profile_Button = ctk.CTkButton(Background_Frame, image=Profile_Img, text="", width=200, height=200,
                               command=My_Upload,
                               fg_color="transparent")
Profile_Button.place(relx=0.5, rely=0.25, anchor="center")





window.mainloop()
