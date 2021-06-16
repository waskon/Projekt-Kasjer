import tkinter as tk
import tkinter.font as fnt

global current_item_index
global ui
global current_item_type
global current_item


class UserInterface:

    def __init__(self, start_callback, item_click_callback, on_weigh_click_callback):

        self.cleared_entry = True
        self.start_callback = start_callback
        self.item_click_callback = item_click_callback
        self.on_weigh_click_callback = on_weigh_click_callback

        self.window = tk.Tk()
        self.frame_left = tk.Frame(master=self.window)
        self.frame_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.frame_right = tk.Frame(master=self.window, background="gray80")
        self.frame_right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.frame_right_numerical_btns = tk.Frame(master=self.frame_right, background="gray50")
        self.frame_right_numerical_btns.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)


        # panel przycisków
        for i in range(4):
            for j in range(3):
                numerical_btn_frame = tk.Frame(
                    master=self.frame_right_numerical_btns,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                numerical_btn_frame.grid(row=i, column=j, padx=5, pady=5)

                if i == 0 and j == 0:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="1", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("1"))
                    numerical_btn.pack()

                elif i == 0 and j == 1:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="2", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("2"))
                    numerical_btn.pack()

                elif i == 0 and j == 2:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="3", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("3"))
                    numerical_btn.pack()

                elif i == 1 and j == 0:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="4", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("4"))
                    numerical_btn.pack()

                elif i == 1 and j == 1:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="5", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("5"))
                    numerical_btn.pack()

                elif i == 1 and j == 2:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="6", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("6"))
                    numerical_btn.pack()

                elif i == 2 and j == 0:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="7", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("7"))
                    numerical_btn.pack()

                elif i == 2 and j == 1:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="8", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("8"))
                    numerical_btn.pack()

                elif i == 2 and j == 2:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="9", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("9"))
                    numerical_btn.pack()

                elif i == 3 and j == 0:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="Wyczyść", padx=15, pady=10,
                                                font=fnt.Font(size=10), command=lambda: self.clear_entry())
                    numerical_btn.pack()

                elif i == 3 and j == 1:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="0", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("0"))
                    numerical_btn.pack()
                elif i == 3 and j == 2:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="Backspace", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.backspace_entry())
                    numerical_btn.pack()

        numerical_btn_frame = tk.Frame(
            master=self.frame_right_numerical_btns,
            relief=tk.RAISED,
            borderwidth=1
        )

        # przesunięcie ramki zwaz
        numerical_btn_frame.grid(row=0, column=3, padx=10, pady=5)
        weigh_btn = tk.Button(master=numerical_btn_frame, text="Zważ", padx=15, pady=10,
                              font=fnt.Font(size=10),
                              command=lambda: self.on_weigh_click_callback())
        weigh_btn.pack()

        # pole wyśw wpisane wyniki
        self.ent_weigh = tk.Entry(master=self.frame_right, font=fnt.Font(size=20), text="1")
        self.ent_weigh.place(width=300, height=50, relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.ent_weigh.insert(0, 1)
        self.ent_weigh.configure(state=tk.DISABLED)

        # pole nastepny klient
        self.next_client_btn = tk.Button(master=self.frame_left, text="Następny klient", padx=15, pady=10, width=13,
                                         background="gray83",
                                         font=fnt.Font(size=10),
                                         command=lambda: self.hide_next_client_btn_and_start())
        self.next_client_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        # przyciski z towarami
        self.item_btn = tk.Button(master=self.frame_left, padx=15, pady=10, width=13, background="gray83",
                                  font=fnt.Font(size=10),
                                  command=lambda: self.item_click_callback(int(self.ent_weigh.get())))

        self.frame_loss = tk.Frame(master=self.window)
        self.frame_end = tk.Frame(master=self.window)

        # przegrana gra
        self.try_again_btn = tk.Button(master=self.frame_loss, text="Rozpocznij ponownie", padx=15, pady=10,
                                       background="gray83",
                                       font=fnt.Font(size=10),
                                       command=lambda: self.start_again())
        self.try_again_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        lbl_loss = tk.Label(master=self.frame_loss, text="Przegrana", font=fnt.Font(size=30))
        lbl_loss.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        self.try_again_btn_end = tk.Button(master=self.frame_end, text="Rozpocznij ponownie", padx=15, pady=10,
                                           font=fnt.Font(size=10),
                                           command=lambda: self.start_again_end())
        self.try_again_btn_end.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        self.lbl_avg_time = tk.Label(master=self.frame_end, font=fnt.Font(size=20))
        self.lbl_avg_time.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        lbl_end = tk.Label(master=self.frame_end, text="Koniec", font=fnt.Font(size=30))
        lbl_end.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

    # Metoda dopisująca cyfrę do okienka
    def add_number_to_entry(self, number):

        self.ent_weigh.configure(state=tk.NORMAL)
        if self.cleared_entry:
            self.ent_weigh.delete(0, tk.END)
            self.ent_weigh.insert(0, number)
            self.cleared_entry = False
        else:
            current_text = self.ent_weigh.get()
            self.ent_weigh.delete(0, tk.END)
            self.ent_weigh.insert(0, current_text + number)

        self.ent_weigh.configure(state=tk.DISABLED)

    # Metoda czyszcząca okienko (entry)
    def clear_entry(self):

        self.ent_weigh.configure(state=tk.NORMAL)
        self.ent_weigh.delete(0, tk.END)
        self.ent_weigh.insert(0, 1)
        self.ent_weigh.configure(state=tk.DISABLED)
        self.cleared_entry = True

    # Metoda usuwająca pojedynczą cyfre z okienka (entry)
    def backspace_entry(self):

        self.ent_weigh.configure(state=tk.NORMAL)
        if len(self.ent_weigh.get()) == 1:
            self.ent_weigh.delete(0, tk.END)
            self.ent_weigh.insert(0, 1)
        else:
            self.ent_weigh.delete(len(self.ent_weigh.get()) - 1, tk.END)
            self.cleared_entry = True

        self.ent_weigh.configure(state=tk.DISABLED)

    # Metoda ukrywająca przycisk "następny klient" i wywołująca callback ze startem aplikacji
    def hide_next_client_btn_and_start(self):


        self.next_client_btn.pack_forget()
        self.start_callback()

    # Metoda pokazująca przycisk "następny klient"
    def show_next_client_btn(self):


        self.item_btn.pack_forget()
        self.next_client_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

    # Metoda zmieniająca tekst przycisku towaru (pokazująca kolejny towar)
    def show_item(self, text):


        self.item_btn['text'] = text
        self.item_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

    # Metoda pokazująca ekran informujący o przegranej
    def show_loss_information(self):

        self.frame_left.pack_forget()
        self.frame_right.pack_forget()
        self.frame_loss.pack(expand=True, fill=tk.BOTH)

    # Metoda pokazująca ekran informujący o skasowaniu wszystkich przedmiotów ( w tym średni czas)
    def show_end_information(self, time_text):

        self.frame_left.pack_forget()
        self.frame_right.pack_forget()
        self.lbl_avg_time['text'] = time_text
        self.frame_end.pack(expand=True, fill=tk.BOTH)

    # Metoda ukrywająca ekran z informacją o przegranej
    def hide_loss_information(self):

        self.frame_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame_right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame_loss.pack_forget()

    # Metoda ukrywająca ekran z informacją o skasowaniu wszystkich towarów
    def hide_end_information(self):

        self.frame_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame_right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame_end.pack_forget()

    # Metoda przywracająca początkowy wygląd interfejsu (rozpoczęcie od początku po przegranej)
    def start_again(self):

        self.clear_entry()
        self.hide_loss_information()
        self.show_next_client_btn()

    # Metoda przywracająca początkowy wygląd interfejsu (rozpoczęcie od początku po skasowaniu wszystkich towarów)
    def start_again_end(self):

        self.clear_entry()
        self.hide_end_information()
        self.show_next_client_btn()









