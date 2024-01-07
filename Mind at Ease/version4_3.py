import tkinter as tk
import ttkbootstrap as ttk
import creating_files

from PIL import Image

Image.CUBIC = Image.BICUBIC


def appopen():
    root = ttk.Toplevel()
    root.geometry("650x600")
    root.title("Mind at Ease")
    root.columnconfigure((0, 1, 2, 3, 4), weight=1)
    root.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    root.resizable(False, False)

    def getdate():
        global datepicked
        # grab date.This is the variable that should be used to open the current date window
        datepicked = dateentry.entry.get()
        strvar.set(value=f"Selected-Date is {datepicked}")
        giannisapp()

    def newwindow():
        # the function that takes place when you press the button with the title:enter as doctor
        def getpassword():
            # getting the password from the entrybox and putting it in the variable password
            password = passwordentry.get()
            # setting the current password
            realpassword = "1234"
            if realpassword == password:
                # if the password is correct a new window is created and the last one is destroyed
                app2 = ttk.Toplevel()
                app2.geometry("650x350")
                app2.title("Doctors setting's")
                win.destroy()
                lbl = ttk.Label(
                    app2,
                    bootstyle="secondary",
                    text="               Change the doctors notes then press save\n(please press enter before hitting the border of the text box)",
                )
                lbl.pack(padx=10, pady=10)
                # text widget
                textfordoc = ttk.Text(app2, height=5, width=39, takefocus=True)
                textfordoc.pack(padx=10, pady=10)

                # the function that changes the current doctor notes to new ones when you press the button save
                def save():
                    docnotes = textfordoc.get("1.0", "end")
                    notevar.set(docnotes)

                btn = ttk.Button(app2, bootstyle="primary", text="Save", command=save)
                btn.pack(ipadx=40, ipady=10)
            # if the password is incorrect then it will create a label that says wrong password
            else:
                labelerror = ttk.Label(
                    win, text="Wrong Password! Try again", bootstyle="secondary-inverse"
                )
                labelerror.grid(
                    row=1, column=1, rowspan=3, sticky="n", pady=10, padx=(0, 15)
                )
                passwordentry.delete(0, "end")

        """Create a new window"""
        win = tk.Toplevel(root)
        win.geometry("400x120")
        win.title("Password entry")
        win.rowconfigure((0, 1, 2, 3), weight=1)
        win.columnconfigure((0, 1, 2, 3), weight=1)
        passwordentry = ttk.Entry(win, show="*", bootstyle="warning", takefocus=True)
        passwordentry.grid(row=0, column=1, padx=(10, 30), sticky="we")
        password = ttk.Label(
            win,
            bootstyle="secondary",
            text="Password:",
        )
        password.grid(row=0, column=0, padx=(10, 0), sticky="e")
        # the button that opens the sumbits the password
        buttonpassword = ttk.Button(
            win, text="Sumbit", bootstyle="secondary-outline", command=getpassword
        )
        buttonpassword.grid(row=0, column=2, sticky="w", padx=0)

        # # # the commands needed to place the currnet background image
        folder = Path(__file__).parent
        image_path = Path(folder, "fonto_journal.jpg")
        bg = tk.PhotoImage(file=image_path)

    # bg = tk.PhotoImage(
    #     file="C:\\Users\\gpoli\\Desktop\\PythonProject2023-main2\\PythonProject2023-main\\pastel.png"
    # )
    # backgroundphoto = ttk.Label(root, image=bg)
    # backgroundphoto.place(x=0, y=0, relwidth=1, relheight=1)

    # label next to the date entry
    titlelabel = ttk.Label(root, text="select a date:", bootstyle="primary-inverse")
    titlelabel.grid(row=0, column=1, sticky="e", padx=10, pady=15)
    # dateentry widget
    dateentry = ttk.DateEntry(root, dateformat="%d/%m/%Y")
    dateentry.grid(row=0, column=2, sticky="we", pady=10)

    # random default value

    # count = 10
    count = creating_files.count_files_with_later_dates()
    # count should be a variable that is used as(count=+1) so that everytime
    # the button is clicked it adds +1 to count and displays on the meter the current datestreak

    datestreak = count
    # print(creating_files.count_files_with_later_dates())
    # datestreak = creating_files.count_files_with_later_dates()
    # the line in between statistics and date selection. Makes the app look better
    separationline = ttk.Separator(root, bootstyle="primary")
    separationline.grid(row=1, columnspan=4, stick="ew", padx=30, pady=(35, 10))
    # the label frame which will contain the meter and the doctor notes
    labelframe = ttk.LabelFrame(
        root, bootstyle="primary", relief="ridge", text="Statistics-Notes"
    )
    labelframe.grid(row=2, column=0, columnspan=4, rowspan=4, sticky="wen", padx=25)
    # the meter that will show the current day streak
    meterstats = ttk.Meter(
        labelframe,
        bootstyle="primary",
        arcrange=180,
        arcoffset=180,
        amounttotal=30,
        amountused=datestreak,
        meterthickness=10,
        metersize=160,
        interactive=False,
        subtext="Streak",
        metertype="semi",
        textright="Days",
        stepsize=1,
        stripethickness=6,
    )
    meterstats.grid(row=0, column=0, columnspan=2, pady=25, padx=(20, 0))
    # basicaly the title that says Doctor's notes. it works like a frame widget which will contain the notefordoctor Label
    doctorsnoteframe = ttk.LabelFrame(
        labelframe,
        text="Doctor's Notes:",
        width=150,
        height=100,
        relief="flat",
        bootstyle="secondary",
    )
    doctorsnoteframe.grid(
        row=0, column=2, rowspan=3, columnspan=3, padx=50, sticky="ne"
    )
    # the line between the title that says doctors notes and the actual doctors notes
    underlining = ttk.Separator(doctorsnoteframe, bootstyle="primary")
    underlining.grid(row=0, column=0, sticky="wne", padx=(0, 175))
    # this notevar variable should be able to change by the doctor from doctor settings
    notevar = tk.StringVar(
        value="Dont forget to always tell good things\n to yourself when you look at the mirror,\nand to always acknowledge the importance\n of the effort you put in your work"
    )
    notefordoctor = ttk.Label(
        doctorsnoteframe, bootstyle="secondary", textvariable=notevar
    )
    notefordoctor.grid(row=1, column=0, pady=7, sticky="w")

    # button that confirms the selected date
    confirmbutton = ttk.Button(
        root,
        text="Press to confirm",
        bootstyle="primary-outline",
        command=getdate,
    )
    confirmbutton.grid(row=0, column=3, sticky="w", padx=10)
    # optional label that changes to the corresponding date that has been selected by the user
    strvar = tk.StringVar(value="Waiting for a date to be selected")
    mylabel = ttk.Label(root, bootstyle="primary-inverse", textvariable=strvar)
    mylabel.grid(row=1, column=2, sticky="n")

    docsbutton = ttk.Button(
        root, text="Enter as Doctor", command=newwindow, bootstyle="primary-outlined"
    )
    docsbutton.grid(row=5, column=2)

    # root.mainloop()
    # function that gets called when the event of closing the window of the main app happens
    def on_closing():
        """On closing window"""
        root_welcomepage.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)


