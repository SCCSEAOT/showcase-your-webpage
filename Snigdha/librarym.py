from ast import Add
from importlib.resources import contents
from tkinter import *
from tkinter import *
from tkinter import ttk 
import pymysql
from tkinter import messagebox
class Library:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1350x700+0+0")
        
        #========Title Lable========
        title=Label(self.root,text="Library Management System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="#CC9B6D",fg="#FF2E63")
        title.pack(side=TOP,fill=X)
        
        #=====All Variables======
        self.regi_var=StringVar()
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.stream_var=StringVar()
        self.contact_var=StringVar()
        self.serialn_var=StringVar()
        self.issue_d_var=StringVar()
        self.return_d_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        
        
        #========Manage Frame=========
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#CC9B6D")
        Manage_Frame.place(x=10,y=70,width=450,height=580)
        
        m_title=Label(Manage_Frame,text="Student Details",bg="#CC9B6D",fg="#493323",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=4)
        #=========Registration no.===============
        lbl_regi=Label(Manage_Frame,text="Registration No.",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_regi.grid(row=1,column=0,padx=10,sticky="w")
        
        txt_regi=Entry(Manage_Frame,textvariable=self.regi_var,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_regi.grid(row=1,column=1,pady=10,padx=10,sticky="w")
        #==============Student Id==============
        lbl_id=Label(Manage_Frame,text="Student Id",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_id.grid(row=2,column=0,padx=10,sticky="w")
        
        txt_id=Entry(Manage_Frame,textvariable=self.id_var,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_id.grid(row=2,column=1,pady=10,padx=10,sticky="w")
        #================Name====================
        lbl_name=Label(Manage_Frame,text="Name",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=3,column=0,padx=10,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_name.grid(row=3,column=1,pady=10,padx=10,sticky="w")
        #==============Stream===================
        lbl_Stream=Label(Manage_Frame,text="Stream",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_Stream.grid(row=4,column=0,padx=10,sticky="w")
        
        combo_Stream=ttk.Combobox(Manage_Frame,textvariable=self.stream_var,font=("times new roman",13,"bold"),state='readonly')
        combo_Stream['values']=("DCST","DCE","DME","DEE")
        combo_Stream.grid(row=4,column=1,padx=10,pady=10)
        #===============Contact no.==============
        lbl_contact=Label(Manage_Frame,text="Contact No.",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_contact.grid(row=5,column=0,padx=10,sticky="w")
        
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=10,sticky="w")
        #===========Address===================
        lbl_address=Label(Manage_Frame,text="Address",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_address.grid(row=6,column=0,padx=10,sticky="w")
        
        self.txt_address=Text(Manage_Frame,width=25,height=2)
        self.txt_address.grid(row=6,column=1,padx=10,pady=10,sticky="w")
        #==========Book Serial No.=============
        lbl_serialn=Label(Manage_Frame,text="Book Serial No.",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_serialn.grid(row=7,column=0,padx=10,sticky="w")
        
        txt_serialn=Entry(Manage_Frame,textvariable=self.serialn_var,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_serialn.grid(row=7,column=1,pady=10,padx=10,sticky="w")
        #==================Date of Issue==================
        lbl_issue_d=Label(Manage_Frame,text="Issue Date",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_issue_d.grid(row=8,column=0,padx=10,sticky="w")
        
        txt_issue_d=Entry(Manage_Frame,textvariable=self.issue_d_var,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_issue_d.grid(row=8,column=1,pady=10,padx=10,sticky="w")
        #==========Date of Return===========
        lbl_return_d=Label(Manage_Frame,text="Return Date",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_return_d.grid(row=9,column=0,padx=10,sticky="w")
        
        txt_return_d=Entry(Manage_Frame,textvariable=self.return_d_var,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_return_d.grid(row=9,column=1,pady=10,padx=10,sticky="w")
        
        
        #============Button Frame===========
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#CC9B6D")
        btn_Frame.place(x=5,y=490,width=420,)
        
        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_studentdata).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        
        #==========Detail Frame==========
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#CC9B6D")
        Detail_Frame.place(x=480,y=70,width=780,height=580)    
        
        lbl_Search=Label(Detail_Frame,text="Search By",bg="#CC9B6D",fg="black",font=("times new roman",15,"bold"))
        lbl_Search.grid(row=0,column=0,padx=10,sticky="w")
    
        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15,font=("times new roman",13,"bold"),state='readonly')
        combo_Search['values']=("regi","id","serialn","name")
        combo_Search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        Searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        Showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#====================Table frame=============    
        
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#CC9B6D")
        Table_Frame.place(x=10,y=60,width=760,height=500)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Library_table=ttk.Treeview(Table_Frame,columns=("regi","id","name","stream","contact","address","serialn","issue_d","return_d"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Library_table.xview)
        scroll_y.config(command=self.Library_table.yview)
        self.Library_table.heading("regi",text="Registration No.")
        self.Library_table.heading("id",text="Student Id")
        self.Library_table.heading("name",text="Name")
        self.Library_table.heading("stream",text="Stream")
        self.Library_table.heading("contact",text="Contact No.")
        self.Library_table.heading("address",text="Address")
        self.Library_table.heading("serialn",text="Book Serial No.")
        self.Library_table.heading("issue_d",text="Issue Date")
        self.Library_table.heading("return_d",text="Return Date")
        self.Library_table['show']='headings'
        self.Library_table.column("regi",width=100)
        self.Library_table.column("id",width=100)
        self.Library_table.column("name",width=100)
        self.Library_table.column("stream",width=50)
        self.Library_table.column("contact",width=100)
        self.Library_table.column("address",width=100)
        self.Library_table.column("serialn",width=100)
        self.Library_table.column("issue_d",width=100)
        self.Library_table.column("return_d",width=100)
        self.Library_table.pack(fill=BOTH,expand=1)
        self.Library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
        
    def add_studentdata(self):
        if self.regi_var.get()=="" or self.name_var.get()=="":
                messagebox.showerror("Error","All fields are required!")
        else:
                con=pymysql.connect(host="localhost",user="root",password="",database="librarym")
                cur=con.cursor()
                cur.execute("insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.regi_var.get(),
                                                                                          self.id_var.get(),
                                                                                          self.name_var.get(),
                                                                                          self.stream_var.get(),
                                                                                          self.contact_var.get(),
                                                                                          self.txt_address.get('1.0',END),
                                                                                          self.serialn_var.get(),
                                                                                          self.issue_d_var.get(),
                                                                                          self.return_d_var.get()
                                                                                         ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")
        
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="librarym")
        cur=con.cursor()
        cur.execute("select * from studentdata")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Library_table.delete(*self.Library_table.get_children())
            for row in rows:
                self.Library_table.insert('',END,values=row)
                con.commit()
            con.close()        
    
    def clear(self):
        self.regi_var.set("")
        self.id_var.set("")
        self.name_var.set("")
        self.stream_var.set("")
        self.contact_var.set("")
        self.txt_address.delete('1.0',END)
        self.serialn_var.set("")
        self.issue_d_var.set("")
        self.return_d_var.set("")
    
    def get_cursor(self,ev):
        cursor_row=self.Library_table.focus()
        contents=self.Library_table.item(cursor_row)
        row=contents['values']
        self.regi_var.set(row[0])
        self.id_var.set(row[1])
        self.name_var.set(row[2])
        self.stream_var.set(row[3])
        self.contact_var.set(row[4])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[5])
        self.serialn_var.set(row[6])
        self.issue_d_var.set(row[7])
        self.return_d_var.set(row[8])
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="librarym")
        cur=con.cursor()
        cur.execute("update studentdata set regi=%s,id=%s,name=%s,stream=%s,contact=%s,address=%s,serialn=%s,issue_d=%s where return_d=%s",(
                                                                                                                                self.regi_var.get(),
                                                                                                                                self.id_var.get(),
                                                                                                                                self.name_var.get(),
                                                                                                                                self.stream_var.get(),
                                                                                                                                self.contact_var.get(),
                                                                                                                                self.txt_address.get('1.0',END),
                                                                                                                                self.serialn_var.get(),
                                                                                                                                self.issue_d_var.get(),
                                                                                                                                self.return_d_var.get()
                                                                                                                                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()       
        
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="librarym")
        cur=con.cursor()
        cur.execute("delete from studentdata where regi=%s",self.regi_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()   
    
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="librarym")
        cur=con.cursor()
        cur.execute("select * from studentdata where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Library_table.delete(*self.Library_table.get_children())
            for row in rows:
                self.Library_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    
    
        
    
    
    
root=Tk()
ob=Library(root)
root.mainloop()
