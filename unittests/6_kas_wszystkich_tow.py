import time
import unittest

import towar
import main
import interface


# Test polegający na skasowaniu wszystkich towarów (oczekiwane okno z podsumowaniem symulacji).
class ValidateAllItemsTest(unittest.TestCase):

    def test6(self):
        ui = interface.UserInterface(main.start, main.on_item_click, main.on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.update()

        main.ui = ui
        main.start()
        main.ui.hide_next_client_btn_and_start()
        window.update()
        time.sleep(1)

        for i in range(len(main.items_list)):
            if main.current_item_type == towar.TowarNaWage:
                main.on_item_click(1)
                main.on_weigh_click()
                window.update()
                time.sleep(0.4)

                main.on_item_click(1)
                window.update()
                time.sleep(0.4)

            else:
                current_item: towar.TowarNaSztuki = main.current_item
                main.on_item_click(current_item.quantity)
                window.update()
                time.sleep(0.4)

        window.update()
        time.sleep(1)

        self.assertEqual(main.validating_finished, True)  # sprawdzenie wartości flagi informującej o skasowaniu
        # wszystkich towarów