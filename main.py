from pynput import keyboard
import threading
import noteController
from pynput.keyboard import Controller, Key
import time

# global variable
input_type_toggle = 0

# the keyboard controller specifically to simulate pressing buttons
kb = Controller()


def add_header():
    # print("here 2")
    global input_type_toggle
    input_type_toggle = 0

    """if did_input_type_switch(input_type_toggle, temp_input_type):
        # set the global variable to the new value
        input_type_toggle = 0
        # delete the the hotkey from the user input"""
    end_execute()


def add_content():
    # print("here")
    global input_type_toggle
    input_type_toggle = 1
    end_execute()


def print_note():
    nc.print_note()


def end_execute():
    # simulate pressing enter so the user input type will change
    # TODO: decide what should be done with anything user has input so far and now they are changing input type
    kb.press(Key.delete)
    kb.release(Key.delete)
    print("here3")
    kb.press("R")
    kb.release("R")
    kb.press(Key.delete)
    kb.release(Key.delete)
    kb.press(Key.delete)
    kb.release(Key.delete)
    kb.press(Key.delete)
    kb.release(Key.delete)
    kb.press(Key.enter)
    kb.release(Key.enter)
    # print("here4")


def load():
    t = {'load': None,
         'new_note': {'title': ''}}
    c = input("Enter title of note: ")
    # TODO: check for any notes with the title,
    # but for now just create new note
    t['new_note']['title'] = c
    return noteController.NoteController(t)


def did_input_type_switch(old_input_type, new_input_type):
    """Returns True or False if the global variable 'input_type_toggle' has switched or not"""

    pass


def delete_letter():
    #print("Here")
    kb.press('a')
    kb.release('a')
    kb.press(Key.backspace)
    kb.release(Key.backspace)
    return None


def get_user_input(header=None):
    d = {
        0: "Add section header:",
        1: f'[{header}]| input content:',
    }

    while True:
        previous_input_toggle = input_type_toggle

        c = input(f"[Note location: {nc.current_note_address()}] {d[input_type_toggle]}")
        print(f'input is: {c}')
        print(f'input_type_toggle is: {input_type_toggle}')
        actions = {0: 'add_header', 1: 'add_content'}
        content = {'action': actions[input_type_toggle], 'value': c}
        nc.import_content(content)
        """if previous_input_toggle == input_type_toggle:
            actions = {0: 'add_header', 1: 'add_content'}
            content = {'action': actions[input_type_toggle], 'value': c}
            nc.import_content(content)
        else:
            print("switched function")
"""


def main():
    thread2 = threading.Thread(target=get_user_input, args=())
    thread2.start()
    with keyboard.GlobalHotKeys({
        '<shift>+A': add_header,
        '<shift>+S': add_content,
        '<shift>+Z': print_note,
        '<shift>+D': delete_letter}) as h:
        h.join()


nc = load()
main()
