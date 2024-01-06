from welcome_page import WelcomePage

from date_selection import DateSelection
from teliko_montelo_ergasias import JournalApp as Journal
import tkinter as tk
import date_selection as datesec


class App:
    def __init__(self) -> None:
        self.state = "welcome"
        self.page = None
        self.root = None

    def main(self):
        while self.state != "exit":
            if self.state == "welcome":
                self.page = WelcomePage(self.root)
            elif self.state == "entry":
                self.page = DateSelection(self.root)
            elif self.state == "journal":
                self.page = Journal(self.root)
                self.page.state = "welcome"
            else:
                self.state = "exit"
                break

            # if self.state != "entry":
            self.page.main()
            self.page.root.mainloop()
            self.state = self.page.state


if __name__ == "__main__":
    app = App()
    app.main()
