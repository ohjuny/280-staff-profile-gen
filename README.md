# About
Tools for converting between csv, html, json for staff profile cards on [eecs280.org](https://www.eecs280.org).

## html_to_json.py
Converts HTML card to raw json.

Usage:
```terminal
python3 html_to_json.py [INPUT_FILENAME.csv] [OUTPUT_FILENAME]
```

Note: the email line for faculty cards is slightly different, so may not work for faculty cards.

## csv_to_html.py
Converts raw csv to HTML card.

Usage:
```terminal
python3 csv_to_html.py [INPUT_FILENAME.csv] [OUTPUT_FILENAME]
```

Example Input (csv):
```
Timestamp,Email Address,uniqname,Preferred Name (First and Last),Preferred Pronouns,Preferred OS,Preferred IDE,"(optional) Hometown (format: Ann Arbor, MI or Seoul, South Korea)","Profile Picture (jpg, 360x360, uniqname.jpg)",Emoji 1 Name,Emoji 1 Description,Emoji 2 Name,Emoji 2 Description,Emoji 3 Name,Emoji 3 Description,Emoji 4 Name,Emoji 4 Description,Emoji 5 Name,Emoji 5 Description
8/31/2023 19:08:16,ohjun@umich.edu,ohjun,Oh Jun Kweon,he/him,macOS,VS Code,"Dubai, UAE",https://drive.google.com/open?id=1DPf4u1xDKd5J7lTXwrytQLbeu0jZNKqg,bell,I can play the bell tower,coffee,My blood is 83% coffee,sushi,Greatest invention by humans,alarm_clock,Worst invention by humans,spades,Advice: learn how to play euchre...
```
The input file can be generated using Google Forms. The code generation does not depend on the field names, but does depend on the field ordering.
The code generation also assumes that 3 emojis (name+description) are always avilable, with emoji 4 and 5 being optional.

Example Output:
```html
        <div class="ui card">
          <div class="image">
            <img src="assets/headshots/ohjun.jpg" alt="Oh Jun Kweon head shot" />
          </div>
          <div class="content">
            <div class="header">
              Oh Jun Kweon
            </div>
            <div class="meta">
              he/him
            </div>
            <div class="description">
              <a class="email" href="mailto:ohjun@umich.edu" target="_blank" data-tooltip="ohjun@umich.edu"><i class="icon envelope"></i></a>
              <span data-tooltip="macOS"><i class="icon apple"></i></span>
              <span data-tooltip="VS Code"><i class="icon-vscode"></i></span>
              <span data-tooltip="Hometown: Dubai, UAE"><i class="icon map pin"></i></span>
            </div>
          </div>
          <div class="emoji content">
            <span data-tooltip="I can play the bell tower"><em data-emoji="bell"></em></span>
            <span data-tooltip="My blood is 83% coffee"><em data-emoji="coffee"></em></span>
            <span data-tooltip="Greatest invention by humans"><em data-emoji="sushi"></em></span>
            <span data-tooltip="Worst invention by humans"><em data-emoji="alarm_clock"></em></span>
            <span data-tooltip="Advice: learn how to play euchre..."><em data-emoji="spades"></em></span>
          </div>
        </div><!-- /fluid card -->
```

Indentation on output is set by default for easy copy-pasting into eecs280 codebase, but can be configured by DEFAULT_NUM_SPACES global variable.

Notes:
- Profile picture is referenced as "uniqname.jpg". Must manually move images over (with correct name) into assets folder.
- There are some ambiguous cases such as OS being inputted as "macOS+Linux", IDE being inputted as "VS Code, CLion (not profficient)", emoji name being inputted as "emoji1, emoji2" (2 emojis for 1 description), etc. In these cases, the program will insert the string TODO for easy ctrl+f searching.
