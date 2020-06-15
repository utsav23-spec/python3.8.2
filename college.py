from tkinter import *
from tkinter import messagebox
import sqlite3

################################################################
class guest:

    def __init__(self, root):
        self.root = root
        self.root.title("Guests List")
        self.root.geometry("1200x707")
        self.root.config(bg="light gray")
        self.root.resizable(0,0)

       # GstID = StringVar()
      ##  FirstName = StringVar()
      ##  LastName = StringVar()
     #   Age = StringVar()
      #  Address = StringVar()
      ##  Dob = StringVar()
      ##  Gender = StringVar()
      #  RoomNo = StringVar()
#
###################################################################
        #making function call
        def guestData():

            con = sqlite3.connect("guest.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS guest(id INTEGER PRIMARY KEY,GstID text,FirstName text,LastName text,Age text,Address text,Dob text,Gender text,RoomNo text, CheckIn text, CheckOut text)")
            con.commit()
            con.close()
        guestData()

#####################################################################

        def add_guestRec(GstID, FirstName, LastName, Age, Address, Dob, Gender, RoomNo, CheckIn, CheckOut):
            con = sqlite3.connect("guest.db")
            cur = con.cursor()
            cur.execute("INSERT INTO guest VALUES (NULL,?,?,?,?,?,?,?,?,?,?)",
                        (GstID, FirstName, LastName, Age, Address, Dob, Gender, RoomNo, CheckIn, CheckOut))
            con.commit()
            clear()
            con.close()


        def e_xit():
            e_xit = messagebox.askyesno("Confirm if want to exit")
            if e_xit > 0:
                root.destroy()
                return

       # def displayData():
        #    guestlist.delete(0, END)
         #   for rows in viewData():
          #      guestlist.insert(END, rows, str(""))
########################################################################
        def viewData():
            con = sqlite3.connect("guest.db")
            cur = con.cursor()
            cur.execute("SELECT *,oid FROM guest")
            rows = cur.fetchall()
            con.close()
            return rows

        def displayData():
            guestlist.delete(0, END)
            for rows in viewData():
                guestlist.insert(END, rows, str(""))

