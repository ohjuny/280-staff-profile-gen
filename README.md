# 280-staff-profile-gen
Generates HTML for eecs280.org based on form data in csv format.

Usage:
```terminal
python3 eecs280profile.py [INPUT_FILENAME.csv] [OUTPUT_FILENAME]
```

Input (csv):
```
Timestamp,Email Address,uniqname,Preferred Name (First and Last),Preferred Pronouns,Preferred OS,Preferred IDE,"(optional) Hometown (format: Ann Arbor, MI or Seoul, South Korea)","Profile Picture (jpg, 360x360, uniqname.jpg)",Emoji 1 Name,Emoji 1 Description,Emoji 2 Name,Emoji 2 Description,Emoji 3 Name,Emoji 3 Description,Emoji 4 Name,Emoji 4 Description,Emoji 5 Name,Emoji 5 Description
8/31/2023 19:08:16,ohjun@umich.edu,ohjun,Oh Jun Kweon,he/him,macOS,VS Code,"Dubai, UAE",https://drive.google.com/open?id=1DPf4u1xDKd5J7lTXwrytQLbeu0jZNKqg,bell,I can play the bell tower,coffee,My blood is 83% coffee,sushi,Greatest invention by humans,alarm_clock,Worst invention by humans,spades,Advice: learn how to play euchre...
```
Output:
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
              <span data-tooltip="MacOS"><i class="icon apple"></i></span>
              <span data-tooltip="VS Code"><i class="icon-vscode"></i></span>
              <span data-tooltip="Hometown: Dubai, UAE"><i class="icon map pin"></i></span>
            </div>
          </div>
          <div class="emoji content">
            <span data-tooltip="I grew up in Dubai"><em data-emoji="dromedary_camel"></em></span>
            <span data-tooltip="I can play the bell tower"><em data-emoji="bell"></em></span>
            <span data-tooltip="I skydived (skydove?) for the first time last year"><em data-emoji="parachute"></em></span>
            <span data-tooltip="Tell me about your favorite book!"><em data-emoji="books"></em></span>
          </div>
        </div><!-- /fluid card -->
```

Indentation on output is set by default for easy copy-pasting into eecs280 codebase, but can be configured by DEFAULT_NUM_SPACES global variable.

Notes:
- There are some ambiguous cases such as OS being inputted as "macOS+Linux", IDE being inputted as "VS Code, CLion (not profficient)", emoji name being inputted as "emoji1, emoji2" (2 emojis for 1 description), etc. In these cases, the program will insert the string TODO for easy ctrl+f searching.
