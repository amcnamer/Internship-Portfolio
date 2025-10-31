
import tkinter
import tkinter.font as tkfont
import sqlite3
import webbrowser
import simpleaudio

"""Creating the cursor and connecting to the database"""
music_connection = sqlite3.connect('Music.db')
music_cursor = music_connection.cursor()


class ComposerGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry('750x500+0+0')
        self.master.title('Main Menu')
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=20)

        self.top_frame = tkinter.Frame(self.master)
        self.middle1_frame = tkinter.Frame(self.master)
        self.middle2_frame = tkinter.Frame(self.master)
        self.middle3_frame = tkinter.Frame(self.master)
        self.middle4_frame = tkinter.Frame(self.master)
        self.middle5_frame = tkinter.Frame(self.master)
        self.middle6_frame = tkinter.Frame(self.master)
        self.middle7_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        """Creating a radio button for each of the moods and setting their initial values."""
        self.title = tkinter.Label(self.top_frame, text='Please choose a Theme')
        self.love = tkinter.Radiobutton(self.middle1_frame, text='Love Theme', variable=self.radio_var, value=1)
        self.sad = tkinter.Radiobutton(self.middle1_frame, text='Sad Ballad', variable=self.radio_var, value=2)
        self.mystery = tkinter.Radiobutton(self.middle2_frame, text='Mystery/Suspense', variable=self.radio_var,
                                           value=3)
        self.high_action = tkinter.Radiobutton(self.middle2_frame, text='High Intensity Action',
                                               variable=self.radio_var, value=4)
        self.magic = tkinter.Radiobutton(self.middle3_frame, text='Magical Fantasy', variable=self.radio_var, value=5)
        self.supernatural_grandeur = tkinter.Radiobutton(self.middle3_frame, text='Supernatural Grandeur',
                                                         variable=self.radio_var, value=6)
        self.dark_magic = tkinter.Radiobutton(self.middle4_frame, text='Dark Magical Fantasy', variable=self.radio_var,
                                              value=7)
        self.slow_drama = tkinter.Radiobutton(self.middle4_frame, text='Slow Drama', variable=self.radio_var, value=8)
        self.comedy = tkinter.Radiobutton(self.middle5_frame, text='Comedy', variable=self.radio_var, value=9)
        self.moderate_action = tkinter.Radiobutton(self.middle5_frame, text='Moderate Intensity Action',
                                                   variable=self.radio_var, value=10)
        self.lyrical_grandeur = tkinter.Radiobutton(self.middle6_frame, text='Lyrical Grandeur',
                                                    variable=self.radio_var, value=11)
        self.hero = tkinter.Radiobutton(self.middle6_frame, text='Heroic Theme', variable=self.radio_var, value=12)
        self.villain = tkinter.Radiobutton(self.middle7_frame, text='Villain Theme', variable=self.radio_var, value=13)
        self.action_adventure = tkinter.Radiobutton(self.middle7_frame, text='Action Adventure',
                                                    variable=self.radio_var, value=14)
        """Adding the indicator on for the selection style."""
        self.love.configure(indicatoron=True)
        self.sad.configure(indicatoron=True)
        self.mystery.configure(indicatoron=True)
        self.high_action.configure(indicatoron=True)
        self.magic.configure(indicatoron=True)
        self.supernatural_grandeur.configure(indicatoron=True)
        self.dark_magic.configure(indicatoron=True)
        self.slow_drama.configure(indicatoron=True)
        self.comedy.configure(indicatoron=True)
        self.moderate_action.configure(indicatoron=True)
        self.lyrical_grandeur.configure(indicatoron=True)
        self.hero.configure(indicatoron=True)
        self.villain.configure(indicatoron=True)
        self.action_adventure.configure(indicatoron=True)

        self.title.pack()
        self.love.pack(side="left")
        self.sad.pack(side='left')
        self.mystery.pack(side='left')
        self.high_action.pack(side='left')
        self.magic.pack(side='left')
        self.supernatural_grandeur.pack(side='left')
        self.dark_magic.pack(side='left')
        self.slow_drama.pack(side='left')
        self.comedy.pack(side='left')
        self.moderate_action.pack(side='left')
        self.lyrical_grandeur.pack(side='left')
        self.hero.pack(side='left')
        self.villain.pack(side='left')
        self.action_adventure.pack(side='left')

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu, width=10)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy, width=10)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.middle3_frame.pack()
        self.middle4_frame.pack()
        self.middle5_frame.pack()
        self.middle6_frame.pack()
        self.middle7_frame.pack()
        self.bottom_frame.pack()

    """ Open Menu opens the next window based on the selection from the radio_var menu and sends 
    the mood variable (which is used in the database select statements), 
    the mood_title (which is used in the window title), and the tonality associated with each mood."""
    def open_menu(self):
        if self.radio_var.get() == 1:
            mood = '%Love%'
            mood_title = 'Love'
            tonality = 'Major'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 2:
            mood = '%Sad Ballad%'
            mood_title = 'Sad Ballad'
            tonality = 'Minor'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 3:
            mood = '%Mystery%'
            mood_title = 'Mystery/Suspense'
            tonality = 'Chromatic'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 4:
            mood = '%High Intensity Action%'
            mood_title = 'High Intensity Action'
            tonality = 'Chromatic'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 5:
            mood = '%Magical Fantasy%'
            mood_title = 'Magical Fantasy'
            tonality = 'Major'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 6:
            mood = '%Supernatural Grandeur%'
            mood_title = 'Supernatural Grandeur'
            tonality = 'Major'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 7:
            mood = '%Dark Magic and Fantasy%'
            mood_title = 'Dark Magical Fantasy'
            tonality = 'Minor'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 8:
            mood = '%Slow Drama%'
            mood_title = 'Slow Drama'
            tonality = 'Minor'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 9:
            mood = '%Comedy%'
            mood_title = 'Comedy'
            tonality = 'Major'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 10:
            mood = '%Moderate Intensity Action%'
            mood_title = 'Moderate Intensity Action'
            tonality = 'Chromatic'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 11:
            mood = '%Lyrical Grandeur%'
            mood_title = 'Lyrical Grandeur'
            tonality = 'Major'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 12:
            mood = '%Heroic%'
            mood_title = 'Heroic'
            tonality = 'Major'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        elif self.radio_var.get() == 13:
            mood = '%Villain%'
            mood_title = 'Villain'
            tonality = 'Minor'
            _ = MoodGUI(self.master, mood, tonality, mood_title)

        else:
            mood = '%Action Adventure%'
            mood_title = 'Action Adventure'
            tonality = 'Major'
            _ = MoodGUI(self.master, mood, tonality, mood_title)