"""GIANNIS"""


def giannisapp():
    global app_giannis

    class App:
        def __init__(self, root):
            super().__init__()
            self.w = root
            self.w.resizable(0, 0)
            self.w.geometry("715x742")  # Θέτω το μέγεθος του παραθύρου σε 800x775
            self.w.title("Mind at Ease")  # Ορίζω τον τίτλο του παραθύρου
            self.w.configure(bg="#e1c9f8")  # Ορίζω το χρώμα του παραθύρου

            self.entries = (
                []
            )  # Δημιουργώ μια νέα λίστα που θα περιέχει όλα τα entry πεδία που θα δημιουργηθούν στην ενέργεια του κώδικα
            self.entrysave = (
                []
            )  # list that contains the value of each entrybox when you press the button save
            self.variables = []  # list that contains stringvars
            self.textvar = ""  # variable that contains the value of the text widget
            self.listatoutext = []
            self.frame1 = Frame1(self.w, self)
            self.frame1.grid(
                row=0, column=0, columnspan=3, sticky="news"
            )  # Τοποθετώ το πρώτο πλαίσιο στο παράθυρο
            self.frame2 = Frame2(self.w, self)
            self.frame2.grid(
                row=1, column=0, rowspan=2, columnspan=3, sticky="news"
            )  # Τοποθετώ το δεύτερο πλαίσιο στο παράθυρο
            self.frame3 = Frame3(self.w, self)
            self.frame3.grid(
                row=3, column=0, columnspan=3, sticky="news"
            )  # Τοποθετώ το τρίτο πλαίσιο στο παράθυρο

        def savee(self):
            for i in self.entries:
                self.entrysave.append(i.get())
            self.textvar = self.listatoutext[0].get(0.1, "end")

    class Frame1(tk.Frame):
        def __init__(self, parent, app):
            super().__init__(
                parent, bg="#e1c9f8"
            )  # Φτιάχνει το πρώτο πλαίσιο με parent widget
            self.label1 = ttk.Label(
                self,
                text=f"[{datepicked}]-Fill in the blanks with emotions you felt today:",
                font=("Helvetica", 10),
                bootstyle="primary-inverse",
            )  # Φτιάχνει μια ταμπέλα με ένα καθορισμένο κείμενο
            self.label1.grid(
                row=0, column=1, columnspan=3, sticky="news", padx=125
            )  # Τοποθετώ την ταμπέλα
            self.app = app
            self.entries = (
                []
            )  # Δημιουργώ μια νέα λίστα που θα περιέχει όλα τα entry πεδία που θα δημιουργηθούν στην ενέργεια του κώδικα
            self.entrysave = []  # lista poy periexei ta periexomena ton entries
            self.variables = []
            self.emotionlist = []
            filename = "_".join(datepicked.split("/")) + ".txt"
            # print(filename)
            self.file_info_dictionary = creating_files.read_from_files(filename)
            if self.file_info_dictionary is not None :
                self.emotionlist = self.file_info_dictionary["emotion_list"]

            for i in range(5):
                # Τοποθετώ μέσα σε μια σειρά τα παρακάτω widget για να αποφύγω την επανάληψη τους
                self.lbl = ttk.Label(
                    self, text="•"
                )  # Δημιουργώ μια ταμπέλα με "•" σαν κείμενο
                self.lbl.grid(
                    row=i + 1, column=0, sticky="w", padx=20
                )  # Τοποθετώ την ταμπέλα
                defaultvalue = ""
                if i < len(self.emotionlist):
                    defaultvalue = self.emotionlist[i]

                text = tk.StringVar(value=defaultvalue)

                self.app.variables.append(text)
                self.entry = ttk.Entry(
                    self,
                    width=30,
                    font=("Helvetica", 10),
                    bootstyle="danger",
                    textvariable=text,
                )
                self.entry.grid(row=i + 1, column=1, sticky="news", padx=10, pady=10)
                self.entry.bind("<Key>", self.char_limit)
                self.app.entries.append(self.entry)

            # Κάνω ακριβώς το ίδιο και για τη δεύτερη στήλη
            for i in range(5):
                defaultvalue = ""
                if (i + 5) < len(self.emotionlist):
                    defaultvalue = self.emotionlist[i + 5]
                text = tk.StringVar(value=defaultvalue)
                self.lbl = ttk.Label(self, text="•")
                self.lbl.grid(row=i + 1, column=2, sticky="w", padx=20)

                self.app.variables.append(text)
                self.entry = ttk.Entry(
                    self,
                    width=30,
                    font=("Helvetica", 10),
                    bootstyle="danger",
                    textvariable=text,
                )
                self.entry.grid(row=i + 1, column=3, sticky="news", padx=10, pady=10)
                self.entry.bind(
                    "<Key>", self.char_limit
                )  # Μια ενέργεια που γίνεται κάθε φορά που πατά ο χρήστης μια πλήκτρο στο entry πεδίο. Αυτή η ενέργεια καλεί την συνάρτηση self.char_limit κάθε φορά που πατά ο χρήστης ένα πλήκτρο
                self.app.entries.append(
                    self.entry
                )  # μια ενέργεια που προσθέτει το entry πεδίο στη λίστα self.entries. Αυτό το γίνεται για να διατηρηθεί η λίστα με όλα τα entry πεδία που δημιουργήθηκαν

        def char_limit(
            self, event
        ):  # Η συνάρτηση που βάζει όριο στους χαρακτήρες που μπορούν να πληκτρολογηθούν στα entry box.
            entry_widget = (
                event.widget
            )  # Προσδιορίζει ποιό entry box έχει ενεργοποιηθεί και το εκχωρεί στην μεταβλητή entry_widget
            input_str = (
                entry_widget.get()
            )  # Θέτω ως input_str 'ο,τι έχει γράψει ο χρήστης στα entry box
            if (
                len(input_str) > 13
            ):  # Ελέγχει εάν το μήκος του string είναι μεγαλύτερο των 15 χαρακτήρων
                entry_widget.delete(
                    0, "end"
                )  # Διαγράφει όλο το περιεχόμενο του entry πεδίου από την θέση 0 μέχρι το τέλος.
                entry_widget.insert(
                    0, input_str[:15]
                )  # Καλείται μετά τη διαγραφή του περιεχόμενου του entry πεδίου για να εισάγει το νέο περιεχόμενο.

    class Frame2(tk.Frame):
        def __init__(self, parent, app):
            super().__init__(
                parent, bg="#e1c9f8"
            )  # Φτιάχνει το δεύτερο πλαίσιο με parent widget
            self.label2 = ttk.Label(
                self,
                text="Elaborate further on these feelings !",
                font=("Helvetica", 10),
                bootstyle="primary-inverse",
            )  # Φτιάχνει μια ταμπέλα με ένα καθορισμένο κείμενο
            self.label2.grid(
                row=0, column=0, columnspan=3, sticky="news", pady=2, padx=250
            )  # Τοποθετώ την ταμπέλα
            self.app = app
            defaultvalue = "    "

            if (
                self.app.frame1.file_info_dictionary
                and self.app.frame1.file_info_dictionary["emotion_text"]
            ):
                defaultvalue = self.app.frame1.file_info_dictionary["emotion_text"]
            # variabletoutext = tk.StringVar(value=defaultvalue)

            self.text = ttk.Text(
                self,
                font=("Helvetica", 10),
                width=80,
                height=23,
            )  # textvariable=variabletoutext
            # Δημιουργώ ένα text widget, στο οποίο ο χρήστης μπορεί να πληκρολογήσει ελεύθερα τις σκέψεις του
            # self.text.setvar(defaultvalue)
            # give a defualt text to display on the self.text
            self.text.insert(1.0, defaultvalue)

            self.text.grid(
                row=1, column=0, sticky="news", rowspan=1, columnspan=3, padx=10
            )  # Τοποθετώ το widget
            self.listatoutext = []
            self.app.listatoutext.append(self.text)
            self.clear_all_button = ttk.Button(
                self,
                text="Clear Text",
                bootstyle="warning-link",
                width=85,
                command=self.clear_all,
            )
            self.clear_all_button.grid(row=2, column=0, columnspan=1, sticky="se")

        def clear_all(self):
            self.text.delete(1.0, "end")

    class Frame3(tk.Frame):
        def __init__(self, parent, app):
            super().__init__(
                parent, bg="#e1c9f8"
            )  # Φτιάχνει το τρίτο πλαίσιο με parent widget
            self.button1 = ttk.Button(
                self,
                text="Save & Quit",
                bootstyle="primary",
                command=self.save_and_quit_window,
            )  # Δημιουργώ ενα κουμπί "Save", το οποίο όταν πατηθεί αποθηκεύει ό,τι έχει γράψει ο χρήστης
            self.button1.grid(
                row=1, column=3, sticky="news", padx=555, pady=3
            )  # Τοποθετώ το κουμπί στο πλαίσιο
            self.app = app
            self.button2 = ttk.Button(
                self, text="Exit", bootstyle="primary", command=self.exit_window
            )  # Δημιουργώ ένα κουμπί "Exit", το οποίο όταν πατηθεί κλείνει το παράθυρο
            self.button2.grid(
                row=1, column=1, sticky="news", padx=15, pady=3
            )  # Τοποθετώ το κουμπί στο πλαίσιο

        def exit_window(self):
            self.master.destroy()  # Δημιουργώ την συνάρτηση για το κουμπί "Exit" , η οποία κλείνει το παράθυρο

        def save_and_quit_window(self):
            self.app.savee()  # Δημιουργώ την συνάρτηση για το κουμπί "Save & Quit", η οποία αποθηκεύει τα στοιχεία του παραθύρου και το κλείνει
            creating_files.create_folder_files()
            creating_files.save_file(
                datepicked, self.app.entrysave, self.app.textvar
            )  # checkpoint
            self.master.destroy()

    # Δημιουργώ το παράθυρο, και βάζω ένα συγκεκριμένο theme
    root = ttk.Toplevel()
    app_giannis = App(root)
    # Θέτω ως παράμετρο της κλάσης App το ίδιο το παράθυρο, ώστε η κλάση αυτή να είναι υπεύθυνη για το περιεχόμενο και τη λειτουργικότητα του παραθύρου
    # root.mainloop() # Με αυτή τη μέθοδο ξεκινάει ο βρόχος επεξεργασίας γεγονότων


