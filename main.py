import interface
import towar
from datetime import datetime
import random
import wyjatki

global current_item_index
global ui
global current_item_type
global current_item

should_weigh_item = False  # flaga odpowiedzialna za wymuszanie na użutkowniku zważenia towar
user_lost = False  # flaga ustawiana gdy uzytkownik przegra
validating_finished = False  # flaga ustawiana gdy użytkownik skasuje wszystkie towary

items_list = []
items_counter = 0
start_time = datetime.now()
items_size = 0


def shuffle_list_and_return(x):
    """ Metoda mieszająca kolejność towarów z listy """
    random.shuffle(x)
    return x


def generate_items_list(size):
    """ Metoda generująca listę towarów"""
    unshuffled_list = shuffle_list_and_return([towar.TowarNaSztuki() if x < int(size / 2)
                                               else towar.TowarNaWage() for x in range(size)])  # połowa towarów na sztuki
    return shuffle_list_and_return(unshuffled_list)


def set_current_item_info(index):
    """ Metoda aktualizująca aktualny towar i dane o nim"""
    global current_item_type, current_item
    current_item = items_list[index]
    current_item.append_time = datetime.now()
    current_item_type = type(current_item)


def show_towar_na_wage_item(item: towar.TowarNaWage):
    """ Metoda ta wywołuje metodę w interfejsie - pokazującą kolejny towar(towar na wagę)"""
    ui.show_item(item.name + " ?kg")


def show_towar_na_sztuki_item(item: towar.TowarNaSztuki):
    """ Metoda ta wywołuje metodę w interfejsie - pokazującą kolejny towar(towar na sztuki)"""
    ui.show_item(item.name + " x" + str(item.quantity))


def on_item_click(quantity):
    """ Metoda wywoływana po kliknięciu przycisku towaru"""
    global should_weigh_item, items_counter, user_lost, validating_finished

    try:
        if should_weigh_item:
            should_weigh_item = False
            raise wyjatki.ItemUnweightedError()
        else:
            if current_item_type == towar.TowarNaWage:
                if is_towar_na_wage_weighed(current_item):
                    items_counter += 1
                    current_item.validate_time = datetime.now()
                    ui.clear_entry()
                    show_next_item()
                else:
                    should_weigh_item = True
            else:
                handle_towar_na_sztuki_click(current_item, quantity)
    except wyjatki.ItemUnweightedError:
        user_lost = True
        ui.show_loss_information()


def is_towar_na_wage_weighed(item: towar.TowarNaWage):
    """ Metoda sprawdzająca czy towar na wagę został zważony"""
    return True if item.weighed else False


def on_weigh_click():
    """ Metoda obsługująca kliknięcie przycisku odpowiedzialnego za ważenie towaru"""
    global should_weigh_item, user_lost

    if current_item_type == towar.TowarNaWage:
        handle_on_weigh_click(current_item)
    else:
        print("dzialanie niedozwolone")
        user_lost = True
        ui.show_loss_information()


def handle_on_weigh_click(item: towar.TowarNaWage):
    """ Metoda obsługująca klikniecię przycisku odpowiedzialnego za ważenie towaru, ustawienie wagi na przycisku"""
    global should_weigh_item

    if should_weigh_item:
        should_weigh_item = False
        item.weighed = True
        ui.show_item(item.name + " " + str(item.weight) + " kg")


def show_next_item():
    """ Metoda odpowiedzialna za pokazywanie kolejnego towaru"""
    global items_counter, current_item_index, items_list

    current_item_index += 1
    if current_item_index != len(items_list):
        set_current_item_info(current_item_index)
        show_towar_na_wage_item(current_item) if type(current_item) == towar.TowarNaWage else show_towar_na_sztuki_item(
            current_item)
    else:
        show_end_screen()


def increase_items_count_from_towar_na_sztuki(item: towar.TowarNaSztuki):
    """ Metoda zwiększająca licznik towarów o ilość aktualnego towaru na sztuki"""
    global items_counter
    items_counter += item.quantity


def show_end_screen():
    """ Metoda odpowiedzialną za pokazanie ekranu końcowego"""
    global validating_finished, start_time, items_counter

    validating_finished = True
    difference = (datetime.now() - start_time)
    total_seconds = difference.total_seconds()
    avg_item_time = total_seconds / items_counter
    ui.show_end_information("Średni czas kasowania jednego przedmiotu: " + "{:.3f}".format(avg_item_time) + "s")


def handle_towar_na_sztuki_click(item: towar.TowarNaSztuki, entry_quantity):
    """ Metoda obsługująca klikniecie przycisku z towarem na sztuki"""
    global user_lost

    try:
        if item.quantity - entry_quantity < 0:
            raise wyjatki.ItemTooMuchError()
        else:
            if item.quantity - entry_quantity == 0:
                increase_items_count_from_towar_na_sztuki(current_item)
                ui.clear_entry()
                show_next_item()
            else:
                item.quantity -= entry_quantity
                ui.clear_entry()
                ui.show_item(item.name + " x" + str(item.quantity))

    except wyjatki.ItemTooMuchError:
        user_lost = True
        ui.show_loss_information()


def start():
    """ funkcja rozpoczynająca gre"""
    global items_counter, start_time, items_size, items_list, current_item_index, user_lost, validating_finished

    user_lost = False
    validating_finished = False
    items_counter = 0
    start_time = datetime.now()
    items_size = random.randint(10, 20)
    items_list = generate_items_list(items_size)
    current_item_index = 0
    set_current_item_info(current_item_index)
    show_towar_na_wage_item(
        current_item) if current_item_type == towar.TowarNaWage else show_towar_na_sztuki_item(
        current_item)


if __name__ == "__main__":
    """Metoda główna, tworzenie interfejsu"""

    ui = interface.UserInterface(start, on_item_click, on_weigh_click)
    window = ui.window
    window.geometry('1000x500')
    window.resizable(False, False)
    window.title("Symulator kasjera")
    window.mainloop()