class MoodGUI:
    def __init__(self, master, mood, tonality, mood_title):
        mood_string = ""
        compositional_elements_string = "Compositional Elements:\n"
        harmony_string = "Harmony:\n"
        instruments_string = "Instruments:\n"
        listening_examples_string = "Listening Examples:\n"

        try:
            """Selects all information from the moods table based on which mood is selected"""
            music_cursor.execute("""SELECT * FROM Moods WHERE MoodName LIKE ?""",
                                 (mood,))
            mood_list = music_cursor.fetchall()

            """For loop formatting the information contained in the mood_list selection and 
            concatenating it to mood_string"""
            for item in mood_list:
                temp = ("Mood: " + item[0] + "\nEmotion: " + item[1] + "\nPace: " + item[2] +
                        "\nOrchestration level: " + item[3] + "\n")
                mood_string += temp

            """Concatenates the tonality to the harmony string for display"""
            harmony_string = harmony_string + ' ' + tonality + ' Scales and Modes.'

            """Selects each element name from the database based on the mood chosen"""
            music_cursor.execute("""SELECT ElementName FROM CompositionalElements WHERE Mood LIKE ?""",
                                 (mood,))
            compositional_elements_list = music_cursor.fetchall()

            """For space I only used the first four elements in the list to display and added a new line before
            re-concatenating it to compositional_elements_string"""
            for item in compositional_elements_list[:4]:
                temp = item[0] + '\n'
                compositional_elements_string += temp

            """Selecting the instrument names based on mood chosen"""
            music_cursor.execute("""SELECT InstrumentName FROM Instruments WHERE LeadMood LIKE ?""",
                                 (mood,))
            instruments_list = music_cursor.fetchall()

            """Similarly to elements, I only used the first 3 instruments in the initial display 
            to compact the data shown."""
            for item in instruments_list[:3]:
                temp = item[0] + '\n'
                instruments_string += temp

            """Selects the piece name based on the mood chosen."""
            music_cursor.execute("""SElECT PieceName FROM ListeningExamples WHERE Mood LIKE ?""",
                                 (mood,))
            listening_examples_list = music_cursor.fetchall()

            """Adds a newline before re-concatenating the contents of the list into a string"""
            for item in listening_examples_list:
                temp = item[0] + '\n'
                listening_examples_string += temp

        except sqlite3.Error:
            print("SQLite Error occurred")

        self.mood = tkinter.Toplevel(master)

        """Using geometry to create the same window everytime and using the mood_title data sent from 
        the ComposerGUI class for the title."""
        self.mood.geometry('1500x1100+750+0')
        self.mood.title(f'Creating a {mood_title} Theme')

        self.mood_frame = tkinter.Frame(self.mood)
        self.middle1_frame = tkinter.Frame(self.mood)
        self.middle2_frame = tkinter.Frame(self.mood)
        self.middle3_frame = tkinter.Frame(self.mood)
        self.middle4_frame = tkinter.Frame(self.mood)
        self.bottom_frame = tkinter.Frame(self.mood)

        """Sets each of the buttons within their own frame, adding width and a background color for each."""
        self.mood_label = tkinter.Label(self.mood_frame, text=mood_string, width=50, bg='#E8E8E8')
        self.listen_button = tkinter.Button(self.middle1_frame, text=listening_examples_string,
                                            command=lambda: self.listen_info(mood, mood_title), width=50, bg='#E0E0E0',
                                            borderwidth=2)
        self.harmony_button = tkinter.Button(self.middle2_frame, text=harmony_string,
                                             command=lambda: self.harmony_info(mood_title, tonality), width=50,
                                             bg='#E0E0E0', borderwidth=2)
        self.instrument_button = tkinter.Button(self.middle3_frame, text=instruments_string,
                                                command=lambda: self.instrument_info(mood, mood_title), width=50,
                                                bg='#E0E0E0', borderwidth=2)
        self.elements_button = tkinter.Button(self.middle4_frame, text=compositional_elements_string,
                                              command=lambda: self.element_info(mood, mood_title), width=50,
                                              bg='#E0E0E0', borderwidth=2)

        self.mood_label.pack(side='left')
        self.listen_button.pack(side='left')
        self.harmony_button.pack(side='left')
        self.instrument_button.pack(side='left')
        self.elements_button.pack(side='left')

        self.quit_button = tkinter.Button(self.bottom_frame, text='Back', command=self.go_back, width=10)

        self.quit_button.pack(side='left')

        self.mood_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.middle3_frame.pack()
        self.middle4_frame.pack()
        self.bottom_frame.pack()

    """Sends the mood and mood_title to the ListenInfoGUI class when listening examples is chosen."""
    def listen_info(self, mood, mood_title):
        _ = ListenInfoGUI(self.mood, mood, mood_title)

    """Sends the mood_title and tonality to the either the HarmonyInfoGUI or the ChromaticHarmonyInfoGUI
    based on what the tonality variable is set to.
    I did this because both the major and minor have the same number of scales and chromatic was a lot less."""
    def harmony_info(self, mood_title, tonality):
        if tonality == 'Major' or tonality == 'Minor':
            _ = HarmonyInfoGUI(self.mood, mood_title, tonality)
        else:
            _ = ChromaticHarmonyInfoGUI(self.mood, mood_title, tonality)

    """Sends the mood and mood_title variables into the InstrumentInfoGUI class when chosen."""
    def instrument_info(self, mood, mood_title):
        _ = InstrumentInfoGUI(self.mood, mood, mood_title)

    """Sends the mood and mood_title variables into the ElementInfoGUI class when chosen."""
    def element_info(self, mood, mood_title):
        _ = ElementInfoGUI(self.mood, mood, mood_title)

    def go_back(self):
        self.mood.destroy()


