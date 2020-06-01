from tkinter import *
import  tkinter.messagebox
import sqlite3
from main2 import *


#class for front end UI
class Product:
    def __init__(self,root):
        p= database()
        p.conn()
        self.root = root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="yellow")

        pId=StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany= StringVar()
        pContact = StringVar()

        def close():
            print("Product : close method callled")
            close = tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM",
                                                "Do you really want to close the system??")
            if close > 0:
                root.quit()
                print("Product: close method finished\n")
                return

        def clear():
            print("product: clear methoid clled")
            self.txtpId.delete(0, END)
            self.txtpName.delete(0, END)
            self.txtpPrice.delete(0, END)
            self.txtpQty.delete(0, END)
            self.txtpCompany.delete(0, END)
            self.txtpContact.delete(0, END)
            print("product: clear finished")

        def insert():
            print("product: insert method starts")
            if (len(pId.get())!=0):
                p.insert(pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get())
                productlist.delete(0,END)
                productlist.insert(END,pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get())
                showilist()
            else:
                tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM",
                                            "Enter product Id")
            print("Product: insert method finished")

        def showilist():
            print("product: show method ")
            productlist.delete(0,END)
            for row in p.show():
                productlist.insert(END, row, str(""))
            print("product: show prduct finished\n")

        def prodrec(event):
            print("product: prodrec called")
            global pd
            searchpd = productlist.curselection()[0]
            pd= productlist.get(searchpd)
            self.txtpId.delete(0,END)
            self.txtpId.insert(END, pd[0])

            self.txtpName.delete(0, END)
            self.txtpName.insert(END, pd[1])

            self.txtpPrice.delete(0, END)
            self.txtpPrice.insert(END, pd[2])

            self.txtpQty.delete(0, END)
            self.txtpQty.insert(END, pd[3])

            self.txtpCompany.delete(0, END)
            self.txtpCompany.insert(END, pd[4])

            self.txtpContact.delete(0, END)
            self.txtpContact.insert(END, pd[5])

            print("product: prodrec finished")

        def delete():
            print("prodcuct: delete starts")
            if (len(pId.get())!=0):
                p.delete(pd[0])
                clear()
                showilist()
            print("prodct: delete finished")

        def search():
            print("product: search method")
            productlist.delete(0,END)
            for row in p.search(pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get()):
                productlist.insert(END, row, str(""))
            print("product: seacrch finished")

        def update():
            print("product: update called")
            if (len(pId.get()!=0)):
                print("pd[0]",pd[p])
                p.delete(pd[0])
            if(len(pId.get()!=0)):
                p.insert(pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get())
                productlist.delete(0,END)
            productlist.insert(END,(pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get()))
            print("product: update finished")

        #create frame
        mainframe = Frame(self.root,bg="RED")
        mainframe.grid()
        headframe = Frame(mainframe,bd=1, padx=50,pady=10, bg="white",relief=RIDGE)
        headframe.pack(side=TOP)

        self.ITitle = Label(headframe, font=("arial", 43,"bold"),fg="red",text="WAREHOUSE INVENTORY SALES PURCHASE",bg="white")
        self.ITitle.grid()

        operationframe = Frame(mainframe, bd=1, width=1300, height=60,padx=50,pady=20,bg="white",relief=RIDGE)
        operationframe.pack(side=BOTTOM)

        bodyframe = Frame(mainframe,bd=2,width=1290, height=400, padx=30,pady=20,bg="white", relief=RIDGE )
        bodyframe.pack(side=BOTTOM)

        lefbody = LabelFrame(bodyframe, bd=2, width=600, height=380, padx=20, pady=10, bg="yellow", relief=RIDGE, font=("arial",13,"bold"),text="PRODUCT ITEM DETAILS:")
        lefbody.pack(side=LEFT)

        rigbody = LabelFrame(bodyframe, bd=2, width=300, height=380, padx=20, pady=10, bg="yellow", relief=RIDGE,
                             font=("arial", 13, "bold"), text="PRODUCT ITEM INFORMATION:")
        rigbody.pack(side=LEFT)

        #add widgets to left body fram
        self.labelpId= Label(lefbody, font=("arial",15,"bold"), text="Product ID", padx=2, bg="white", fg="blue",pady=2)
        self.labelpId.grid(row=0,column=0, sticky="w")
        self.txtpId = Entry(lefbody, font=("arial",15,"bold"), textvariable=pId, width=35)
        self.txtpId.grid(row=0, column=1, sticky="w")

        self.labelpName= Label(lefbody, font=("arial",15,"bold"), text="Product Name", padx=2, bg="white", fg="blue",pady=2)
        self.labelpName.grid(row=1,column=0, sticky="w")
        self.txtpName = Entry(lefbody, font=("arial",15,"bold"), textvariable=pName, width=35)
        self.txtpName.grid(row=1, column=1, sticky="w")

        self.labelpPrice= Label(lefbody, font=("arial",15,"bold"), text="Product Price", padx=2, bg="white", fg="blue",pady=2)
        self.labelpPrice.grid(row=2,column=0, sticky="w")
        self.txtpPrice = Entry(lefbody, font=("arial",15,"bold"), textvariable=pPrice, width=35)
        self.txtpPrice.grid(row=2, column=1, sticky="w")

        self.labelpQty= Label(lefbody, font=("arial",15,"bold"), text="Product Qty", padx=2, bg="white", fg="blue",pady=2)
        self.labelpQty.grid(row=3,column=0, sticky="w")
        self.txtpQty = Entry(lefbody, font=("arial",15,"bold"), textvariable=pQty, width=35)
        self.txtpQty.grid(row=3, column=1, sticky="w")

        self.labelpCompany= Label(lefbody, font=("arial",15,"bold"), text="Product Company", padx=2, bg="white",pady=2,fg="blue")
        self.labelpCompany.grid(row=4,column=0, sticky="w")
        self.txtpCompany = Entry(lefbody, font=("arial",15,"bold"), textvariable=pCompany, width=35)
        self.txtpCompany.grid(row=4, column=1, sticky="w")

        self.labelpContact= Label(lefbody, font=("arial",15,"bold"), text="Product Contact No.", padx=2, bg="white", fg="blue",pady=2)
        self.labelpContact.grid(row=5,column=0, sticky="w")
        self.txtpContact = Entry(lefbody, font=("arial",15,"bold"), textvariable=pContact, width=35)
        self.txtpContact.grid(row=5, column=1, sticky="w")

        self.labelpC1 = Label(lefbody, padx=2, pady=2)
        self.labelpC1.grid(row=6, column=0,sticky="w")

        self.labelpC2 = Label(lefbody, padx=2, pady=2)
        self.labelpC2.grid(row=7, column=0,sticky="w")

        self.labelpC3 = Label(lefbody, padx=2, pady=2)
        self.labelpC3.grid(row=8, column=0,sticky="w")

        self.labelpC4 = Label(lefbody, padx=2, pady=2)
        self.labelpC4.grid(row=9, column=0,sticky="w")

        #add SCROLL BAR
        scroll = Scrollbar(rigbody)
        scroll.grid(row=0, column=1, sticky="ns")

        productlist = Listbox(rigbody, width=40, height= 16, font=("arial",15,"bold"), yscrollcommand=scroll.set)
        productlist.bind('<<ListboxSelect>>',prodrec)
        productlist.grid(row=0,column=0,padx=8)
        scroll.config(command= productlist.yview)

        #add button  to operation frame
        self.bshow =  Button(operationframe, text="Show",font=("arial",20,"bold"),height=1, width=8,bd=4,padx=2,command=showilist)
        self.bshow.grid(row=0,column=0)

        self.bsave =  Button(operationframe, text="Save",font=("arial",20,"bold"),height=1, width=10,bd=4,padx=2,command=insert)
        self.bsave.grid(row=0,column=1)

        self.breset =  Button(operationframe, text="Reset",font=("arial",20,"bold"),height=1, width=10,bd=4,padx=2,command=clear)
        self.breset.grid(row=0,column=2)

        self.bdelete =  Button(operationframe, text="Delete",font=("arial",20,"bold"),height=1, width=10,bd=4,padx=2,command=delete)
        self.bdelete.grid(row=0,column=3)

        self.bsearch =  Button(operationframe, text="Search",font=("arial",20,"bold"),height=1, width=10,bd=4,padx=2,command=search)
        self.bsearch.grid(row=0,column=4)

        self.bupdate =  Button(operationframe, text="Update",font=("arial",20,"bold"),height=1, width=10,bd=4,padx=2)
        self.bupdate.grid(row=0,column=5)

        self.bclose =  Button(operationframe, text="Close",font=("arial",20,"bold"), height=1, width=10,bd=4,padx=2,command=close)
        self.bclose.grid(row=0,column=6)

if __name__ == '__main__':

    root= Tk()
    app = Product(root)
    root.mainloop()


