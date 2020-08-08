#lib management system.

from tkinter import *
import tkinter.messagebox

class Library:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Database Management System")
        self.root.geometry("1350x750+0+0")

        MTy = StringVar()
        Ref = StringVar()
        Tit = StringVar()
        fna = StringVar()
        sna = StringVar()
        Adr1 = StringVar()
        Adr2 = StringVar()
        pcd = StringVar()
        MNo = StringVar()
        Bkid = StringVar()
        Bkt = StringVar()
        BkT = StringVar()
        Atr = StringVar()
        DBo = StringVar()
        Ddu = StringVar()
        sPr = StringVar()
        LrF = StringVar()
        DoD = StringVar()
        DonL = StringVar()

    #===================================================FRAME==========================================================

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=40, pady=8, bg="cadet blue", relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTit = Label(TitleFrame, font=('arial', 46, 'bold'), text="Library Database Management System")
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=100, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=0, width=1350, height=50, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=800, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text="Library Membership Info:",bg="cadet blue")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=20, pady=3, relief=RIDGE,font=('arial', 12, 'bold'), bg="cadet blue", text="Book Details",)
        DataFrameRight.pack(side=RIGHT)
        #======================================label and  entry========================================================

        self.lblMemberType = Label(DataFrameLeft, font=("arial",12 ,"bold"), text="Member Type", padx=2,pady=2,bg="cadet blue")
        self.lblMemberType.grid(row=0, column=0, sticky=W)
        self.TxtMType = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=MTy, width=25)
        self.TxtMType.grid(row=0, column=1)

        self.lblBKIDType = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book ID", padx=2, pady=2,bg="cadet blue")
        self.lblBKIDType.grid(row=0, column=2, sticky=W)
        self.TxtBKID = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Bkid, width=25)
        self.TxtBKID.grid(row=0, column=3)

        self.lblRef = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference N0:", padx=2, pady=2, bg="cadet blue")
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.TxtRef = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Ref, width=25)
        self.TxtRef.grid(row=1, column=1)

        self.lblBkt = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book title:", padx=2, pady=2,bg="cadet blue")
        self.lblBkt.grid(row=1, column=2, sticky=W)
        self.TxtBkt = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Bkt, width=25)
        self.TxtBkt.grid(row=1, column=3)

        self.lblTit = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Title:", padx=2, pady=2,bg="cadet blue")
        self.lblTit.grid(row=2, column=0, sticky=W)
        self.TxtTit = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Tit, width=25)
        self.TxtTit.grid(row=2, column=1)

        self.lblAtr = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Author:", padx=2, pady=2,bg="cadet blue")
        self.lblAtr.grid(row=2, column=2, sticky=W)
        self.TxtAtr = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Atr, width=25)
        self.TxtAtr.grid(row=2, column=3)

        self.lblfna = Label(DataFrameLeft, font=("arial", 12, "bold"), text="First Nmae:", padx=2, pady=2,bg="cadet blue")
        self.lblfna.grid(row=3, column=0, sticky=W)
        self.Txtfna = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=fna, width=25)
        self.Txtfna.grid(row=3, column=1)

        self.lblDBo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Borrowed:", padx=2, pady=2,bg="cadet blue")
        self.lblDBo.grid(row=3, column=2, sticky=W)
        self.TxtDBo = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=DBo, width=25)
        self.TxtDBo.grid(row=3, column=3)

        self.lblsna = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Surname:", padx=2, pady=2,bg="cadet blue")
        self.lblsna.grid(row=4, column=0, sticky=W)
        self.Txtsna = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=sna, width=25)
        self.Txtsna.grid(row=4, column=1)

        self.lblDdu = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Due:", padx=2, pady=2,bg="cadet blue")
        self.lblDdu.grid(row=4, column=2, sticky=W)
        self.TxtDdu = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Ddu, width=25)
        self.TxtDdu.grid(row=4, column=3)

        self.lblAdr1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Addres 1:", padx=2, pady=2,bg="cadet blue")
        self.lblAdr1.grid(row=5, column=0, sticky=W)
        self.TxtAdr1 = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Adr1, width=25)
        self.TxtAdr1.grid(row=5, column=1)

        self.lblDonL = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Days on loan:", padx=2, pady=2,bg="cadet blue")
        self.lblDonL.grid(row=5, column=2, sticky=W)
        self.TxtDonL = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=DonL, width=25)
        self.TxtDonL.grid(row=5, column=3)

        self.lblAdr2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Addres 2:", padx=2, pady=2,bg="cadet blue")
        self.lblAdr2.grid(row=6, column=0, sticky=W)
        self.TxtAdr2 = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=Adr2, width=25)
        self.TxtAdr2.grid(row=6, column=1)

        self.lblLrf = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Late Return Fine:", padx=2, pady=2,bg="cadet blue")
        self.lblLrf.grid(row=6, column=2, sticky=W)
        self.TxtLrf = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=LrF, width=25)
        self.TxtLrf.grid(row=6, column=3)

        self.lblpcd = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post code:", padx=2, pady=2,bg="cadet blue")
        self.lblpcd.grid(row=7, column=0, sticky=W)
        self.Txtpcd = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=pcd, width=25)
        self.Txtpcd.grid(row=7, column=1)

        self.lblDoD = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Over due:", padx=2, pady=2,bg="cadet blue")
        self.lblDoD.grid(row=7, column=2, sticky=W)
        self.TxtDoD = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=DoD, width=25)
        self.TxtDoD.grid(row=7, column=3)

        self.lblMNo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile No:", padx=2, pady=2,bg="cadet blue")
        self.lblMNo.grid(row=8, column=0, sticky=W)
        self.TxtMNo = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=MNo, width=25)
        self.TxtMNo.grid(row=8, column=1)

        self.lblsPr = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Selling Price:", padx=2, pady=2,bg="cadet blue")
        self.lblsPr.grid(row=8, column=2, sticky=W)
        self.TxtsPr = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=sPr, width=25)
        self.TxtsPr.grid(row=8, column=3)

        #====================================listbox and scrollbar==================================================

        scrolbar=Scrollbar(DataFrameRight)








if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()