class ListenInfoGUI:
    def __init__(self, master, mood, mood_title):
        example = []
        url = []

        try:
            music_cursor.execute("""SELECT PieceName, ComposerName, PieceYear, 
            MediaTitle, MediaType, KeyName, Tempo, URL, Notes FROM ListeningExamples WHERE Mood LIKE ?""",
                                 (mood,))
            input_list = music_cursor.fetchall()

            """Using a For loop I get each line in input_list, 
            set each of the values in that line equal to a variable of a similar name
            concatenate all of that information into a string using f string
            append the formatted information from the line to the example list using the information variable
            taking the link_url variable and formatting it to string and appending it to the url list"""

            for line in input_list:
                piece, name, year, title, type, key, tempo, link_url, notes = line
                information = (f'{piece} by {name}\n from the {year} {type} {title}\n '
                               f'In the key of {key} at a tempo of {tempo} bpm\n Notes:\n{notes}')
                example.append(information)
                form_url = f'{link_url}'
                url.append(form_url)

        except sqlite3.Error:
            print("SQLite Error occurred")

        self.listen = tkinter.Toplevel(master)
        self.listen.geometry('1500x1250+750+0')
        self.listen.title("Listening Examples Information Expanded")

        self.top_frame = tkinter.Frame(self.listen)
        self.middle1_frame = tkinter.Frame(self.listen)
        self.middle2_frame = tkinter.Frame(self.listen)
        self.middle3_frame = tkinter.Frame(self.listen)
        self.middle4_frame = tkinter.Frame(self.listen)
        self.bottom_frame = tkinter.Frame(self.listen)

        self.listen_label = tkinter.Label(self.top_frame, text=f'Prior works associated with {mood_title}',
                                          )
        """I used the information contained in the lists together because the first example and the first url elements 
        would coincide with each other."""
        self.example1_button = tkinter.Button(self.middle1_frame, text=example[0], command=lambda: self.play(url[0]),
                                              bg='#E0E0E0', borderwidth=2, width=85)
        self.example2_button = tkinter.Button(self.middle2_frame, text=example[1], command=lambda: self.play(url[1]),
                                              bg='#E0E0E0', borderwidth=2, width=85)
        self.example3_button = tkinter.Button(self.middle3_frame, text=example[2], command=lambda: self.play(url[2]),
                                              bg='#E0E0E0', borderwidth=2, width=85)
        self.example4_button = tkinter.Button(self.middle4_frame, text=example[3], command=lambda: self.play(url[3]),
                                              bg='#E0E0E0', borderwidth=2, width=85)

        self.listen_label.pack()
        self.example1_button.pack()
        self.example2_button.pack()
        self.example3_button.pack()
        self.example4_button.pack()

        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.go_back)

        self.back_button.pack()

        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.middle3_frame.pack()
        self.middle4_frame.pack()
        self.bottom_frame.pack()

    """Using the webbrowser library, I can open a window using the provided link from the database which is 
    associated with that specific example."""
    @staticmethod
    def play(link):
        webbrowser.open(link)

    def go_back(self):
        self.listen.destroy()