########################################################################

        def GuestRec(NONE):
            global sd
            searchGtd = guestlist.curselection()[0]
            sd = guestlist.get(searchGtd)


            GstID.delete(0, END)
            GstID.insert(END, sd[1])
            FirstName.delete(0, END)
            FirstName.insert(END, sd[2])
            LastName.delete(0, END)
            LastName.insert(END, sd[3])
            Age.delete(0, END)
            Age.insert(END, sd[4])
            Address.delete(0, END)
            Address.insert(END, sd[5])
            Dob.delete(0, END)
            Dob.insert(END, sd[6])
            Gender.delete(0, END)
            Gender.insert(END, sd[7])
            RoomNo.delete(0, END)
            RoomNo.insert(END, sd[8])
            eee.delete(0, END)
            eee.insert(END, sd[9])
            eeee.delete(0, END)
            eeee.insert(END, sd[10])

    #################################################################
        def delRec(id):
            con = sqlite3.connect("guest.db")
            cur = con.cursor()
            cur.execute("DELETE FROM guest WHERE id=?", (id,))
            con.commit()
            con.close()
        def deletee():
            delRec(sd[0])
            clear()
            displayData()
     ###########################clear##################################
        def clear():
            GstID.delete(0, END)
            FirstName.delete(0, END)
            LastName.delete(0, END)
            Age.delete(0, END)
            Dob.delete(0, END)
            Address.delete(0, END)
            Gender.delete(0, END)
            RoomNo.delete(0, END)
            eee.delete(0, END)
            eeee.delete(0, END)

    ######################################################################

        def searchData(GstID="", FirstName="", LastName="", Age="", Address="", Dob="", Gender="", RoomNo="", CheckIn="", CheckOut=""):
            con = sqlite3.connect("guest.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM guest WHERE GstID=? or FirstName=? or LastName=? or Age=? or Address=? or Dob=? or Gender=? or RoomNo=? or CheckIn=? or CheckOut=?", (GstID, FirstName, LastName, Age, Address, Dob, Gender, RoomNo, CheckIn, CheckOut))
            rows = cur.fetchall()
            con.close()
            return rows
        def displaysearch():
            guestlist.delete(0, END)
            for row in searchData(GstID.get(), FirstName.get(), LastName.get(), Age.get(), Address.get(), Dob.get() , Gender.get(), RoomNo.get(), eee.get(),eeee.get() ):
                guestlist.insert(END, row, str(""))


    ######################################################################

        def updateData(id, GstID="", FirstName="", LastName="", Age="", Address="", Dob="", Gender="", RoomNo=""):
            con = sqlite3.connect("guest.db")
            cur = con.cursor()
            cur.execute(" UPDATE guest SET GstID=?, FirstName=?, LastName=?, Age=?, Address=?, Dob=?, Gender=?, RoomNo=? WHERE id=?", ( GstID, FirstName, LastName, Age, Address, Dob, Gender, RoomNo, id))
            con.commit()
            con.close()
        def update():
            delRec(sd[0])
            add_guestRec(GstID.get(), FirstName.get(), LastName.get(), Age.get(), Address.get(), Dob.get() , Gender.get(), RoomNo.get(), eee.get(), eeee.get())
            guestlist.delete(0, END)
            guestlist.insert(END, GstID.get(), FirstName.get(), LastName.get(), Age.get(), Address.get(), Dob.get() , Gender.get(), RoomNo.get(), eee.get(), eeee.get())
            displayData()
    #####################################################################

        #main frame of the display
        Frame1 = Frame(self.root, bg="light gray")
        Frame1.pack()

        #frame for title
        Frame2 = Frame(Frame1, bd=1, bg="red", padx=140, pady=14)
        Frame2.pack(side=TOP)

        #label of the interface i.e the title of the page.
        lbl = Label(Frame2, font=("arial", 30, "bold"), text="The Everest Hotel", padx=140, pady=10, bg="blue", fg="red")
        lbl.pack()

        #frame for the input of guest information.
        Frame5 = Frame(Frame1, bd=2, bg="light grey", width=1350, height=70, pady=10)
        Frame5.pack(side=BOTTOM)

        Frame4 = LabelFrame(Frame1, text="Guest Details", bd=2, bg="light gray", width=1400, height=500, padx=20, pady=20, font=("arial", 35, "bold"))
        Frame4.pack(side=BOTTOM)

        Frame3 = LabelFrame(Frame4, bd=2, bg="light gray", width=500, height=500, padx=20, pady=20, font=("arial", 35, "bold"))
        Frame3.pack(side=LEFT)

        Frame6 = LabelFrame(Frame4, bd=2, bg = "light grey", text="Records",font=("arial", 21, "bold"), width=500, height=500, padx=20, pady=20)
        Frame6.pack(side=RIGHT)

##############################################################################33

        #frame for the necessary buttons.

        #frame for selection of the files.
        #Frame4 = Frame(Frame2, bd=2, bg="red", padx=30, pady=14)
        #Frame4.pack(side=TOP)

        #Frame3 = Frame(Frame2, bd=2, bg="red", padx=30, pady=14)
        #Frame3.pack(side=TOP)


#########################################################################################

        self.lblid = Label(Frame3, text="GUEST ID", font=("ariel", 21, "bold"), bg="light gray", padx=10, pady= 7)
        self.lblid.grid(row=0, column=0, sticky=W)

        self.lblfname = Label(Frame3, text="First Name", font=("ariel", 21, "bold"), bg="light gray", padx=10, pady=7)
        self.lblfname.grid(row=1, column=0, sticky=W)

        self.lbllname = Label(Frame3, text="Last Name", font=("ariel", 21, "bold"), bg = "light gray", padx=10, pady=7)
        self.lbllname.grid(row=2, column=0, sticky=W)

        self.lblage = Label(Frame3, text="Age", font=("ariel", 21, "bold"), bg="light gray", padx=10, pady=7)
        self.lblage.grid(row=3, column=0, sticky=W)

        self.lbladdress = Label(Frame3, text="Address", font=("ariel", 21, "bold"), bg = "light gray", padx=10, pady=7)
        self.lbladdress.grid(row=4, column=0, sticky=W)

        self.lbldob = Label(Frame3, text="DOB", font=("ariel", 21, "bold"), bg = "light gray", padx=10, pady=7)
        self.lbldob.grid(row=5, column=0, sticky=W)

        self.lblgender = Label(Frame3, text="Gender", font=("ariel", 21, "bold"), bg = "light gray", padx=10, pady=7)
        self.lblgender.grid(row=6, column=0, sticky=W)

        self.lblroomno = Label(Frame3, text="Room NO", font=("ariel", 21, "bold"), bg = "light gray", padx=10, pady=7)
        self.lblroomno.grid(row=7, column=0, sticky=W)

