class Note:
    """This is a docstring. I have created a new class"""
    title = ""
    content = {}
    references = None  # perhaps this could be a dictionary of other related notes

    def __init__(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def print(self):
        print(f'Note title, {self.title}')

