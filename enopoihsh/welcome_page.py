import tkinter as tk
import random
import ttkbootstrap as ttk
from pathlib import Path

# import purple_theme_ttk


class WelcomePage:
    def __init__(self, root=None, app=None):
        self.root = root
        # Κραταμε μια μεταβλητη για state, που βοηθαει στην ενοποιηση του κωδικα
        # Την αρχικοποιουμε σαν exit για μπορει να κλεινει το παραθυρο
        self.state = "exit"

    def main(self):
        # Σπασαμε το κομματι του κωδικα που κανει initialize την αρχικη σελιδα
        if self.root is None:
            # Δημιουργει το παραθυρο tkinter που θα εμφανιστει
            # self.root = tk.Tk()
            # self.root = ttk.Window(themename="purpletheme")
            self.root = ttk.Window(themename="litera")

        self.root.title("MyJournal")
        self.root.geometry("1500x900")
        # Δεν επιτρεπει στον χρηστη να μπορει να κανει μεγενθυση ή σμικρυνση στο παραθυρο
        self.root.resizable(0, 0)

        # Με την συναρτηση Path βρισκουμε τον φακελο που τρεχει το αρχειο, με το __file__ και το .parent παμε ενα επιπεδο πανω
        folder = Path(__file__).parent
        # Φτιαχνουμε το absolute path για την εικονα που θελουμε να βαλουμε στο background
        image_background = Path(folder, "bg.png")
        # Τοποθετηση εικονας για bg
        self.bg = tk.PhotoImage(file=image_background)

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
            self.root, width=1500, height=900
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
        self.button_exit = ttk.Button(
            self.root,
            bootstyle="light",
            text="Exit",
            command=self.button_exit_pushed,
        )

        self.button_entry = ttk.Button(
            self.root, bootstyle="light", text="Entry", command=self.button_entry_pushed
        )

        # Τοποθετηση των κουμπιων στον κανβα
        self.button_exit_canvas = self.canvas.create_window(
            15, 800, anchor="nw", window=self.button_exit
        )

        self.button_entry_canvas = self.canvas.create_window(
            1400, 800, anchor="nw", window=self.button_entry
        )
        print("Welcome main")

    def button_exit_pushed(self):
        self.state = "exit"
        self.root.destroy()  # με το πατημα του κουμπιου 'exit' το παραθυρο κλεινει
        print("Root Main destroyed")

    def button_entry_pushed(self):
        # με το πατημα του κουμπιου 'entry' το παραθυρο κλεινει και ανοιγει το παραθυρο της εφαρμογης entry
        # Στο entry, δεν τρεχει το παραθυρο , αλλα στο journal κανει κανονικα την εναλλαγη
        self.state = "entry"
        # self.state = "journal"
        self.root.destroy()

    def b3_pushed(self):
        self.root.destroy()
        # clear_root(self.root)


if __name__ == "__main__":
    # root_welcomepage = ttk.Window(themename="litera")
    welcome_page = WelcomePage()
    welcome_page.main()
    welcome_page.root.mainloop()
