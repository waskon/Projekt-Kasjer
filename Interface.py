import tkinter as tk
import tkinter.font as fnt
import Towar
global ui


class UserInterface:

    def __init__(self, start):

        self.cleared_entry = True

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
                if i == 3 and j == 0:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="Wyczyść", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.clear_entry())
                    numerical_btn.pack()
                elif i == 3 and j == 2:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="Backspace", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.backspace_entry())
                    numerical_btn.pack()
                elif i == 3 and j == 1:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="0", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("0"))
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

                elif i == 0 and j == 0:
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

        numerical_btn_frame = tk.Frame(
            master=self.frame_right_numerical_btns,
            relief=tk.RAISED,
            borderwidth=1
        )

        # przesunięcie ramki zwaz
        numerical_btn_frame.grid(row=0, column=3, padx=10, pady=5)
        weigh_btn = tk.Button(master=numerical_btn_frame, text="Zważ", padx=15, pady=10,
                              font=fnt.Font(size=10))
        weigh_btn.pack()

        # pole wyśw wpisane wyniki
        self.ent_weigh = tk.Entry(master=self.frame_right, font=fnt.Font(size=20), text="1")
        self.ent_weigh.place(width=300, height=50, relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.ent_weigh.insert(0, 1)
        self.ent_weigh.configure(state=tk.DISABLED)

        # następny klient
        self.next_client_btn = tk.Button(master=self.frame_left, text="Następny klient", padx=15, pady=10, width=13,
                                         background="gray83",
                                         font=fnt.Font(size=10), command=lambda: self.show_item(Towar.items_list[0]))
        self.next_client_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        self.item_btn = tk.Button(master=self.frame_left, padx=15, pady=10, width=13, background="gray83",
                                  font=fnt.Font(size=10))

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

    def clear_entry(self):

        self.ent_weigh.configure(state=tk.NORMAL)
        self.ent_weigh.delete(0, tk.END)
        self.ent_weigh.insert(0, 1)
        self.ent_weigh.configure(state=tk.DISABLED)
        self.cleared_entry = True

    def backspace_entry(self):

        self.ent_weigh.configure(state=tk.NORMAL)
        if len(self.ent_weigh.get()) == 1:
            self.ent_weigh.delete(0, tk.END)
            self.ent_weigh.insert(0, 1)
        else:
            self.ent_weigh.delete(len(self.ent_weigh.get()) - 1, tk.END)
            self.cleared_entry = True

        self.ent_weigh.configure(state=tk.DISABLED)


#towary pojawiające się

    def show_item(self, text):
        # ukryj przycisk nastepny klient
        self.next_client_btn.pack_forget()
        # self.start_callback()
        # pokaz kolejny towar
        self.item_btn['text'] = text
        self.item_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

    def show_towar_na_wage_item(item: Towar.TowarNaWage):

        ui.show_item(item.name + " ?kg")

    def show_towar_na_sztuki_item(item: Towar.TowarNaSztuki):

        ui.show_item(item.name + " x" + str(item.quantity))



