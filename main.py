import noteController


def print_note():
    nc.print_note()


def load():
    t = {'load': None,
         'new_note': {'title': ''}}
    c = input("Enter title of note: ")
    # TODO: check for any notes with the title,
    # but for now just create new note
    t['new_note']['title'] = c
    return noteController.NoteController(t)


def get_user_input():
    input_type = 0
    input_type_messages = {
        0: "Add section header:",
        1: f'Input content:',
    }

    while True:
        c = input(f"[Note location: {nc.current_note_address()}] {input_type_messages[input_type]}")
        print(f'input is: {c}')
        # check if user is changing input type
        header_cmd = '**header'
        content_cmd = '**content'
        print_cmd = '**print'
        if header_cmd in c:
            input_type = 0
        elif content_cmd in c:
            input_type = 1
        elif print_cmd in c:
            print_note()
        # TODO not accounting for if they both in user input because that's ridiculous!
        else:
            actions = {0: 'add_header', 1: 'add_content'}
            content = {'action': actions[input_type], 'value': c}
            nc.import_content(content)


def main():
    get_user_input()


# instantiate NoteController object
nc = load()

# run main
main()
