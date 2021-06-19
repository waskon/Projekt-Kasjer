import time
import unittest

import towar
import main
import interface


# Test polegający na próbie skasowania towaru na sztuki wpisując zbyt dużą liczność (oczekiwana informacja o
#     przegranej).
class TowarNaSztukiTooMuchTest(unittest.TestCase):

    def test3(self):
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

        main.handle_towar_na_sztuki_click(main.current_item, current_item.quantity + 1)

        self.assertEqual(main.user_lost, True)  # sprawdzenie wartości flagi informującej o przegranej
