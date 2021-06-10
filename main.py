import Interface

if __name__ == "__main__":
    ui = Interface.UserInterface()
    window = ui.window
    window.geometry('1000x500')
    window.resizable(False, False)
    window.title("Symulator kasjera")
    window.mainloop()
