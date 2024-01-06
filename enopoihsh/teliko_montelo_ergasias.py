from tkinter import *  # Εισάγω τις απαραίτητες βιβλιοθήκες για την υλοποίηση του κώδικα
import ttkbootstrap as ttk


class JournalApp:
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.state = "exit"

    def main(self):
        if self.root is None:
            self.root = ttk.Window(
                # themename="purpletheme"
                # --------- CHANGED FOR LINUX ---------
                themename="litera"
                # --------------------------------------
            )
            # Δημιουργώ το παράθυρο, και βάζω ένα συγκεκριμένο theme
        # self.root = Toplevel(self.root)
        self.root.geometry("763x840")  # Θέτω το μέγεθος του παραθύρου σε 800x775
        self.root.title("Emotion Journal")  # Ορίζω τον τίτλο του παραθύρου
        self.root.configure(bg="#e1c9f8")  # Ορίζω το χρώμα του παραθύρου

        self.frame1 = Frame1(self.root, self)
        self.frame1.grid(
            row=0, column=0, columnspan=3, sticky=W + E + N + S
        )  # Τοποθετώ το πρώτο πλαίσιο στο παράθυρο
        self.frame2 = Frame2(self.root, self)
        self.frame2.grid(
            row=1, column=0, rowspan=2, columnspan=3, sticky=W + E + N + S
        )  # Τοποθετώ το δεύτερο πλαίσιο στο παράθυρο
        self.frame3 = Frame3(self.root, self)
        self.frame3.grid(
            row=3, column=0, columnspan=3, sticky=W + E + N + S
        )  # Τοποθετώ το τρίτο πλαίσιο στο παράθυρο


class Frame1(Frame):
    def __init__(self, parent, app):
        super().__init__(
            parent, bg="#e1c9f8"
        )  # Φτιάχνει το πρώτο πλαίσιο με parent widget
        self.label1 = ttk.Label(
            self,
            text="Fill in the blanks with the prevailing emotions of the day :",
            font=("Helvetica", 10),
            bootstyle="primary-inverse",
        )  # Φτιάχνει μια ταμπέλα με ένα καθορισμένο κείμενο
        self.label1.grid(
            row=0, column=1, columnspan=3, sticky=W + E + N + S, padx=125
        )  # Τοποθετώ την ταμπέλα

        self.entries = (
            []
        )  # Δημιουργώ μια νέα λίστα που θα περιέχει όλα τα entry πεδία που θα δημιουργηθούν στην ενέργεια του κώδικα

        for i in range(
            5
        ):  # Τοποθετώ μέσα σε μια σειρά τα παρακάτω widget για να αποφύγω την επανάληψη τους
            self.lbl = Label(
                self, text="•", bg="#e1c9f8"
            )  # Δημιουργώ μια ταμπέλα με "•" σαν κείμενο
            self.lbl.grid(
                row=i + 1, column=0, sticky=W, padx=20
            )  # Τοποθετώ την ταμπέλα

            self.entry = ttk.Entry(
                self, width=30, font=("Helvetica", 10), bootstyle="danger"
            )
            self.entry.grid(row=i + 1, column=1, sticky=W + E + N + S, padx=10, pady=10)
            self.entry.bind("<Key>", self.char_limit)
            self.entries.append(self.entry)

        # Κάνω ακριβώς το ίδιο και για τη δεύτερη στήλη
        for i in range(5):
            self.lbl = Label(self, text="•", bg="#e1c9f8")
            self.lbl.grid(row=i + 1, column=2, sticky=W, padx=20)
            self.entry = ttk.Entry(
                self, width=30, font=("Helvetica", 10), bootstyle="danger"
            )
            self.entry.grid(row=i + 1, column=3, sticky=W + E + N + S, padx=10, pady=10)
            self.entry.bind(
                "<Key>", self.char_limit
            )  # Μια ενέργεια που γίνεται κάθε φορά που πατά ο χρήστης μια πλήκτρο στο entry πεδίο. Αυτή η ενέργεια καλεί την συνάρτηση self.char_limit κάθε φορά που πατά ο χρήστης ένα πλήκτρο
            self.entries.append(
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
            len(input_str) > 15
        ):  # Ελέγχει εάν το μήκος του string είναι μεγαλύτερο των 15 χαρακτήρων
            entry_widget.delete(
                0, "end"
            )  # Διαγράφει όλο το περιεχόμενο του entry πεδίου από την θέση 0 μέχρι το τέλος.
            entry_widget.insert(
                0, input_str[:15]
            )  # Καλείται μετά τη διαγραφή του περιεχόμενου του entry πεδίου για να εισάγει το νέο περιεχόμενο.


class Frame2(Frame):
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
            row=0, column=0, columnspan=3, sticky=W + E + N + S, pady=2, padx=250
        )  # Τοποθετώ την ταμπέλα

        self.text = Text(
            self, bg="#efe7ff", font=("Helvetica", 10), width=80, height=23
        )  # Δημιουργώ ένα text widget, στο οποίο ο χρήστης μπορεί να πληκρολογήσει ελεύθερα τις σκέψεις του
        self.text.grid(
            row=1, column=0, sticky=W + E + N + S, rowspan=1, columnspan=3, padx=10
        )  # Τοποθετώ το widget

        self.clear_all_button = ttk.Button(
            self,
            text="Clear Text",
            bootstyle="warning-link",
            width=85,
            command=self.clear_all,
        )
        self.clear_all_button.grid(row=2, column=0, columnspan=1, sticky=S + E)

    def clear_all(self):
        self.text.delete(1.0, END)


class Frame3(Frame):
    def __init__(self, parent, app):
        super().__init__(
            parent, bg="#e1c9f8"
        )  # Φτιάχνει το τρίτο πλαίσιο με parent widget
        # button1 -> save & quit
        self.app = app
        self.button1 = ttk.Button(
            self,
            text="Save & Quit",
            bootstyle="selectbg",
            command=self.save_and_quit_window,
        )  # Δημιουργώ ενα κουμπί "Save", το οποίο όταν πατηθεί αποθηκεύει ό,τι έχει γράψει ο χρήστης
        self.button1.grid(
            row=1, column=3, sticky=N + E + W + S, padx=555, pady=3
        )  # Τοποθετώ το κουμπί στο πλαίσιο

        self.button2 = ttk.Button(
            self, text="Exit", bootstyle="selectbg", command=self.exit_window
        )  # Δημιουργώ ένα κουμπί "Exit", το οποίο όταν πατηθεί κλείνει το παράθυρο
        self.button2.grid(
            row=1, column=1, sticky=N + E + W + S, padx=15, pady=3
        )  # Τοποθετώ το κουμπί στο πλαίσιο

    def exit_window(self):
        # self.state = "entry"
        self.app.state = "entry"
        self.master.destroy()  # Δημιουργώ την συνάρτηση για το κουμπί "Exit" , η οποία κλείνει το παράθυρο

    def save_and_quit_window(self):
        self.app.state = "exit"
        pass  # Δημιουργώ την συνάρτηση για το κουμπί "Save & Quit", η οποία αποθηκεύει τα στοιχεία του παραθύρου και το κλείνει


if __name__ == "__main__":
    app = JournalApp()
    app.main()
    # Θέτω ως παράμετρο της κλάσης App το ίδιο το παράθυρο, ώστε η κλάση αυτή να είναι υπεύθυνη για το περιεχόμενο και τη λειτουργικότητα του παραθύρου
    app.root.mainloop()  # Με αυτή τη μέθοδο ξεκινάει ο βρόχος επεξεργασίας γεγονότων
