import time
import unittest

import main
import towar
import interface


# Test polegający na próbie skasowania towaru na wagę jakby był towarem na sztuki (oczekiwana informacja o
# przegranej).
class TowarNaWageUnweightedTest(unittest.TestCase):

    def test5(self):
        ui = interface.UserInterface(main.start, main.on_item_click, main.on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.update()

        main.ui = ui
        main.start()
        main.ui.hide_next_client_btn_and_start()
        main.items_list[1] = towar.TowarNaWage()
        main.show_next_item()
        window.update()
        time.sleep(1)

        main.on_item_click(1)
        main.on_item_click(1)

        window.update()
        time.sleep(1)

        self.assertEqual(main.user_lost, True)  # sprawdzenie wartości flagi informującej o przegranej
