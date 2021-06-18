import interface
import towar
from datetime import datetime
import random
import wyjatki

global current_item_index
global ui
global current_item_type
global current_item

should_weigh_item = False  # flaga odpowiedzialna za wymuszanie na użutkowniku zważenia towar \
# (w przeciwnym razie przegrana)
user_lost = False  # flaga ustawiana gdy uzytkownik przegra
validating_finished = False  # flaga ustawiana gdy użytkownik skasuje wszystkie towary

items_list = []
items_counter = 0
start_time = datetime.now()
items_size = 0


# """Metoda mieszająca kolejność towarów z listy
def shuffle_list_and_return(x):

    random.shuffle(x)
    return x


# """Metoda generująca listę towarów
def generate_items_list(size):

    unshuffled_list = shuffle_list_and_return([towar.TowarNaSztuki() if x < int(size / 2)
                                               else towar.TowarNaWage() for x in range(size)])  # połowa towarów na sztuki
    return shuffle_list_and_return(unshuffled_list)


# Metoda aktualizująca aktualny towar i dane o nim
def set_current_item_info(index):

    global current_item_type, current_item

    current_item = items_list[index]
    current_item.append_time = datetime.now()
    current_item_type = type(current_item)


# Metoda ta wywołuje metodę w interfejsie - pokazującą kolejny towar(towar na wagę)
def show_towar_na_wage_item(item: towar.TowarNaWage):

    ui.show_item(item.name + " ?kg")


# Metoda ta wywołuje metodę w interfejsie - pokazującą kolejny towar(towar na sztuki)
def show_towar_na_sztuki_item(item: towar.TowarNaSztuki):


    ui.show_item(item.name + " x" + str(item.quantity))


# Metoda wywoływana po kliknięciu przycisku towaru
def on_item_click(quantity):

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


# Metoda sprawdzająca czy towar na wagę został już zważony czy nie (na podstawie flagi ustawianej w obiekcie)
def is_towar_na_wage_weighed(item: towar.TowarNaWage):

    return True if item.weighed else False


# Metoda obsługująca kliknięcie przycisku odpowiedzialnego za ważenie towaru
def on_weigh_click():


    global should_weigh_item, user_lost

    if current_item_type == towar.TowarNaWage:
        handle_on_weigh_click(current_item)
    else:
        print("dzialanie niedozwolone")
        user_lost = True
        ui.show_loss_information()


# Metoda obsługująca klikniecię przycisku odpowiedzialnego za ważenie towaru podczas gdy aktualnym towarem jest towar
# na wagę - ustawienie wagi na przycisku
def handle_on_weigh_click(item: towar.TowarNaWage):

    global should_weigh_item

    if should_weigh_item:
        should_weigh_item = False
        item.weighed = True
        ui.show_item(item.name + " " + str(item.weight) + " kg")


# Metoda odpowiedzialna za wywoływanie metody interfejsu odpowiedzialnej za pokazywanie kolejnego towaru
def show_next_item():

    global items_counter, current_item_index, items_list

    current_item_index += 1
    if current_item_index != len(items_list):
        set_current_item_info(current_item_index)
        show_towar_na_wage_item(current_item) if type(current_item) == towar.TowarNaWage else show_towar_na_sztuki_item(
            current_item)
    else:
        show_end_screen()


# Metoda zwiększająca licznik towarów o ilość aktualnego towaru na sztuki
def increase_items_count_from_towar_na_sztuki(item: towar.TowarNaSztuki):

    global items_counter
    items_counter += item.quantity


# Metoda wywołująca metodę interfejsu odpowiedzialną za pokazanie ekranu końcowego (po skasowaniu wszystkich towarów)
def show_end_screen():

    global validating_finished, start_time, items_counter

    validating_finished = True
    difference = (datetime.now() - start_time)
    total_seconds = difference.total_seconds()
    avg_item_time = total_seconds / items_counter
    ui.show_end_information("Średni czas kasowania jednego przedmiotu: " + "{:.3f}".format(avg_item_time) + "s")


# """Metoda obsługująca klikniecie przycisku z towarem na sztuki
def handle_towar_na_sztuki_click(item: towar.TowarNaSztuki, entry_quantity):

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


# dunkcja rozpoczynająca gre
def start():

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

    ui = interface.UserInterface(start, on_item_click, on_weigh_click)
    window = ui.window
    window.geometry('1000x500')
    window.resizable(False, False)
    window.title("Symulator kasjera")
    window.mainloop()
