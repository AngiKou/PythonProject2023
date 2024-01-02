import tkinter as tk
import ttkbootstrap as ttk

root=ttk.Window(themename="purpletheme")

root.geometry("650x600")
root.title("Date Selection")
root.columnconfigure((0,1,2,3,4),weight=1)
root.rowconfigure((0,1,2,3,4,5,6),weight=1)


def getdate():
    #grab date.This is the variable that should be used to open the current date window
    datepicked=dateentry.entry.get()
    strvar.set(value=f"Selected-Date is {datepicked}")
def newwindow():
    """Create a new window"""
    def getpassword():
        password = passwordentry.get()
        realpassword="1234"
        if realpassword==password:
            app2=ttk.Toplevel()
            app2.geometry("450x350")
            app2.title("Doctors setting's")
            win.destroy()
            lbl=ttk.Label(app2,bootstyle="secondary",text="               Change the doctors notes then press save\n(please press enter before hitting the border of the text box)")
            lbl.pack(padx=10, pady=10)
            textfordoc=ttk.Text(app2,height=5,width=39,takefocus=True)
            textfordoc.pack(padx=10,pady=10)
            def save():
                docnotes=textfordoc.get("1.0","end")
                notevar.set(docnotes)

            btn=ttk.Button(app2,bootstyle="primary",text="Save",command=save)
            btn.pack(ipadx=40, ipady=10)
        
        else:
            labelerror=ttk.Label(win,text="Wrong Password! Try again",bootstyle="secondary-inverse")
            labelerror.grid(row=1,column=1,rowspan=3,sticky="n",pady=10,padx=(0,15))
            passwordentry.delete(0,"end")
            
    win = tk.Toplevel(root)
    win.geometry("400x120")
    win.title("Password entry")
    win.rowconfigure((0,1,2,3),weight=1)
    win.columnconfigure((0,1,2,3),weight=1)
    passwordentry=ttk.Entry(win,show="*",bootstyle="warning",takefocus=True)
    passwordentry.grid(row=0,column=1,padx=(10,30),sticky="we")
    password=ttk.Label(win,bootstyle="secondary",text="Password:",)
    password.grid(row=0,column=0,padx=(10,0),sticky="e")
    buttonpassword=ttk.Button(win,text="Sumbit",bootstyle="secondary-outline",command=getpassword)
    buttonpassword.grid(row=0,column=2,sticky="w",padx=0)


bg=tk.PhotoImage(file="C:\\Users\\gpoli\\Desktop\\CALENDAR PROJECT\\violet-watercolor-texture-background.png")
backgroundphoto=ttk.Label(root,image=bg)
backgroundphoto.place(x=0,y=0,relwidth=1,relheight=1)

#label next to the date entry
titlelabel=ttk.Label(root,text="select a date:",bootstyle="primary-inverse")
titlelabel.grid(row=0,column=1,sticky="e",padx=10,pady=15)
#dateentry widget
dateentry=ttk.DateEntry(root)
dateentry.grid(row=0,column=2,sticky="we",pady=10)

#random default value
count=10
#count should be a variable that is used as(count=+1) so that everytime
#the button is clicked it adds +1 to count and displays on the meter the current datestreak
datestreak=count
#the line in between statistics and date selection. Makes the app look better
separationline=ttk.Separator(root,bootstyle="primary")
separationline.grid(row=1,columnspan=4,stick="ew",padx=30,pady=(35,10))
#the label frame 
labelframe=ttk.LabelFrame(root,
                          bootstyle="primary",
                          relief="ridge",
                          text="Statistics-Notes")
labelframe.grid(row=2,column=0,columnspan=4,rowspan=4,sticky="wen",padx=25)
#the meter that appears this way
meterstats=ttk.Meter(labelframe, 
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
                     textright='Days',
                     stepsize=1,
                     stripethickness=6,
                     )
meterstats.grid(row=0,column=0,columnspan=2,pady=25,padx=(20,0))
#basicaly the title that says Doctor's notes. it works like a frame widget which will contain the notefordoctor Label 
doctorsnoteframe=ttk.LabelFrame(labelframe,
                                text="Doctor's Notes:"
                                ,width=150
                                ,height=100,
                                relief="flat",
                                
                                bootstyle="secondary"
                                )
doctorsnoteframe.grid(row=0,column=2,rowspan=3,columnspan=3,padx=50,sticky="ne")
underlining=ttk.Separator(doctorsnoteframe,bootstyle="primary")
underlining.grid(row=0,column=0,sticky="wne",padx=(0,175))
#this notevar variable should be able to change by the doctor from doctor settings
notevar=tk.StringVar(value="Dont forget to always tell good things\n to yourself when you look at the mirror,\nand to always acknowledge the importance\n of the effort you put in your work")
notefordoctor=ttk.Label(doctorsnoteframe,bootstyle="secondary",textvariable=notevar)
notefordoctor.grid(row=1,column=0,pady=7,sticky="w")




#button that confirms the selected date
confirmbutton=ttk.Button(root,text="Press to confirm",bootstyle="primary-outline",
                         command=getdate,
                         )
confirmbutton.grid(row=0,column=3,sticky="w",padx=10)

strvar=tk.StringVar(value="Waiting for a date to be selected")
mylabel=ttk.Label(root,bootstyle="primary-inverse",textvariable=strvar)
mylabel.grid(row=1,column=2,sticky="n")


docsbutton=ttk.Button(root,text="Enter as Doctor",command=newwindow,bootstyle="primary-outlined")
docsbutton.grid(row=5,column=2)



root.mainloop()