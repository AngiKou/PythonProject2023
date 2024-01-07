import tkinter as tk  # Εισαγωγή του tkinter ως tk για τη δημιουργία γραφικού περιβάλλοντος
from tkinter import ttk  # Εισαγωγή του ttk από το tkinter για χρήση βελτιωμένων widgets
from tkinter import *  # Εισαγωγή όλων των στοιχείων από το tkinter για ευκολότερη πρόσβαση

class App:  # Ορισμός της κλάσης App
    def __init__(self, root):  # Ορισμός του κατασκευαστή της κλάσης
        super().__init__()  # Κληρονομεί από την υπερκλάση
        self.w = root  # Ορισμός του παραθύρου ως ριζικού παραθύρου
        self.w.resizable(0, 0)  # Καθορισμός της αδυναμίας αλλαγής μεγέθους του παραθύρου
        self.w.geometry("763x840")  # Καθορισμός του μεγέθους του παραθύρου
        self.w.title("Mind at Ease")  # Καθορισμός του τίτλου του παραθύρου
        self.w.configure(bg="#e1c9f8")  # Καθορισμός του χρώματος του παραθύρου

        self.entries = []  # Αρχικοποίηση λίστας για τα entry widgets
        self.entrysave = []  # Αρχικοποίηση λίστας για την αποθήκευση των τιμών των entry widgets
        self.variables = []  # Αρχικοποίηση λίστας για τις StringVars
        self.textvar = ""  # Αρχικοποίηση μεταβλητής για την αποθήκευση του κειμένου από το Text widget
        self.listatoutext = []  # Αρχικοποίηση λίστας για το Text widget
        self.frame1 = Frame1(self.w, self)  # Δημιουργία του πρώτου πλαισίου
        self.frame1.grid(row=0, column=0, columnspan=3, sticky="news")  # Τοποθέτηση του πρώτου πλαισίου στο παράθυρο
        self.frame2 = Frame2(self.w, self)  # Δημιουργία του δεύτερου πλαισίου
        self.frame2.grid(row=1, column=0, rowspan=2, columnspan=3, sticky="news")  # Τοποθέτηση του δεύτερου πλαισίου στο παράθυρο
        self.frame3 = Frame3(self.w, self)  # Δημιουργία του τρίτου πλαισίου
        self.frame3.grid(row=3, column=0, columnspan=3, sticky="news")  # Τοποθέτηση του τρίτου πλαισίου στο παράθυρο

    def savee(self):  # Συνάρτηση για την αποθήκευση των τιμών από τα entry και το Text widget
        for i in self.entries:
            self.entrysave.append(i.get())  # Αποθηκεύει τις τιμές που έχουν εισαχθεί στα entry widgets
        self.textvar = self.listatoutext[0].get(1.0, "end")  # Αποθηκεύει το κείμενο που έχει εισαχθεί στο Text widget

