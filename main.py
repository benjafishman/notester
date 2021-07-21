from pynput import keyboard
import threading
import noteController
from pynput.keyboard import Controller

# global variable
glob_level = 0

# the keyboard controller specifically to simulate pressing buttons
kb = Controller()


def add_header():
    global glob_level
    glob_level = 0
    end_execute()


def function_2():
    global glob_level
    glob_level = 1
    end_execute()


def print_note():
    nc.print_note()


def end_execute():
    # simulate pressing enter so the user input type will change
    # TODO: decide what should be done with anything user has input so far and now they are changing input type
    kb.press(keyboard.Key.enter)
    kb.release(keyboard.Key.enter)


def load():
    t = {'load': None,
         'new_note': {'title': ''}}
    c = input("Enter title of note: ")
    # TODO: check for any notes with the title,
    # but for now just create new note
    t['new_note']['title'] = c
    return noteController.NoteController(t)


def get_user_input(header=None):
    d = {
        0: "Add section header:",
        1: f'[{header}]| input content:',
    }

    while True:
        c = input(f"[Note location: {nc.current_note_address()}] {d[glob_level]}")
        print(f'input is: {c}')
        actions = {0: 'add_header', 1: 'add_content'}
        content = {'action': actions[glob_level], 'value': c}
        nc.import_content(content)


def main():
    thread2 = threading.Thread(target=get_user_input, args=())
    thread2.start()
    with keyboard.GlobalHotKeys({
        '<shift>+A': add_header,
        '<shift>+T': function_2,
        '<shift>+Z': print_note}) as h:
        h.join()


nc = load()
main()
