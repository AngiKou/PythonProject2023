import tkinter as tk
import random
import ttkbootstrap as ttk

class WelcomePage():
    def __init__(self,root_welcomepage):
        self.w = root_welcomepage
        self.w.title('MyJournal')
        self.w.geometry('1500x900')
        self.w.resizable(0,0)#Δεν επιτρεπει στον χρηστη να μπορει να κανει μεγενθυση ή σμικρυνση στο παραθυρο
        self.bg = tk.PhotoImage(file='bg.png')#Τοποθετηση εικονας για bg
        
        #Λιστα με τυχαια quotes
        self.randomquotes = ['Love yourself first and everything else falls into line. — Lucille Ball',
                             '"The most common way people give up their power is by thinking they do not have any." — Alice Walker',
                             '"Stand before the people you fear and speak your mind even if your voice shakes." — Maggie Kuhn',
                             '"You cannot turn back the clock. But you can wind it up again." — Bonnie Prudden',
                             '"A problem is a chance for you to do your best." — Duke Ellington',
                             '"Give light and people will find the way." — Ella Baker',
                             '"It always seems impossible until it is done." — Nelson Mandela',
                             '"Failure is the condiment that gives success its flavor." — Truman Capote',
                             ' "Keep your face always toward the sunshine, and shadows will fall behind you." — Walt Whitman']
        #Χρηση της συναρτησης random.choice ωστε η μεταβλητη self.quote να παιρνει τυχαια την τιμη ενος quote σε μορφη string
        self.quote = random.choice(self.randomquotes)
        
        self.canvas = tk.Canvas(self.w, width=1500, height=900)#Δημιουργια κανβα για τοποθετηση των κουμπιων, τoυ random quote και του bg
        self.canvas.pack(fill = 'both', expand = 1)#Τοποθετηση του κανβα μεσα στο παραθυρο αφου εχει οριστει το μεγεθος του παραπανω και με συνθηκες μεσα στο .pack() ωστε να καταλαμβανει ολοκληρο τον χωρο
        self.canvas.create_image(0,0,image=self.bg,anchor='nw')#Δημιουργια της εικονας που βρισκετε στο bg με συνθηκες ωστε να πιανει ολοκληρο τον χωρο του κανβα
        
        #Δημιουργια κειμενου με text το τυχαιο quote και συνθηκες ωστε να βγαινει στην μεση της σελιδας και απο πανω 'Quote of the day:'
        self.canvas.create_text(750,390,text = 'Quote of the day:',font=('Open Sans',30,'bold'),fill='black')
        self.canvas.create_text(750,450,text = self.quote,font=('Open Sans',30,'bold'),fill='black')#Δημιουργια κειμενου με text το τυχαιο quote και συνθηκες ωστε να βγαινει στην μεση της σελιδας
        
        #Δημιουργια των κουμπιων 'Exit' 'Show Statistics' και 'Entry'
        self.b1 = ttk.Button(self.w,bootstyle="light",text='Exit',font=('Arial',20),command = self.b1_pushed, bg = '#e4d6ff',fg = 'black') 
        self.b2 = ttk.Button(self.w,bootstyle="light",text='Show Statistics',font=('Arial',20),command= self.b2_pushed, bg = '#e4d6ff',fg='black')
        self.b3 = ttk.Button(self.w,bootstyle="light",text='Entry',font=('Arial',20),command = self.b2_pushed)
        
        #Τοποθετηση των κουμπιων στον κανβα
        self.b1_canvas = self.canvas.create_window(15,800,anchor='nw',window=self.b1) 
        self.b2_canvas = self.canvas.create_window(680,800,anchor='nw',window=self.b2)
        self.b3_canvas = self.canvas.create_window(1400,800,anchor='nw',window=self.b3)
    
    def b1_pushed(self):
        self.w.destroy()#με το πατημα του κουμπιου 'exit' το παραθυρο κλεινει
    def b2_pushed(self):
        self.w.destroy()
        #εδω θα ανοιγει το παραθυρο των στατιστικων(συμπληρωση κατα την συνοχη των κωδικων)
        
    def b3_pushed(self):
        self.w.destroy()
        #εδω θα ανοιγει το παραθυρο του πολιτη (συμπληρωση κατα την συνοχη των κωδικων)
        


root_welcomepage = tk.Tk()
WelcomePage(root_welcomepage)
root_welcomepage.mainloop()

