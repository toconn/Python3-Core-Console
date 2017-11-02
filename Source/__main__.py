from ua.core.ui.console import Console
from ua.core.ui.listpicker import ListPicker
from ua.core.errors.errors import UserRequestExit


def print_selected (text_list, index):
    
    if index > -1:
        print ("You selected item " + str (index + 1) + ": " + text_list[index])
    elif index == -1:
        print ("You selected nothing.")



console = Console()
listpicker = ListPicker(console)

list1 = ["Item 1", "Item 2", "Item 3", "Item 4"]



print ("Pick frorm one of these...")
print()

try:
    index = listpicker.pick_item (list1)
    print()

    print_selected (list1, index)
except UserRequestExit:
    print ("You cancelled.")
    
print()
