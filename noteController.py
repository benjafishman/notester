import note


class NoteController:
    """A class to interact with a note object"""
    note = None
    statuses = ['header', 'content']
    current_status = None
    current_address = []

    def __init__(self, t):
        """
        t - should be a json dictionary with a key of 'load'
        to load a previously created note or 'new_note' to create a new note
        and then there should be a key 'title' for the new note
        of"""

        if t['load']:
            # TODO: build out when they want to load a note
            pass
        elif t['new_note']:
            # new note is created
            self.note = note.Note(t['new_note']['title'])
            self.current_address.append('content')
        else:
            print("Error in Note Controller initialization")

            # TODO: return error something bad happened here,
            #  might want to make some sort object variable that holds errors

    def print_note(self):
        return self.note.print()

    def import_content(self, t):
        """
        t = {
        'action':'add_header',
        'value': 'h1'
        }
        """
        print(t)
        if t['action'] == 'add_header':
            val = {}
            temp_address = []
            # if len(self.current_address < 1):
            # self.current_address.append(t['value'])  # a list's order is persistent ;)

            print(self.current_address)
            self.note.add_or_edit_by_address(t['value'], self.current_address)

        pass

    def current_note_address(self):
        """ returns a string representation of the current_address list
        with each element separated by a > """

        t = '>'
        return t.join(self.current_address)

    def move_address_down_level(self):
        # if len(self.current_address) > 0:
        pass

    def move_address_up_level(self):
        if len(self.current_address) > 0:
            last = self.current_address[-1]
            self.current_address.remove(last)
            return self.current_address
        else:
            # TODO: return message that there is no where higher to go
            return self.current_address

    def get_keys_in_parent_section(self):
        """I guess current level is the penultimate address item
        so we'll just cherry pick the penultimate element in the address list and return all first order keys within
        (not sub-keys)"""

        #parent_section = self.current_address[-1]  # if current address is only one element
        #if len(self.current_address) > 1:  # if current address has more than one element
        #    parent_section = self.current_address[-2]
        address = self.current_address[:-1]
        # get all first order keys within given parent section
        print(f"address to section is: {address}")
        return self.note.get_sections(address)

    def move_current_note_address_in(self):
        pass