# app_giannis.entrysave
# app_giannis.textvar


"""HEKLIS"""
import random
from pathlib import Path


class WelcomePage:
    def __init__(self, root_welcomepage):
        self.w = root_welcomepage
        self.w.title("Mind at Ease")
        self.w.geometry("1500x900")
        self.w.resizable(
            0, 0
        )  # Δεν επιτρεπει στον χρηστη να μπορει να κανει μεγενθυση ή σμικρυνση στο παραθυρο
        # self.bg = tk.PhotoImage(file='""C:\\background.png""')#Τοποθετηση εικονας για bg
        folder = Path(__file__).parent
        image_path = Path(folder, "bg.png")
        self.bg = tk.PhotoImage(file=image_path)
        # Λιστα με τυχαια quotes
        self.randomquotes = [
            '"Love yourself first and everything else falls into line."\n-Lucille Ball',
            '"The most common way people give up their power\nis by thinking they do not have any."\n-Alice Walker',
            '"Stand before the people you fear and speak\nyour mind even if your voice shakes."\n-Maggie Kuhn',
            '"You cannot turn back the clock. But you can wind it up again."\n-Bonnie Prudden',
            '"A problem is a chance for you to do your best."\n-Duke Ellington',
            '"Give light and people will find the way."\n-Ella Baker',
            '"It always seems impossible until it is done."\n-Nelson Mandela',
            '"Failure is the condiment that gives success its flavor."\n-Truman Capote',
            ' "Keep your face always toward the sunshine,\nand shadows will fall behind you."\n-Walt Whitman',
        ]
        # Χρηση της συναρτησης random.choice ωστε η μεταβλητη self.quote να παιρνει τυχαια την τιμη ενος quote σε μορφη string
        self.quote = random.choice(self.randomquotes)

        self.canvas = tk.Canvas(
            self.w, width=1500, height=900
        )  # Δημιουργια κανβα για τοποθετηση των κουμπιων, τoυ random quote και του bg
        self.canvas.pack(
            fill="both", expand=1
        )  # Τοποθετηση του κανβα μεσα στο παραθυρο αφου εχει οριστει το μεγεθος του παραπανω και με συνθηκες μεσα στο .pack() ωστε να καταλαμβανει ολοκληρο τον χωρο
        self.canvas.create_image(
            0, 0, image=self.bg, anchor="nw"
        )  # Δημιουργια της εικονας που βρισκετε στο bg με συνθηκες ωστε να πιανει ολοκληρο τον χωρο του κανβα

        # Δημιουργια κειμενου με text το τυχαιο quote και συνθηκες ωστε να βγαινει στην μεση της σελιδας και απο πανω 'Quote of the day:'
        self.canvas.create_text(
            750,
            390,
            text="Quote of the day:",
            font=("Open Sans", 30, "bold"),
            fill="black",
        )
        self.canvas.create_text(
            750, 520, text=self.quote, font=("Open Sans", 25, "bold"), fill="black"
        )  # Δημιουργια κειμενου με text το τυχαιο quote και συνθηκες ωστε να βγαινει στην μεση της σελιδας

        # Δημιουργια των κουμπιων 'Exit' 'Show Statistics' και 'Entry'
        self.b1 = ttk.Button(
            self.w,
            bootstyle="dark-link",
            text="Exit",
            command=self.b1_pushed,
        )

        self.b3 = ttk.Button(
            self.w, bootstyle="dark-link", text="Entry", command=self.b3_pushed
        )

        # Τοποθετηση των κουμπιων στον κανβα
        self.b1_canvas = self.canvas.create_window(15, 800, anchor="nw", window=self.b1)

        self.b3_canvas = self.canvas.create_window(
            1400, 800, anchor="nw", window=self.b3
        )

    def b1_pushed(self):
        self.w.destroy()  # με το πατημα του κουμπιου 'exit' το παραθυρο κλεινει

    def b2_pushed(self):
        self.w.destroy()
        # εδω θα ανοιγει το παραθυρο των στατιστικων(συμπληρωση κατα την συνοχη των κωδικων)

    def b3_pushed(self):
        appopen()
        # επειδη το προγραμμα δεν δουλευει οταν καταστρεφεται το προηγουμενο παραθυρο με το wm_state("iconic")
        # γινεται minimize το παραθυρο
        self.w.wm_state("iconic")
        # εδω θα ανοιγει το παραθυρο του πολιτη (συμπληρωση κατα την συνοχη των κωδικων)


root_welcomepage = ttk.Window(themename="purpletheme")
#root_welcomepage = ttk.Window(themename="litera")
WelcomePage(root_welcomepage)
root_welcomepage.mainloop()#
