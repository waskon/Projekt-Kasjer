import time
import unittest

import main
import towar
import interface


# Test polegający na próbie zważenia towaru na sztuki (oczekiwana informacja o przegranej).
class TowarNaSztukiWeightedTest(unittest.TestCase):

    def test4(self):
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

        main.on_weigh_click()

        self.assertEqual(main.user_lost, True)  # sprawdzenie wartości flagi informującej o przegranej
