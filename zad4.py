import time
from threading import Thread
import PIL as pil
import customtkinter as ctk
import Globalne as glb
from datetime import datetime

#W linijkach 70-77 masz fragmenty kodu
#Poniżej umieszczony jest kod z brakującymi fragmentami
#Wklej poszczególne fragmenty w miejsca nazwane: kod (cyfra)
#Za cyfrą jest podpowiedź co ma znaleźć się w danym miejscu
#Jako odpowiedź możesz wysłać tylko poprawną kolejność
#Uważaj kodu brakuje również  w metodzie expand()!


class Scroll(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bank Login")
        self.geometry("420x740+700+20")
        self.ostatni_click = "nic"

        self.background_frame = ctk.CTkFrame(self,
                                             fg_color=glb.color_background,
                                             border_color=glb.color_background,
                                             width=420, height=740)
        self.background_frame.place(relx=0, rely=0, anchor="nw")



        self.Saldo_Label = ctk.CTkLabel(self.background_frame,
                                         height=30, width=80,
                                         corner_radius=10,
                                         text="Stan Konta: " + str(glb.Saldo) + " zł",
                                         font=("Arial", 20, "bold"),
                                         text_color=glb.color_text, 
                                         fg_color=glb.color_background)
        self.Saldo_Label.place(relx=0.5, rely=0.22, anchor="center")



        self.historia_scrol=ctk.CTkScrollableFrame(master=self, 
                                                   bg_color=glb.color_background,
                                                   border_color=glb.color_magenta,
                                                   border_width=0,
                                                   width=300,
                                                   height=400,
                                                   fg_color= glb.color_background2,
                                                   label_text="Historia tranzakcji",
                                                   label_fg_color=glb.color_yellow,
                                                   scrollbar_button_color=glb.color_magenta,
                                                   corner_radius=10,)
        self.historia_scrol.place(relx=0.5, rely=0.6, anchor="center")


        self.buttons = []  # List to store button instances
        self.labels = []
        
        self.rodzaj = []  # List to store button instances
        self.ilosc = []   # List to store label instances
        # getting the current date and time
        current_datetime = datetime.now()


        current_date_time = current_datetime.strftime("%H:%M:%S  %m/%d/%Y")
        
        self.arrow1_img = ctk.CTkImage(dark_image=glb.arrow1, size=(30, 30))
        self.arrow2_img = ctk.CTkImage(dark_image=glb.arrow2, size=(30, 30))


        # fragmenty kodu do skopiowania
        # self.buttons[x//2].configure(image=self.arrow2_img)
        # command=lambda x=x: self.expand(x),
        # label2.grid(row=x, column=2, padx=(10, 5), pady=10, sticky=ctk.W)
        # self.historia_scrol, text= glb.historia1[x], fg_color=glb.color_background2
        # self.buttons.append(arrow_button)
        # label.grid_remove()
        # self.labels.append(label_czas)
        for x in range(0,len(glb.historia1),2):
            
            label = ctk.CTkLabel ()# kod 1 dodaj wewnątrz nawiasu argumenty metody do tworzenia label zawierającego glb.historia1[x]
            label.grid(row=x, column=1, padx=(10, 81), pady=10, sticky=ctk.W,)
            self.rodzaj.append(label)

            label2 = ctk.CTkLabel(self.historia_scrol, text=str(glb.historia1[x+1]) + " zł", fg_color=glb.color_background2)
            # kod 2 dodaj label2 do gridu
            self.ilosc.append(label2)


            arrow_button = ctk.CTkButton(self.historia_scrol, image=self.arrow1_img, text="",
                                        width=20, height=20,
                                        fg_color=glb.color_background2,
                                        # kod 3 dodaj metodę aktywowaną po wciśnięciu przycisku
            )
            arrow_button.grid(row=x, column=0, padx=(10, 5), pady=10, sticky=ctk.W)
            # kod 4 dodaj arrow_button do tabeli
            
            label_czas = ctk.CTkLabel(self.historia_scrol, text= current_date_time, fg_color=glb.color_background2,text_color=glb.color_background2,width=0, height=0)
            
            #kod 5 dodaj label_czas do tabeli

    def expand(self,x):
        

        for button in self.buttons:
            button.configure(image=self.arrow1_img)
        for label in self.labels:
            label.configure(text_color=glb.color_background2,width=0, height=0)
            #kod 6 usuń wszystkie czas_label
    
          
        if self.ostatni_click != x:
        
            #kod 7 zmień obraz self.labels[x//2]
            self.labels[x//2].configure(text_color=glb.color_blue,width=2, height=2)
            self.labels[x//2].grid(row=x+1, column=1, padx=(10, 5), pady=10, sticky=ctk.W,)
            self.ostatni_click = x
        else:
            self.ostatni_click = "nic"

   

                

    def destruction(self):
        self.destroy()
        

        


Scroll().mainloop()
