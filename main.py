# ATM Management System

# Modules to be imported
import mysql.connector as myc
from tkinter import *
from tkinter import messagebox as msg



# creating list of valid pins
con = myc.connect(user = "root", passwd = "root", host = "localhost", db = "atm")
cur = con.cursor()
l = []
cur.execute("select pin from details")
xaoisj = cur.fetchall()

for i in xaoisj:
    l.append(str(i[0]))

# accessing database
con = myc.connect(user = "root", passwd = "root", host = "localhost", db = "atm")
# print(con)
cur = con.cursor()

def balinq():

    # sc3 = Toplevel(sc1)
    # sc3.geometry("300x300")
    # sc3.title("Balance Inquiry")
    con = myc.connect(user = "root", passwd = "root", host = "localhost", db = "atm")
    # print(con)
    cur = con.cursor()
    cur.execute(f"select balance from details where pin = {pinval.get()}")
    x = cur.fetchall()
    msg.showinfo("Balance Inquiry", f"Current Balance : $ {x}")

    con.close()

    # printing the current balance
    # !!!! to be replaced by the input on screen !!!!

    # for i in cur:
    #     print(i)

def dep():

    sc4  = Toplevel(sc1)
    sc4.geometry("200x200")
    sc4.title("Cash Deposit")

    def deposit():
        con = myc.connect(user = "root", passwd = "root", host = "localhost", db = "atm")
        cur = con.cursor()

        cur.execute(f"Update details set balance = balance + {abs(int(mE.get()))} where pin = {pinval.get()}")

        con.commit()
        con.close()
        msg.showinfo("Status", "Balance Deposited!")
        sc4.destroy()

    xy = Label(sc4, text = "Enter the amount: ")
    xy.grid(row = 0, column = 2)

    global mE

    money = StringVar()
    mE = Entry(sc4, textvariable = money)
    mE.grid(row = 0, column=5)

    btn = Button(sc4, text = "Submit", command = deposit)
    btn.grid(row = 4, column=2)

def wth():

    sc5  = Toplevel(sc1)
    sc5.geometry("200x200")
    sc5.title("Cash Withdrawal")

    def withdrawal():
        con = myc.connect(user = "root", passwd = "root", host = "localhost", db = "atm")
        cur = con.cursor()

        cur.execute(f"Update details set balance = balance - {abs(int(wE.get()))} where pin = {pinval.get()}")

        con.commit()
        con.close()
        msg.showinfo("Status", "Transaction Successfull")
        sc5.destroy()

    xy = Label(sc5, text = "Enter the amount: ")
    xy.grid(row = 0, column = 2)

    global wE

    money = StringVar()
    wE = Entry(sc5, textvariable = money)
    wE.grid(row = 0, column=5)

    btn = Button(sc5, text = "Submit", command = withdrawal)
    btn.grid(row = 4, column=2)

def chp():
    
    global sc2

    sc2 = Toplevel(sc1)
    sc2.geometry("450x300")
    sc2.title("Change Pin!")

    def chapin():
        con = myc.connect(user = "root", passwd = "root", host = "localhost", db = "atm")
        cur = con.cursor()

        cur.execute(f"Update details set pin = {np.get()} where pin = {pinval.get()}")
        con.commit()

        con.close()
        msg.showinfo("Pin Changed", "Pin changed successfully")
        sc2.destroy()

    old = Label(sc2, text = "Old Pin: ")
    old.grid(row = 0, column = 0)

    new = Label(sc2, text = "New Pin: ")
    new.grid(row = 1, column = 0)

    re = Label(sc2, text = "Re-Enter Pin: ")
    re.grid(row = 2, column = 0)

    oldPin = StringVar()
    newPin = StringVar()
    rePin = StringVar()
    
    global np

    op = Entry(sc2, textvariable=oldPin)
    op.grid(row = 0, column = 3)

    np = Entry(sc2, textvariable=newPin)
    np.grid(row = 1, column = 3)

    rp = Entry(sc2, textvariable=rePin)
    rp.grid(row = 2, column = 3)

    change = Button(sc2, text = "Submit", command = chapin)
    change.grid(row = 5, column = 3)


# Post Login Screen
def screen():

    global sc1

    sc1 = Toplevel(sc)
    sc1.geometry("600x450")
    sc1.title("Main Screen!")



    bal = Button(sc1, text = "Balance Inquiry", command = balinq, width = 20)
    bal.grid(row = 0, column = 0)

    depo = Button(sc1, text = "Deposit", command = dep, width = 20)
    depo.grid(row = 0, column = 3)

    wthdrw = Button(sc1, text = "Withdrawal", command = wth, width = 20)
    wthdrw.grid(row = 1, column = 0)

    chap = Button(sc1, text = "Change Pin", command = chp, width = 20)
    chap.grid(row = 1, column = 3)



# Login

def Login():

    global sc

    sc = Tk()
    sc.geometry("900x850")
    sc.title("ATM MANAGEMENT SYSTEM")
    # sc.configure(bg = "cyan")

    def submit():
        
        # check if pin matches any data
        if pinval.get() not in l:
            msg.showerror("Wrong Pin!", "You entered a wrong pin!")
        
        else:
            screen()

    pL = Label(sc, text = "Enter 4-digit Pin: ")
    pL.grid(row = 0, column = 0)

    # pin = IntVar()

    global pinval
    pin = StringVar()
    pinval = Entry(sc, textvariable = pin)
    pinval.grid(row = 0, column =  2)

    sB = Button(sc, text = "Submit", command = submit)
    sB.grid(row = 5, column = 5)


    sc.mainloop()

Login()
