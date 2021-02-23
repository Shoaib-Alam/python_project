from tkinter import*
from add_medicine import Medicine
from Add_window import*
import psycopg2
from psycopg2 import Error


try:
    connect = psycopg2.connect(user = "postgres",
                               password = "Shoaib",
                               port = "5433",
                               host = "localhost",
                               database = "postgres")
    cursor = connect.cursor()
    
    table_name  = "faisal_medical"
    # InsertQry  = "INSERT INTO "+table_name+" values(3, 'Abdus');"
    # cursor.execute(InsertQry)
    # connect.commit()

except(Exception, Error)as error:
    print("Error while connecting to postgreSQL", error)



class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x800+0+0')
        self.root.title("Life easy")
        self.root.configure(background = 'powder blue')
        self.name_var = StringVar()


    def mainwindow(self):
        Var1 = [1,2,3,4,5]
        #================================Title Frame===================================
        TitleFrame = Frame(self.root, bd=5, width=1350, height=30,padx = 50,pady = 5, bg='blue', relief=RIDGE)
        TitleFrame.pack(side=TOP, fill=X)

        MainLabel = Label(TitleFrame, text= 'FAISAL MEDICAL STORE',padx=2, justify=LEFT, font=('arial', 16, 'bold'),
                      bd=8,bg='cadet blue',
                      fg='black').grid(row=0, column=0)
        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_list(self.root))
        #self.entry = Entry(self.root, textvariable=self.search_var, width=13).pack()

        #================================FRAMES===================================
        MainFrame = Frame(self.root, bd=5, width=1350, height=150,padx = 10,pady = 5, bg='cadet blue', relief=RIDGE)
        MainFrame.pack(side=TOP, fill=X)
        #
        Frame2 = Frame(self.root, bd=5, width=1350, height=50,padx = 2,pady = 2, bg='cadet blue', relief=RIDGE)
        Frame2.pack(side=BOTTOM, fill=X)

        #
        Frame1 = Frame(self.root, bd=5, width=200, height=500,padx = 2,pady = 2, bg='cadet blue', relief=RIDGE)
        Frame1.pack(side=LEFT, fill=Y)

        #

        #Main Frame Labels and Entries Start
        Label1 = Label(MainFrame, text= 'Product:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=LEFT).grid(row=1,column=0)

        self.Entry1 = Entry(MainFrame, textvariable=self.search_var, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT)
        self.Entry1.grid(row=1,column=1)

        Label2 = Label(MainFrame, text= 'Pack:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=RIGHT).grid(row=1,column=2)

        Entry2 = Entry(MainFrame, textvariable = Var1, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT).grid(row=1,column=3)

        Label3 = Label(MainFrame, text= 'QTY:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=LEFT).grid(row=1,column=4)

        Entry3 = Entry(MainFrame, textvariable = Var1, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT).grid(row=1,column=5)

        Label4 = Label(MainFrame, text= 'MRP:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=RIGHT).grid(row=1,column=6)

        Entry4 = Entry(MainFrame, textvariable = Var1, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT).grid(row=1,column=7)

        Label5 = Label(MainFrame, text= 'Amount:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=LEFT).grid(row=2,column=0)

        Entry5 = Entry(MainFrame, textvariable = Var1, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT).grid(row=2,column=1)

        Label6 = Label(MainFrame, text= 'SGST:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=RIGHT).grid(row=2,column=2)

        Entry6 = Entry(MainFrame, textvariable = Var1, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT).grid(row=2,column=3)

        Label7 = Label(MainFrame, text= 'CGST:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=LEFT).grid(row=2,column=4)

        Entry7 = Entry(MainFrame, textvariable = Var1, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT).grid(row=2,column=5)

        Label8 = Label(MainFrame, text= 'Batch:', font=('arial', 15, 'bold'),
                       bd=8,bg='cadet blue',
                       fg='black', width=10, justify=RIGHT).grid(row=2,column=6)

        Entry8 = Entry(MainFrame, textvariable = Var1, font=('arial', 16, 'bold'),
                       bd=8, fg='black', width=14, justify=LEFT).grid(row=2,column=7)

        AddButton = Button(MainFrame, text='ADD', width=15,height=2,
                           activebackground='green',bd=3).grid(row=1, column=8, padx=50)

        ResetButton = Button(MainFrame, text='RESET', width=15,height=2,
                             activebackground='green',bd=3).grid(row=2, column=8, padx=50)

        #Main Frame Labels and Entries End

       #Create Listbox to show entire me
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.lbox = Listbox(self.root, width=20, height=2,bg='lightgray'
                            ,selectforeground='yellow',
                            highlightcolor='red',highlightthickness=6,selectborderwidth=1,
                            relief='groove',bd=5,activestyle='none',fg='blue',font=('Calibri',15,))
        self.lbox.pack(side = RIGHT, fill=Y,ipadx=10,ipady=50)
        self.lbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command = self.lbox.yview)
        Text1 = Text(self.root, width=200, height=660).pack()

        self.update_list(self.root)


        Button1 = Button(Frame1, text='SALE', width=20,height=5,activebackground='green',bd=3).pack()
        Button2 = Button(Frame1, text='Customer', width=20,height=5,activebackground='red',bd=3).pack()
        self.Button3 = Button(Frame1, text='Add Medicine', width=20,height=5,activebackground='cyan',bd=3,
                              command=self.Open_New_Window)
        self.Button3.pack()
        Button4 = Button(Frame1, text='Dashboard', width=20,height=5,activebackground='red',bd=3).pack()


    def update_list(self,root):
        search_term = self.search_var.get()
        selectQry = "Select product from "+table_name
        cursor.execute(selectQry)
        result = cursor.fetchall();
        M_list = []

        for i in result:
            print(i[0])
            M_list.append(i[0])

        print(M_list)
        # Just a generic list to populate the listbox
        # M_list = ['Abacavir', 'Abacavir / dolutegravir / lamivudine', 'Acyclovir', 'Bob',
        # 'James', 'Frank', 'Susan', 'Amanda', 'Christie','Shoaib','Alam','Faisal','Rex','Cricon',
        # 'Adam', 'Lucy', 'Barry', 'Bob',
        # 'James', 'Frank', 'Susan', 'Amanda', 'Christie','Shoaib','Alam','Faisal','Rex','Cricon']

        user = Medicine('Shoaib')


        for item in M_list:
            user.Add_med(item)


        lbox_list=user.Lists

        self.lbox.delete(0, END)

        for item in lbox_list:
            if search_term.lower() in item.lower():
                self.lbox.insert(END, item)


    def submit(self):
        name = self.name_var.get()
        selQry = 'Select "'+table_name+'.Id" from '+table_name+' Order by id DESC LIMIT 1'
        my_query = cursor.execute(selQry)
        print(my_query)
        id = 108
        inqry = "INSERT INTO "+table_name+" values("+str(id)+", '"+name+"');"
        print(inqry)
        cursor.execute(inqry)
        connect.commit()


    def Open_New_Window(self):
        newWindow = Toplevel(root)
        newWindow.title("New Window")
        newWindow.geometry("300x600")


        newFrame1 = Frame(newWindow, bd=5, width=200, height=600,padx = 10,pady = 5, bg='cadet blue', relief=RIDGE)
        newFrame1.pack(side=TOP, fill=X)

        newLabel1 = Label(newFrame1,text="Name:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=0)
        newEntry1 = Entry(newFrame1,textvariable =self.name_var ,bd=5).place(x=70,y=0)

        newLabel1 = Label(newFrame1,text="Pack:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=30)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=30)

        newLabel1 = Label(newFrame1,text="Exp:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=60)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=60)

        newLabel1 = Label(newFrame1,text="MPR:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=90)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=90)

        newLabel1 = Label(newFrame1,text="Batch:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=120)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=120)

        newLabel1 = Label(newFrame1,text="Rate:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=150)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=150)

        newLabel1 = Label(newFrame1,text="SGST:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=180)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=180)

        newLabel1 = Label(newFrame1,text="CGST:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=210)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=210)

        newLabel1 = Label(newFrame1,text="Total Qty:",bg='cadet blue',font=('system',10,'bold')).place(x=0,y=240)
        newEntry1 = Entry(newFrame1,text="",bd=5).place(x=70,y=240)


        AddButton = Button(newFrame1,command=self.submit,text='ADD', width=15,height=2,
                            activebackground='green',bd=3).place(x=30,y=270)



root = Tk()

obj = Bill_App(root)
obj.mainwindow()
root.mainloop()
