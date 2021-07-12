"""
בס"ד
Bentzion Fishman
Bein Hazmanim 2021
"""

from pynput.keyboard import Controller
from pynput import keyboard
import threading
import time

# keeps track of the type of input a user is doing, should probably change name of the var for more clarity
glob_level = 0

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='X')},
    {keyboard.Key.shift, keyboard.KeyCode(char='x')},
]

# The currently active modifiers
current = set()

# the keyboard controller specifically to simulate pressing buttons
kb = Controller()

'''
- Execute function is execute when a user press ctrl^x (although right now it's only x^ctrl?)
- This takes the global variable glob_level and increases it by 1 then mods it by 2 since we have two options
the mod function acts like a toggle between 2 values
- then sets the new glob_level value which will be used by the getUserInput() function which is on a constant loop
'''


def execute():
    global glob_level
    temp = (glob_level + 1) % 2
    glob_level = temp

    # simulate pressing enter so the user input type will change
    # TODO: decide what should be done with anything user has input so far and now they are changing input type
    kb.press(keyboard.Key.enter)
    kb.release(keyboard.Key.enter)


'''
Function on_press checks if any of the HotKeys have been pressed 
then calls the execute function if true
'''


def on_press(key):
    # print([COMBO for COMBO in COMBINATIONS])
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        print(f'the key is: {key}')
        print(f'current is {current}')
        try:
            current.remove(key)
        except:
            #TODO: do something more productive with this error ,uhh, like fix it.
            print("ERROR ERROR ERROR")


def get_user_input():
    d = {
        0: "top_level content(*):",
        1: "sub_level content(-):"
    }

    while True:
        c = input(f"Enter {d[glob_level]}")
        print(f'input is: {c}')


def main():
    thread2 = threading.Thread(target=get_user_input, args=())
    thread2.start()
    with keyboard.Listener(on_press=on_press,
                           on_release=on_release)as listener:
        listener.join()


main()

'''
if __name__ == '__main__':
    # keyboard.write("GEEKS FOR GEEKS\n")
    # Collect events until released
    # keyboard.on_press_key('f', top_level)
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

What do we need to do: 
1. get the title of the note
2. get the content 
    4 main markers for content
        0. ? major questions on the sugya
        1. * overarching idea
        2. # listing within an overarching idea
        3  - subinformation within the overarching idea and depending on number of 
             dashes is related to how nested the current idea is 
'''
