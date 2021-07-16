from pynput import keyboard
import threading
import note
from pynput.keyboard import Controller

#global variable
glob_level = 0

# the keyboard controller specifically to simulate pressing buttons
kb = Controller()
from pynput.keyboard import Controller

def function_1():
    global glob_level
    print("function 1")
    glob_level = 0
    end_execute()


def function_2():
    print("function 2")
    global glob_level
    glob_level = 1
    end_execute()


def end_execute():
    # simulate pressing enter so the user input type will change
    # TODO: decide what should be done with anything user has input so far and now they are changing input type
    kb.press(keyboard.Key.enter)
    kb.release(keyboard.Key.enter)

def start():
    c = input("Enter title of note: ")
    # TODO: check for any notes with the title,
    # but for now just create new note
    return note.Note(c)


def get_user_input(header=None):
    d = {
        0: "section header(*):",
        1: f'[{header}]| input content:',
    }

    while True:
        c = input(f"{d[glob_level]}")
        print(f'input is: {c}')


def main():
    thread2 = threading.Thread(target=get_user_input, args=())
    thread2.start()
    with keyboard.GlobalHotKeys({
        '<shift>+R': function_1,
        '<shift>+T': function_2}) as h:
        h.join()



my_note = start()
main()