#############################################################################################3

        GstID=Entry(Frame3, width=30, font=("ariel", 14, "bold"), bd=2)
        GstID.grid(row=0, column=1)

        FirstName = Entry(Frame3, width=30, font=("ariel", 14, "bold"), bd=2)
        FirstName.grid(row=1, column=1)

        LastName = Entry(Frame3, width=30, font=("ariel", 14, "bold"), bd=2)
        LastName.grid(row=2, column=1)

        Age = Entry(Frame3, width=30,font=("ariel", 14, "bold"), bd=2)
        Age.grid(row=3, column=1)

        Address = Entry(Frame3, width=30, font=("ariel", 14, "bold"), bd=2)
        Address.grid(row=4, column=1)

        Dob = Entry(Frame3, width=30,font=("ariel", 14, "bold"), bd=2)
        Dob.grid(row=5, column=1)

        Gender = Entry(Frame3, width=30,font=("ariel", 14, "bold"), bd=2)
        Gender.grid(row=6, column=1)

        RoomNo = Entry(Frame3, width=30, font=("ariel", 14, "bold"), bd=2)
        RoomNo.grid(row=7, column=1)


####################################################################################################

        scrollbar =Scrollbar(Frame6)
        scrollbar.grid(row=0, column=1, sticky="ns")

        guestlist = Listbox(Frame6, width=52, height=14,font=("arial", 12, "bold"),yscrollcommand=scrollbar.set)
        guestlist.grid(row=0, column =0, padx=8, columnspan=2)
        guestlist.bind('<<ListboxSelect>>', GuestRec)
        scrollbar.configure(command = guestlist.yview)

        self.lll = Label(Frame6, text="Checkin", font=("ariel", 21, "bold"), bg="light gray", padx=8, pady=5)
        self.lll.grid(row=1, column=0, sticky=W)
        eee = Entry(Frame6, width=30, font=("ariel", 14, "bold"), bd=2)
        eee.grid(row=1, column=1)

        self.llll = Label(Frame6, text="Checkout", font=("ariel", 21, "bold"), bg="light gray", padx=8, pady=5)
        self.llll.grid(row=2, column=0, sticky=W)
        eeee = Entry(Frame6, width=30, font=("ariel", 14, "bold"), bd=2)
        eeee.grid(row=2, column=1)




#########################################################################################

        self.btn_add = Button(Frame5, text="Add", padx=63, pady=5, font=("ariel", 14, "bold"), bd=3, command=lambda:add_guestRec(GstID.get(), FirstName.get(), LastName.get(), Age.get(), Address.get(), Dob.get() , Gender.get(), RoomNo.get(), eee.get(), eeee.get()))
        self.btn_add.grid(row=0, column=0)

        self.btn_display = Button(Frame5, text="Display", padx=56, pady=5, font=("ariel", 14, "bold"), bd=3, command=displayData)
        self.btn_display.grid(row=0, column=1)

        self.btn_delete = Button(Frame5, text="Delete", padx=56, pady=5, font=("ariel", 14, "bold"), bd=3, command=deletee)
        self.btn_delete.grid(row=0, column=2)

        self.btn_search = Button(Frame5, text="Search", padx=56, pady=5, font=("ariel", 14, "bold"), bd=3, command=displaysearch)
        self.btn_search.grid(row=0, column=3)

        self.btn_update = Button(Frame5, text="Update", padx=56, pady=5, font=("ariel", 14, "bold"), bd=3, command=update)
        self.btn_update.grid(row=0, column=4)

        self.btn_exit = Button(Frame5, text="Exit", padx=63, pady=5,font=("ariel", 14, "bold"), bd=3, command = e_xit)
        self.btn_exit.grid(row=0, column=5)


########################################################################

root = Tk()
details = guest(root)
root.mainloop()

