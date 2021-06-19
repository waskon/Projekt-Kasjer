import unittest
import time

import main
import interface
import towar


# Test polegający na skasowaniu towaru na sztuki po klikając na niego kilka razy.
class TowarNaSztukiValidateOneByOneTest(unittest.TestCase):

    def test1(self):
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

        for i in range(current_item.quantity):
            main.on_item_click(1)
            window.update()
            time.sleep(0.4)

        self.assertEqual(main.current_item_index, 2)  # sprawdzenie przejścia do następnego indeksu na liście
