import csv
import sys

# Example input:
# Timestamp,Email Address,uniqname,Preferred Name (First and Last),Preferred Pronouns,Preferred OS,Preferred IDE,"(optional) Hometown (format: Ann Arbor, MI or Seoul, South Korea)","Profile Picture (jpg, 360x360, uniqname.jpg)",Emoji 1 Name,Emoji 1 Description,Emoji 2 Name,Emoji 2 Description,Emoji 3 Name,Emoji 3 Description,Emoji 4 Name,Emoji 4 Description,Emoji 5 Name,Emoji 5 Description
# 8/31/2023 19:08:16,ohjun@umich.edu,ohjun,Oh Jun Kweon,he/him,macOS,VS Code,"Dubai, UAE",https://drive.google.com/open?id=1DPf4u1xDKd5J7lTXwrytQLbeu0jZNKqg,bell,I can play the bell tower,coffee,My blood is 83% coffee,sushi,Greatest invention by humans,alarm_clock,Worst invention by humans,spades,Advice: learn how to play euchre...

# Example card:
        # <div class="ui card">
        #   <div class="image">
        #     <img src="assets/headshots/ohjun.jpg" alt="Oh Jun Kweon head shot" />
        #   </div>
        #   <div class="content">
        #     <div class="header">
        #       Oh Jun Kweon
        #     </div>
        #     <div class="meta">
        #       he/him
        #     </div>
        #     <div class="description">
        #       <a class="email" href="mailto:ohjun@umich.edu" target="_blank" data-tooltip="ohjun@umich.edu"><i class="icon envelope"></i></a>
        #       <span data-tooltip="MacOS"><i class="icon apple"></i></span>
        #       <span data-tooltip="VS Code"><i class="icon-vscode"></i></span>
        #       <span data-tooltip="Hometown: Dubai, UAE"><i class="icon map pin"></i></span>
        #     </div>
        #   </div>
        #   <div class="emoji content">
        #     <span data-tooltip="I grew up in Dubai"><em data-emoji="dromedary_camel"></em></span>
        #     <span data-tooltip="I can play the bell tower"><em data-emoji="bell"></em></span>
        #     <span data-tooltip="I skydived (skydove?) for the first time last year"><em data-emoji="parachute"></em></span>
        #     <span data-tooltip="Tell me about your favorite book!"><em data-emoji="books"></em></span>
        #   </div>
        # </div><!-- /fluid card -->

INPUT_FILENAME = ''
OUTPUT_FILENAME = ''
DEFAULT_NUM_SPACES = 8

ICONS = {
    'macos': 'icon apple',
    'windows': 'icon windows',
    'linux': 'icon linux',
    'vs code': 'icon-vscode',
    'vscode': 'icon-vscode',
    'xcode': 'icon-xcode',
    'visual studio': 'icon-visual-studio',
    'vs': 'icon-visual-studio',
    'clion': 'icon-clion',
    'emacs': 'icon-emacs',
    'vim': 'icon-vim',
}


class Emoji:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc.replace('"', '&quot;')  # avoid nested " in HTML
    
    def __str__(self):
        return f'{self.name}: {self.desc}'

class Person:
    def __init__(self, uniqname, name, pronoun, os, ide, hometown):
        self.uniqname = uniqname
        self.name = name
        self.pronoun = pronoun
        self.os = os
        self.ide = ide
        if hometown:
            self.hometown = hometown
        self.emojis = []

    def add_emoji(self, name, desc):
        self.emojis.append(Emoji(name, desc))

    def __str__(self):
        output = ''
        output += f'uniqname: {self.uniqname}\n'
        output += f'name: {self.name}\n'
        output += f'pronoun: {self.pronoun}\n'
        output += f'os: {self.os}\n'
        output += f'ide: {self.ide}\n'
        output += f'hometown: {self.hometown}\n'
        output += 'emojis:\n'
        for emoji in self.emojis:
            output += '   ' + str(emoji) + '\n'
        return output[:-1]


def populate_people():
    people = []
    with open(INPUT_FILENAME) as csv_file:
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

def code_card(person, num_spaces=0):
    indent = ' ' * num_spaces
    output = ''
    output += indent + '<div class="ui card">\n'
    output += code_image(person, num_spaces+2)
    output += code_content(person, num_spaces+2)
    output += code_emojis(person, num_spaces+2)
    output += indent + '</div><!-- /fluid card -->\n'
    return output

def code_image(person, num_spaces=0):
    indent = ' ' * num_spaces
    output = ''
    output += indent + '<div class="image">\n'
    output += indent + f'  <img src="assets/headshots/{person.uniqname}.jpg" alt="{person.name} head shot" />\n'
    output += indent + '</div>\n'
    return output

def code_content(person, num_spaces=0):
    indent = ' ' * num_spaces
    output = ''
    output += indent + '<div class="content">\n'
    # Name
    output += indent + '  <div class="header">\n'
    output += indent + f'    {person.name}\n'
    output += indent + '  </div>\n'
    # Pronoun
    output += indent + '  <div class="meta">\n'
    output += indent + f'    {person.pronoun}\n'
    output += indent + '  </div>\n'

    output += indent + '  <div class="description">\n'
    # Email
    output += indent + f'    <a class="email" href="mailto:{person.uniqname}@umich.edu" target="_blank" data-tooltip="{person.uniqname}@umich.edu"><i class="icon envelope"></i></a>\n'
    # OS
    if person.os.lower() in ICONS:
        output += indent + f'    <span data-tooltip="{person.os}"><i class="{ICONS[person.os.lower()]}"></i></span>\n'
    else:
        output += indent + f'    <span data-tooltip="{person.os}"><i class="TODO"></i></span>\n'
    # IDE
    if person.ide.lower() in ICONS:
        output += indent + f'    <span data-tooltip="{person.ide}"><i class="{ICONS[person.ide.lower()]}"></i></span>\n'
    else:
        output += indent + f'    <span data-tooltip="{person.ide}"><i class="TODO"></i></span>\n'
    # Hometown
    if person.hometown:
        output += indent + f'    <span data-tooltip="Hometown: {person.hometown}"><i class="icon map pin"></i></span>\n'
    output += indent + '  </div>\n'

    output += indent + '</div>\n'
    return output

def code_emojis(person, num_spaces=0):
    indent = ' ' * num_spaces
    output = ''
    output += indent + '<div class="emoji content">\n'
    for emoji in person.emojis:
        output += code_emoji(emoji, num_spaces+2)
    output += indent + '</div>\n'
    return output

def code_emoji(emoji, num_spaces=0):
    indent = ' ' * num_spaces
    if ',' in emoji.name:  # multiple emojis for given description
        return indent + f'<span data-tooltip="{emoji.desc}"><em data-emoji="TODO: {emoji.name}"></em></span>\n'
    else:
        return indent + f'<span data-tooltip="{emoji.desc}"><em data-emoji="{emoji.name}"></em></span>\n'


if __name__ == "__main__":
    INPUT_FILENAME = sys.argv[1]
    OUTPUT_FILENAME = sys.argv[2]

    people = populate_people()

    # OPTION: sort by last name
    # people.sort(key=lambda person : person.name.split(' ')[-1])

    with open(OUTPUT_FILENAME, 'w') as out_file:
        for person in people:
            out_file.write(code_card(person, DEFAULT_NUM_SPACES))
            out_file.write('\n\n')  # for visual separation