class HarmonyInfoGUI:
    def __init__(self, master, mood_title, tonality):
        url = []
        example = []

        try:
            music_cursor.execute("""SElECT ScaleName, ScalePitches, AvailableChords, URL
             FROM Harmony WHERE Tonality LIKE ?""", (tonality,))
            harmony_list = music_cursor.fetchall()

            """exactly the same as the listening examples information from above 
            but much simpler in terms of data."""
            for line in harmony_list:
                scale, pitch, chord, scale_url = line
                information = f'{scale}:({pitch})\n {chord}\n\n'
                example.append(information)
                form_url = f'{scale_url}'
                url.append(form_url)

        except sqlite3.Error:
            print("SQLite Error occurred")

        self.harmony = tkinter.Toplevel(master)
        self.harmony.title("Harmony Examples Information Expanded")
        self.harmony.geometry('2000x1250+250+0')

        self.top_frame = tkinter.Frame(self.harmony)
        self.middle1_frame = tkinter.Frame(self.harmony)
        self.middle2_frame = tkinter.Frame(self.harmony)
        self.middle3_frame = tkinter.Frame(self.harmony)
        self.middle4_frame = tkinter.Frame(self.harmony)
        self.middle5_frame = tkinter.Frame(self.harmony)
        self.middle6_frame = tkinter.Frame(self.harmony)
        self.bottom_frame = tkinter.Frame(self.harmony)

        self.harmony_label = tkinter.Label(self.harmony, text=f'Scales associated with {mood_title}')

        self.harmony1_button = tkinter.Button(self.middle1_frame, text=example[0],
                                              command=lambda: self.play_wav(url[0]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony2_button = tkinter.Button(self.middle1_frame, text=example[1],
                                              command=lambda: self.play_wav(url[1]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony3_button = tkinter.Button(self.middle1_frame, text=example[2],
                                              command=lambda: self.play_wav(url[2]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony4_button = tkinter.Button(self.middle2_frame, text=example[3],
                                              command=lambda: self.play_wav(url[3]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony5_button = tkinter.Button(self.middle2_frame, text=example[4],
                                              command=lambda: self.play_wav(url[4]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony6_button = tkinter.Button(self.middle2_frame, text=example[5],
                                              command=lambda: self.play_wav(url[5]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony7_button = tkinter.Button(self.middle3_frame, text=example[6],
                                              command=lambda: self.play_wav(url[6]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony8_button = tkinter.Button(self.middle3_frame, text=example[7],
                                              command=lambda: self.play_wav(url[7]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony9_button = tkinter.Button(self.middle3_frame, text=example[8],
                                              command=lambda: self.play_wav(url[8]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony10_button = tkinter.Button(self.middle4_frame, text=example[9],
                                               command=lambda: self.play_wav(url[9]),
                                               bg='#E0E0E0', borderwidth=2)
        self.harmony11_button = tkinter.Button(self.middle4_frame, text=example[10],
                                               command=lambda: self.play_wav(url[10]),
                                               bg='#E0E0E0', borderwidth=2)
        self.harmony12_button = tkinter.Button(self.middle4_frame, text=example[11],
                                               command=lambda: self.play_wav(url[11]),
                                               bg='#E0E0E0', borderwidth=2)
        self.harmony13_button = tkinter.Button(self.middle5_frame, text=example[12],
                                               command=lambda: self.play_wav(url[12]),
                                               bg='#E0E0E0', borderwidth=2)
        self.harmony14_button = tkinter.Button(self.middle5_frame, text=example[13],
                                               command=lambda: self.play_wav(url[13]),
                                               bg='#E0E0E0', borderwidth=2)
        self.harmony15_button = tkinter.Button(self.middle5_frame, text=example[14],
                                               command=lambda: self.play_wav(url[14]),
                                               bg='#E0E0E0', borderwidth=2)
        self.harmony16_button = tkinter.Button(self.middle6_frame, text=example[15],
                                               command=lambda: self.play_wav(url[15]),
                                               bg='#E0E0E0', borderwidth=2)
        self.harmony17_button = tkinter.Button(self.middle6_frame, text=example[16],
                                               command=lambda: self.play_wav(url[16]),
                                               bg='#E0E0E0', borderwidth=2)

        self.harmony_label.pack()
        self.harmony1_button.pack(side='left')
        self.harmony2_button.pack(side='left')
        self.harmony3_button.pack(side='left')
        self.harmony4_button.pack(side='left')
        self.harmony5_button.pack(side='left')
        self.harmony6_button.pack(side='left')
        self.harmony7_button.pack(side='left')
        self.harmony8_button.pack(side='left')
        self.harmony9_button.pack(side='left')
        self.harmony10_button.pack(side='left')
        self.harmony11_button.pack(side='left')
        self.harmony12_button.pack(side='left')
        self.harmony13_button.pack(side='left')
        self.harmony14_button.pack(side='left')
        self.harmony15_button.pack(side='left')
        self.harmony16_button.pack(side='left')
        self.harmony17_button.pack(side='left')

        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.go_back)

        self.back_button.pack()

        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.middle3_frame.pack()
        self.middle4_frame.pack()
        self.middle5_frame.pack()
        self.middle6_frame.pack()
        self.bottom_frame.pack()

    """I am using the simpleaudio library to play sound files (.wav) that I recorded for all of the scales. 
    I stop all audio first to that the scales don't overlap, then I create a sound object 
    and then I play the sound object. 
    I also added the stop_all when the window is destroyed so the audio doesn't carry over 
    back to the previous screen."""
    @staticmethod
    def play_wav(wav):
        simpleaudio.stop_all()
        sound_object = simpleaudio.WaveObject.from_wave_file(wav)
        sound_object.play()

    def go_back(self):
        simpleaudio.stop_all()
        self.harmony.destroy()


class ChromaticHarmonyInfoGUI:
    def __init__(self, master, mood_title, tonality):
        url = []
        example = []

        try:
            music_cursor.execute("""SElECT ScaleName, ScalePitches, AvailableChords, URL
             FROM Harmony WHERE Tonality LIKE ?""", (tonality,))
            harmony_list = music_cursor.fetchall()

            for line in harmony_list:
                scale, pitch, chord, scale_url = line
                information = f'{scale}:({pitch})\n {chord}\n\n'
                example.append(information)
                form_url = f'{scale_url}'
                url.append(form_url)

        except sqlite3.Error:
            print("SQLite Error occurred")

        self.harmony = tkinter.Toplevel(master)
        self.harmony.title("Harmony Examples Information Expanded")
        self.harmony.geometry('2000x1250+250+0')

        self.top_frame = tkinter.Frame(self.harmony)
        self.middle1_frame = tkinter.Frame(self.harmony)
        self.middle2_frame = tkinter.Frame(self.harmony)
        self.middle3_frame = tkinter.Frame(self.harmony)
        self.middle4_frame = tkinter.Frame(self.harmony)
        self.middle5_frame = tkinter.Frame(self.harmony)
        self.bottom_frame = tkinter.Frame(self.harmony)

        self.harmony_label = tkinter.Label(self.harmony, text=f'Scales associated with {mood_title}')

        self.harmony1_button = tkinter.Button(self.middle1_frame, text=example[0],
                                              command=lambda: self.play_wav(url[0]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony2_button = tkinter.Button(self.middle1_frame, text=example[1],
                                              command=lambda: self.play_wav(url[1]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony3_button = tkinter.Button(self.middle2_frame, text=example[2],
                                              command=lambda: self.play_wav(url[2]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony4_button = tkinter.Button(self.middle2_frame, text=example[3],
                                              command=lambda: self.play_wav(url[3]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony5_button = tkinter.Button(self.middle3_frame, text=example[4],
                                              command=lambda: self.play_wav(url[4]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony6_button = tkinter.Button(self.middle3_frame, text=example[5],
                                              command=lambda: self.play_wav(url[5]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony7_button = tkinter.Button(self.middle4_frame, text=example[6],
                                              command=lambda: self.play_wav(url[6]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony8_button = tkinter.Button(self.middle4_frame, text=example[7],
                                              command=lambda: self.play_wav(url[7]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony9_button = tkinter.Button(self.middle5_frame, text=example[8],
                                              command=lambda: self.play_wav(url[8]),
                                              bg='#E0E0E0', borderwidth=2)
        self.harmony10_button = tkinter.Button(self.middle5_frame, text=example[9],
                                               command=lambda: self.play_wav((url[9])),
                                               bg='#E0E0E0', borderwidth=2)

        self.harmony_label.pack()
        self.harmony1_button.pack(side='left')
        self.harmony2_button.pack(side='left')
        self.harmony3_button.pack(side='left')
        self.harmony4_button.pack(side='left')
        self.harmony5_button.pack(side='left')
        self.harmony6_button.pack(side='left')
        self.harmony7_button.pack(side='left')
        self.harmony8_button.pack(side='left')
        self.harmony9_button.pack(side='left')
        self.harmony10_button.pack(side='left')

        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.go_back)

        self.back_button.pack()

        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.middle3_frame.pack()
        self.middle4_frame.pack()
        self.middle5_frame.pack()
        self.bottom_frame.pack()

    @staticmethod
    def play_wav(wav):
        simpleaudio.stop_all()
        sound_object = simpleaudio.WaveObject.from_wave_file(wav)
        sound_object.play()

    def go_back(self):
        simpleaudio.stop_all()
        self.harmony.destroy()


class InstrumentInfoGUI:
    def __init__(self, master, mood, mood_title):
        example = []
        color = []

        try:
            music_cursor.execute("""SELECT * FROM Instruments WHERE LeadMood LIKE ?""",
                                 (mood,))
            instrument_list = music_cursor.fetchall()

            """Exactly the same as the last two examples, also adding instrument color for the association 
            between instrument families."""

            for line in instrument_list:
                name, family, transposition, lead, instrument_color = line
                information = f'{name}\n{family}\n{transposition}\n\n'
                example.append(information)
                color.append(instrument_color)

        except sqlite3.Error:
            print("SQLite Error occurred")

        self.instrument = tkinter.Toplevel(master)
        self.instrument.title("Instrument Information Expanded")
        self.instrument.geometry('1500x1250+750+0')

        self.top_frame = tkinter.Frame(self.instrument)
        self.middle1_frame = tkinter.Frame(self.instrument)
        self.middle2_frame = tkinter.Frame(self.instrument)
        self.middle3_frame = tkinter.Frame(self.instrument)
        self.middle4_frame = tkinter.Frame(self.instrument)
        self.middle5_frame = tkinter.Frame(self.instrument)
        self.bottom_frame = tkinter.Frame(self.instrument)

        self.instrument_label = tkinter.Label(self.top_frame, text=f'Solo/Lead Instruments associated with '
                                                                   f'{mood_title}')
        self.instrument_label.pack()

        """For this section, I'm using if statements to move through my list of moods and drop moods after they reach
        the maximum instruments associated with the mood. I.E. Supernatural Grandeur only has 2 lead instruments 
        so after the initial check, the mood stops at the second line because no further examples are needed. 
        I also pack the labels at each check so that I don't pack labels that don't exist."""

        if mood_title != "":
            self.instrument1_label = tkinter.Label(self.middle1_frame, text=example[0], fg=color[0])
            self.instrument2_label = tkinter.Label(self.middle1_frame, text=example[1], fg=color[1])

            self.instrument1_label.pack(side='left')
            self.instrument2_label.pack(side='left')

        elif mood_title != 'Supernatural Grandeur':

            self.instrument3_label = tkinter.Label(self.middle2_frame, text=example[2], fg=color[2])
            self.instrument4_label = tkinter.Label(self.middle2_frame, text=example[3], fg=color[3])
            self.instrument5_label = tkinter.Label(self.middle3_frame, text=example[4], fg=color[4])

            self.instrument3_label.pack(side='left')
            self.instrument4_label.pack(side='left')
            self.instrument5_label.pack(side='left')

        elif mood_title != 'Lyrical Grandeur' or mood_title != 'High Intensity Action':
            self.instrument6_label = tkinter.Label(self.middle3_frame, text=example[5], fg=color[5])

            self.instrument6_label.pack(side='left')

        elif mood_title != 'Moderate Intensity Action' or mood_title != 'Heroic' or mood_title != 'Action Adventure':
            self.instrument7_label = tkinter.Label(self.middle4_frame, text=example[6], fg=color[6])

            self.instrument7_label.pack(side='left')

        elif mood_title != 'Slow Drama':
            self.instrument8_label = tkinter.Label(self.middle4_frame, text=example[7], fg=color[7])

            self.instrument8_label.pack(side='left')

        elif mood_title != 'Villain':
            self.instrument9_label = tkinter.Label(self.middle5_frame, text=example[8], fg=color[8])

            self.instrument9_label.pack(side='left')

        elif mood_title != 'Love' or mood_title != 'Comedy':
            self.instrument10_label = tkinter.Label(self.middle4_frame, text=example[9], fg=color[9])
            self.instrument11_label = tkinter.Label(self.middle4_frame, text=example[10], fg=color[10])

            self.instrument10_label.pack(side='left')
            self.instrument11_label.pack(side='left')

        elif mood_title != 'Sad Ballad':
            self.instrument12_label = tkinter.Label(self.middle4_frame, text=example[11], fg=color[11])

            self.instrument12_label.pack(side='left')

        elif mood_title != 'Mystery/Suspense' or mood_title != 'Magical Fantasy':
            self.instrument13_label = tkinter.Label(self.middle5_frame, text=example[12], fg=color[12])
            self.instrument14_label = tkinter.Label(self.middle5_frame, text=example[13], fg=color[13])
            self.instrument15_label = tkinter.Label(self.middle5_frame, text=example[14], fg=color[14])

            self.instrument13_label.pack(side='left', padx=10)
            self.instrument14_label.pack(side='left', padx=10)
            self.instrument15_label.pack(side='left', padx=10)

        self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.go_back)

        self.back_button.pack()

        self.top_frame.pack()
        self.middle1_frame.pack()
        self.middle2_frame.pack()
        self.middle3_frame.pack()
        self.middle4_frame.pack()
        self.middle5_frame.pack()
        self.bottom_frame.pack()

    def go_back(self):
        self.instrument.destroy()


class ElementInfoGUI:
    def __init__(self, master, mood, mood_title):
        comp_elements_string = ""

        """For the compositional elements I parsed out the Mystery/Suspense specifically because there were
        so many element examples that I needed to be able to format them clearly. 
        In the future I may copy the instrument if statement example to cleanly do all of them, but I think
        it works well for now. """

        if mood_title == 'Mystery/Suspense':
            example = []
            try:
                music_cursor.execute("""SELECT * FROM CompositionalElements WHERE Mood LIKE ?""",
                                     (mood,))
                compositional_element_list = music_cursor.fetchall()

                for item in compositional_element_list:
                    element, element_type, element_effect, element_mood = item
                    information = f'Element: {element}\nType: {element_type}\nEffect: {element_effect}\n\n'
                    example.append(information)

                self.elements = tkinter.Toplevel(master)
                self.elements.title("Compositional Element Information Expanded")
                self.elements.geometry('1500x1350+750+0')

                self.top_frame = tkinter.Frame(self.elements)
                self.middle_frame = tkinter.Frame(self.elements)
                self.middle2_frame = tkinter.Frame(self.elements)
                self.middle3_frame = tkinter.Frame(self.elements)
                self.middle4_frame = tkinter.Frame(self.elements)
                self.middle5_frame = tkinter.Frame(self.elements)
                self.middle6_frame = tkinter.Frame(self.elements)
                self.bottom_frame = tkinter.Frame(self.elements)

                self.elements_title = tkinter.Label(self.top_frame,
                                                    text=f"Important Compositional Elements for {mood_title}\n\n")
                self.elements_label = tkinter.Label(self.middle_frame, text=example[0])
                self.example1_label = tkinter.Label(self.middle_frame, text=example[1])
                self.example2_label = tkinter.Label(self.middle_frame, text=example[2])
                self.example3_label = tkinter.Label(self.middle2_frame, text=example[3])
                self.example4_label = tkinter.Label(self.middle2_frame, text=example[4])
                self.example5_label = tkinter.Label(self.middle3_frame, text=example[5])
                self.example6_label = tkinter.Label(self.middle3_frame, text=example[6])
                self.example7_label = tkinter.Label(self.middle4_frame, text=example[7])
                self.example8_label = tkinter.Label(self.middle4_frame, text=example[8])
                self.example9_label = tkinter.Label(self.middle5_frame, text=example[9])

                self.elements_title.pack(side='left', padx=10, pady=10)
                self.example1_label.pack(side='left', padx=10, pady=10)
                self.example2_label.pack(side='right', padx=10, pady=10)
                self.example3_label.pack(side='left', padx=10, pady=10)
                self.example4_label.pack(side='left', padx=10, pady=10)
                self.example5_label.pack(side='left', padx=10, pady=10)
                self.example6_label.pack(side='left', padx=10, pady=10)
                self.example7_label.pack(side='left', padx=10, pady=10)
                self.example8_label.pack(side='left', padx=10, pady=10)
                self.example9_label.pack(side='left', padx=10, pady=10)
                self.elements_label.pack(side='left', padx=10, pady=10)

                self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.go_back)

                self.back_button.pack()

                self.top_frame.pack()
                self.middle_frame.pack()
                self.middle2_frame.pack()
                self.middle3_frame.pack()
                self.middle4_frame.pack()
                self.middle5_frame.pack()
                self.middle6_frame.pack()
                self.bottom_frame.pack()

            except sqlite3.Error:
                print("SQLite Error occurred")
        else:

            try:
                music_cursor.execute("""SELECT * FROM CompositionalElements WHERE Mood LIKE ?""",
                                     (mood,))
                compositional_element_list = music_cursor.fetchall()

                for item in compositional_element_list:
                    temp = "Element: " + item[0] + "\nType: " + item[1] + "\nEffect: " + item[2] + " " + "\n\n"
                    comp_elements_string += temp

                self.elements = tkinter.Toplevel(master)
                self.elements.title("Compositional Element Information Expanded")
                self.elements.geometry('1500x1250+750+0')

                self.top_frame = tkinter.Frame(self.elements)
                self.bottom_frame = tkinter.Frame(self.elements)

                self.elements_title = tkinter.Label(self.top_frame,
                                                    text=f"Important Compositional Elements for {mood_title}\n")
                self.elements_label = tkinter.Label(self.top_frame, text=comp_elements_string)

                self.elements_title.pack()
                self.elements_label.pack()

                self.back_button = tkinter.Button(self.bottom_frame, text='Back', command=self.go_back)

                self.back_button.pack()

                self.top_frame.pack()
                self.bottom_frame.pack()

            except sqlite3.Error:
                print("SQLite Error occurred")

    def go_back(self):
        self.elements.destroy()


def main():
    root = tkinter.Tk()
    _ = ComposerGUI(root)
    root.mainloop()


main()