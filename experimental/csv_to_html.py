from jinja2 import Environment, FileSystemLoader
import os
import csv
import sys

# Example input:
# Timestamp,Email Address,uniqname,Preferred Name (First and Last),Preferred Pronouns,Preferred OS,Preferred IDE,"(optional) Hometown (format: Ann Arbor, MI or Seoul, South Korea)","Profile Picture (jpg, 360x360, uniqname.jpg)",Emoji 1 Name,Emoji 1 Description,Emoji 2 Name,Emoji 2 Description,Emoji 3 Name,Emoji 3 Description,Emoji 4 Name,Emoji 4 Description,Emoji 5 Name,Emoji 5 Description
# 8/31/2023 19:08:16,ohjun@umich.edu,ohjun,Oh Jun Kweon,he/him,macOS,VS Code,"Dubai, UAE",https://drive.google.com/open?id=1DPf4u1xDKd5J7lTXwrytQLbeu0jZNKqg,bell,I can play the bell tower,coffee,My blood is 83% coffee,sushi,Greatest invention by humans,alarm_clock,Worst invention by humans,spades,Advice: learn how to play euchre...


class Icon:
    def __init__(self, readable, icon):
        self.readable = readable
        self.icon = icon

ICONS = {
    'macos': Icon('macOS', 'apple'),
    'windows': Icon('Windows', 'windows'),
    'linux': Icon('Linux', 'linux'),
    'vs code': Icon('VS Code', 'vscode'),
    'vscode': Icon('VS Code', 'vscode'),
    'xcode': Icon('Xcode', 'xcode'),
    'visual studio': Icon('Visual Studio', 'visual-studio'),
    'vs': Icon('Visual Studio', 'visual-studio'),
    'clion': Icon('CLion', 'clion'),
    'emacs': Icon('Emacs', 'emacs'),
    'vim': Icon('Vim', 'vim'),
}

def get_icons(names):
    return [ICONS[name] for name in names]

class Emoji:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc.replace('"', '&quot;')  # avoid nested " in HTML

class Person:
    def __init__(self, uniqname, name, pronoun, oss, ides, hometown):
        self.uniqname = uniqname
        self.name = name
        self.pronoun = pronoun
        self.oss = get_icons(oss.lower().split(', '))
        self.ides = get_icons(ides.lower().split(', '))
        self.hometown = hometown
        self.emojis = []

    def add_emoji(self, name, desc):
        self.emojis.append(Emoji(name, desc))

    def get_dict(self):
        return {
            "uniqname": self.uniqname,
            "name": self.name,
            "pronoun": self.pronoun,
            "oss": self.oss,
            "ides": self.ides,
            "hometown": self.hometown,
            "emojis": self.emojis,
        }

def populate_people(inp_filename):
    people = []
    with open(inp_filename) as csv_file:
        next(csv_file)  # Consume header
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            person = Person(row[2], row[3], row[4], row[5], row[6], row[7])
            person.add_emoji(row[9], row[10])  # Emoji 1
            person.add_emoji(row[11], row[12]) # Emoji 2
            person.add_emoji(row[13], row[14]) # Emoji 3
            if row[15]: # Emoji 4
                person.add_emoji(row[15], row[16])
            if row[17]: # Emoji 5
                person.add_emoji(row[17], row[18])

            people.append(person)
    return people

def main():
    if len(sys.argv) != 3:
        print('Usage: python csv_to_html.py [INPUT_FILENAME] [OUTPUT_FILENAME]')
        exit()
    inp_filename = sys.argv[1]
    out_filename = sys.argv[2]
    TEMPLATE = 'student'  # Change to 'faculty' for faculty template

    people = populate_people(inp_filename)

    # OPTION: sort by last name
    people.sort(key=lambda person : person.name.split(' ')[-1])
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template(f'{TEMPLATE}.html')
    with open(out_filename, 'w') as out_file:
        for person in people:
            out_file.write(template.render(person.get_dict()))

if __name__ == "__main__":
    main()
