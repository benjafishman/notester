import datetime


class Note:
    """A class to build a JSON string of a note"""
    date_modified = None
    json_note = {}
    edit_pointer = None
    """
    stub content:
    First mishnah in second perek of avos
        - "rebbi says whats the straight path a person should follow in this world"
        - anything that brings him glory and makes others glorify him
        - one should be alacritous to do easy mitzvos as if they were hard ones since we don't know the reward for mitzvos
        - cheshbon the loss of doing a mitzvoh versus the gain of not doing it and the gain of doing and aveira versus the loss of not doing it
    
    note = {
	"meta_data": {
		"title": "Pirkei Avos",
		"date_created": "todays_date"
	},
	"content": {
		"First mishnah": {
			"0": "rebbi says whats the staright path a person should follow in this world",
			"1": "anything that brings him glory and makes others glorify him",
			"2": "one should be alacritous to do easy mitzvos as if they were hard ones since we dont know the reward for mitzvos",
			"3": "cheshbon the loss of doing a mitzvoh versus the gain of not doing it and the gain of doing and aveira versus the loss of not doing it"
		},
		"Second mishnah": {
			"0": "raban gamliel son of Rebbi yehudah hanasi says torah is beatiful with derech eretz because together they make one forget sin",
			"1": "torah without work will in the end be nullified and lead to sin",
			"3": "anyone who is involved with the tzibur should do so lshem shamayim",
			"4": "because their zches avos will assist them and their righteousness stands forever",
			"5": "and as for the leader he will get rewarded as if he did it himself"
		}
	}
}

    """
    references = None  # perhaps this could be a dictionary of other related notes

    def __init__(self, title, content=None):
        self.edit_pointer = 0

        # set meta data content
        self.json_note['meta_data'] = {
            'title': title,
            'date_created': datetime.date.today()
        }

    def add_section_with_content(self, key, content):
        self.json_note[key] = content

    def traverse_note(self):
        for k, v in self.json_note.iteritems():
            print(k, v)

    def get_sections(self):
        """Returns list of sections relative to user's depth in the note"""
        keys = []
        for k, v in self.json_note.items():
            print(f'key is: {k}, v is: {v}')
            keys.append(k)
        return keys

    def add_or_edit_by_address(self, keys, val):
        """
        Nested_set takes a dictionary with a list of keys whose order parallels how the dictionary is nested and
        then assigns the value to that location. This will can add a new dictionary or update an existing entry in a
        dictionary
        """
        dic = self.json_note
        for key in keys[:-1]:
            #print(f'start dic: {dic}')
            #print(f'key is {key}')
            dic = dic.setdefault(key, {})
            #print(f'end dic: {dic}')
        #print("here!!!!")
        #print(dic)
        #print(keys[-1])
        dic[keys[-1]] = val

    def print(self):
        print(self.json_note)