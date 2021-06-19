import time
import unittest

import towar
import main
import interface


# test polegający na Skasowaniu towaru na sztuki wpisując jego liczność i klikając raz. Wymagane jest
#     resetowanie pola do wartosci 1.
class TowarNaSztukiValidateAtOnceTest(unittest.TestCase):

    def test2(self):
        ui = interface.UserInterface(main.start, main.on_item_click, main.on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.update()

        main.ui = ui
        main.start()
        main.ui.hide_next_client_btn_and_start()
        main.items_list[1] = towar.TowarNaSztuki()
        main.show_next_item()
        window.update()
        time.sleep(1)
        current_item: towar.TowarNaSztuki = main.current_item

        main.on_item_click(current_item.quantity)
        window.update()
        time.sleep(1)

        self.assertEqual(main.current_item_index, 2)  # sprawdzenie przejścia do następnego indeksu na liście
        self.assertEqual(int(main.ui.ent_weigh.get()), 1)  # sprawdzenie resetowania pola do wartości 1
