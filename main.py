import noteController


def print_note():
    nc.print_note()


def show_sections():
    sections = nc.get_keys_in_parent_section()
    for s in sections:
        print(s + '\n')


def load():
    t = {'load': None,
         'new_note': {'title': ''}}
    c = input("Enter title of note: ")
    # TODO: check for any notes with the title,
    # but for now just create new note
    t['new_note']['title'] = c
    return noteController.NoteController(t)


def level_up():
    nc.move_address_up_level()


def get_user_input():
    input_type = 'add_header'
    input_type_messages = {
        0: "Add section header:",
        1: f'Input content:',
    }

    input_types = {
        'add_header': {'description': 'change user input to section header if this is not the current input type. '
                                      'If it is the current input type then this will add a new section header to the '
                                      'lowest order parent key in the note`s address',
                       'command': 'add_header',
                       'message': 'Add section header'},
        'print_note': {'description': 'print current note in dictionary form',
                       'command': 'print_note', 'response_function': print_note},
        'add_content': {'description': 'change user input to content',
                        'command': 'add_content', 'message': 'Input content'},
        'show_sections': {'description': "display all first order sections given a specified parent "
                                         "'key'",
                          'command': 'show_sections',
                          'response_function': show_sections},
    }
    while True:
        user_input = input(f"[Note location: {nc.current_note_address()}] {input_types[input_type]['message']}: ")
        # print(f'input is: {user_input}')
        # print(f'current input type is: {input_type}')
        # input type change
        if user_input in input_types and input_types[user_input].get('response_function') is not None:
            # certain commands require an immediate response to the
            # user but do not necessitate a change in input type
            print(f"do {user_input}")
            # call function
            input_types[user_input]['response_function']()  # why does PC not like this statement?

        elif user_input in input_types and user_input is not input_type:
            # the user has changed input types that does not require immediate response.
            # i.e. a input type that will in the future effect the actual Note abject
            print(f"input type was changed to: {user_input} from {input_type}")
        # input type was not changed
        else:
            print(f"Input_type: {input_type}")
            """actions = {0: 'add_header', 1: 'add_content'}"""
            content = {'action': input_type, 'value': user_input}
            nc.import_content(content)


def main():
    get_user_input()


# instantiate NoteController object
nc = load()

# run main
main()