class Frame1(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#e1c9f8")
        self.label1 = ttk.Label(
            self,
            text="[datepicked]-Fill in the blanks with emotions you felt today:",
            font=("Helvetica", 10),
            bootstyle="primary-inverse",
        )
        self.label1.grid(row=0, column=1, columnspan=3, sticky="news", padx=125)  # Εμφανίζει μια ετικέτα με κείμενο
        self.app = app
        self.entries = []
        self.entrysave = []
        self.variables = []
        self.emotionlist = []

        for i in range(5):
            text = tk.StringVar(value="")
            self.app.variables.append(text)
            self.entry = ttk.Entry(
                self,
                width=30,
                font=("Helvetica", 10),
                bootstyle="danger",
                textvariable=text,
            )
            self.entry.grid(row=i + 1, column=1, sticky="news", padx=10, pady=10)
            self.entry.bind("<Key>", self.char_limit)  # Συνδέει τη συνάρτηση char_limit με τα entry widgets
            self.app.entries.append(self.entry)

        for i in range(5):
            text = tk.StringVar(value="")
            self.app.variables.append(text)
            self.entry = ttk.Entry(
                self,
                width=30,
                font=("Helvetica", 10),
                bootstyle="danger",
                textvariable=text,
            )
            self.entry.grid(row=i + 1, column=3, sticky="news", padx=10, pady=10)
            self.entry.bind("<Key>", self.char_limit)  # Συνδέει τη συνάρτηση char_limit με τα entry widgets
            self.app.entries.append(self.entry)

    def char_limit(self, event):
        entry_widget = event.widget
        input_str = entry_widget.get()
        if len(input_str) > 13:  # Ελέγχει το μήκος του κειμένου εισόδου σε κάθε entry widget
            entry_widget.delete(0, "end")  # Διαγράφει το περιεχόμενο του entry widget
            entry_widget.insert(0, input_str[:15])  # Εισάγει τα πρώτα 15 χαρακτήρες του περιεχομένου

class Frame2(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(
            parent, bg="#e1c9f8"
        )  # Δημιουργεί το δεύτερο πλαίσιο με τον γονικό (parent) widget και ρυθμίζει το χρώμα του background
        self.label2 = ttk.Label(
            self,
            text="Elaborate further on these feelings !",
            font=("Helvetica", 10),
            bootstyle="primary-inverse",
        )  # Δημιουργεί μια ετικέτα (label) με συγκεκριμένο κείμενο
        self.label2.grid(
            row=0, column=0, columnspan=3, sticky="news", pady=2, padx=250
        )  # Τοποθετεί την ετικέτα στο πλαίσιο
        self.app = app
        defaultvalue = ""

        # Η παρακάτω συνθήκη φαίνεται να είναι σχολιασμένη, είναι ένα block που πιθανόν να μην χρησιμοποιείται
        """
        if i < len(self.emotionlist):
            defaultvalue = self.emotionlist[i]
            variabletoutext = tk.StringVar(value=defaultvalue)
        """
            
        self.text = ttk.Text(
            self, font=("Helvetica", 10), width=80, height=23,
        )  # Δημιουργεί ένα κείμενο widget, όπου ο χρήστης μπορεί να εισάγει κείμενο
        self.text.grid(
            row=1, column=0, sticky="news", rowspan=1, columnspan=3, padx=10
        )  # Τοποθετεί το κείμενο widget στο πλαίσιο
        self.listatoutext = []
        self.app.listatoutext.append(self.text)  # Προσθέτει το κείμενο widget σε μια λίστα
        self.clear_all_button = ttk.Button(
            self,
            text="Clear Text",
            bootstyle="warning-link",
            width=85,
            command=self.clear_all,
        )  # Δημιουργεί ένα κουμπί με κείμενο "Clear Text" και τονίζει το χρώμα του κειμένου
        self.clear_all_button.grid(row=2, column=0, columnspan=1, sticky="se")  # Τοποθετεί το κουμπί στο πλαίσιο

    def clear_all(self):
        self.text.delete(1.0, "end")  # Διαγράφει όλο το κείμενο από το widget

class Frame3(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(
            parent, bg="#e1c9f8"
        )  # Δημιουργεί το τρίτο πλαίσιο με τον γονικό (parent) widget και ρυθμίζει το χρώμα του background
        self.button1 = ttk.Button(
            self,
            text="Save & Quit",
            bootstyle="primary",
            command=self.save_and_quit_window,
        )  # Δημιουργεί ένα κουμπί με το κείμενο "Save & Quit", εφαρμόζοντας ένα στιλ για την εμφάνιση του
        self.button1.grid(
            row=1, column=3, sticky="news", padx=555, pady=3
        )  # Τοποθετεί το κουμπί στο πλαίσιο
        self.app = app
        self.button2 = ttk.Button(
            self, text="Exit", bootstyle="primary", command=self.exit_window
        )  # Δημιουργεί ένα κουμπί με το κείμενο "Exit", εφαρμόζοντας ένα στιλ για την εμφάνιση του, και ορίζει τη συνάρτηση που θα κληθεί όταν πατηθεί
        self.button2.grid(
            row=1, column=1, sticky="news", padx=15, pady=3
        )  # Τοποθετεί το κουμπί στο πλαίσιο

    def exit_window(self):
        self.master.destroy()  # Καλείται όταν πατηθεί το κουμπί "Exit" και κλείνει το παράθυρο

    def save_and_quit_window(self):
        self.app.savee()  # Καλεί τη συνάρτηση savee της κλάσης App για αποθήκευση των δεδομένων
        creating_files.create_folder_files()  # Καλεί τη συνάρτηση για δημιουργία φακέλου και αρχείων
        creating_files.save_file(datepicked, self.app.entrysave, self.app.textvar)  # Καλεί τη συνάρτηση για αποθήκευση των δεδομένων σε αρχείο
        self.master.destroy()  # Κλείνει το παράθυρο

root = ttk.Toplevel()  # Δημιουργία ενός καινούριου Toplevel παραθύρου
app_giannis = App(root)  # Δημιουργία αντικειμένου της κλάσης App