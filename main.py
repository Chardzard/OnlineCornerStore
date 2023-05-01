from Listings_Super_Class import Listings
# from Purchasing_Sub_Class import Purchasing
# from Shipping_Info_Sub_Class import Shipping_Info
from datetime import date
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk


def clicked():
    this_root = tk.Toplevel()
    gang = Listings()
    this_root.title("Shop Now   ")
    this_root.geometry("2115x1155")
    name_list = ["/home/sudojudowarrior/Pictures/lotto.png", "/home/sudojudowarrior/Pictures/big40oz.png",
                 "/home/sudojudowarrior/Pictures/backwoods.png", "/home/sudojudowarrior/Pictures/pothead_emoji.png"]
    lbl = Label(this_root, text="Shop With Us!", fg='yellow', bg='black', font=("Times New Roman", 50))
    lbl.place(x=715, y=20)
    i = 0
    for execute in name_list:
        myImg = ImageTk.PhotoImage(file=execute)
        lbl2 = Label(this_root, image=myImg)
        if i == 0:
            lbl2.place(x=20, y=105)
        elif i == 1:
            lbl2.place(x=1290, y=175)
        elif i == 2:
            lbl2.place(x=700, y=300)
        elif i == 3:
            lbl2.place(x=850, y=100)
        lbl2.image = myImg
        i += 1
    button1 = Button(this_root, text="Click to Purchase", fg='black', bg='yellow', command=create_table)
    button1.place(x=205, y=725)
    button2 = Button(this_root, text="Click to Purchase", fg='black', bg='yellow', command=create_table)
    button2.place(x=860, y=725)
    button3 = Button(this_root, text="Click to Purchase", fg='black', bg='yellow', command=create_table)
    button3.place(x=1500, y=725)
    quantity_label1 = Label(this_root, text="Quantity")
    quantity_combo1 = ttk.Combobox(this_root, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', 'MAX'])
    quantity_label1.place(x=125, y=760)
    quantity_combo1.place(x=190, y=760)
    quantity_label2 = Label(this_root, text="Quantity")
    quantity_combo2 = ttk.Combobox(this_root, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', 'MAX'])
    quantity_label2.place(x=780, y=760)
    quantity_combo2.place(x=845, y=760)
    quantity_label3 = Label(this_root, text="Quantity")
    quantity_combo3 = ttk.Combobox(this_root, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', 'MAX'])
    quantity_label3.place(x=1420, y=760)
    quantity_combo3.place(x=1485, y=760)
    gang.set_product_name("Lottery Ticket")
    gang.set_product_num()
    gang.set_product_price(10)
    gang.set_sold_by("quik_stop_hooker")
    lbl3 = Label(this_root, text=gang.get_product_name, fg='yellow', bg='black', font=("Times New Roman", 20))
    lbl3.place(x=192.5, y=800)
    lbl4 = Label(this_root, text="Listing ID: " + str(gang.get_product_num), fg='yellow', bg='black',
                 font=("Times New Roman", 20))
    lbl4.place(x=180, y=900)
    lbl5 = Label(this_root, text="Price: " + str(gang.get_product_price) + "$", fg='yellow', bg='black',
                 font=("Times New Roman", 20))
    lbl5.place(x=210, y=850)
    lbl6 = Label(this_root, text="Sold By: " + gang.get_sold_by, fg='yellow', bg='black', font=("Times New Roman", 20))
    lbl6.place(x=115, y=950)
    gang.set_product_name("Backwoods 5 Pack Cigars")
    gang.set_product_num()
    gang.set_product_price(25)
    gang.set_sold_by("big_doinks_out_in_Amish")
    lbl7 = Label(this_root, text=gang.get_product_name, fg='yellow', bg='black', font=("Times New Roman", 20))
    lbl7.place(x=795, y=800)
    lbl8 = Label(this_root, text="Listing ID: " + str(gang.get_product_num), fg='yellow', bg='black',
                 font=("Times New Roman", 20))
    lbl8.place(x=845, y=900)
    lbl9 = Label(this_root, text="Price: " + str(gang.get_product_price) + "$", fg='yellow', bg='black',
                 font=("Times New Roman", 20))
    lbl9.place(x=875, y=850)
    lbl10 = Label(this_root, text="Sold By: " + gang.get_sold_by, fg='yellow', bg='black', font=("Times New Roman", 20))
    lbl10.place(x=750, y=950)
    gang.set_product_name("40 Oz. Malt Liquor")
    gang.set_product_num()
    gang.set_product_price(5)
    gang.set_sold_by("40_king_bob")
    lbl11 = Label(this_root, text=gang.get_product_name, fg='yellow', bg='black', font=("Times New Roman", 20))
    lbl11.place(x=1470, y=800)
    lbl12 = Label(this_root, text="Listing ID: " + str(gang.get_product_num), fg='yellow', bg='black',
                  font=("Times New Roman", 20))
    lbl12.place(x=1485, y=900)
    lbl13 = Label(this_root, text="Price: " + str(gang.get_product_price) + "$", fg='yellow', bg='black',
                  font=("Times New Roman", 20))
    lbl13.place(x=1520, y=850)
    lbl14 = Label(this_root, text="Sold By: " + gang.get_sold_by, fg='yellow', bg='black', font=("Times New Roman", 20))
    lbl14.place(x=1452.5, y=950)
    this_root.mainloop()


def create_table():
    db = sqlite3.connect("shipping_info.db")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS shipping_info")
    query1 = "CREATE TABLE shipping_info(" \
             + "first_name TEXT," \
             + "last_name TEXT," \
             + "phone TEXT," \
             + "email TEXT," \
             + "address TEXT," \
             + "PRIMARY KEY ('first_name')" \
             + ")"
    cursor.execute(query1)
    db.commit()

    def add_data():
        cursor.execute('INSERT INTO shipping_info (first_name, last_name, phone, email, address) VALUES '
                       '(?, ?, ?, ?, ?)', (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(),))
        db.commit()
        db.close()
        last_root = tk.Toplevel()
        last_root.title("Order Confirmation     ")
        last_root.geometry("2115x1155")
        this_pics = ["/home/sudojudowarrior/Pictures/anon2.png", "/home/sudojudowarrior/Pictures/awesome.png",
                     "/home/sudojudowarrior/Pictures/final_pic.png"]
        j = 0
        for pic in this_pics:
            Img = ImageTk.PhotoImage(file=pic)
            last_label = Label(last_root, image=Img)
            if j == 0:
                last_label.place(x=10, y=10)
            elif j == 1:
                last_label.place(x=1075, y=325)
            elif j == 2:
                last_label.place(x=825, y=775)
            last_label.image = Img
            j += 1
        final = Label(last_root, text="Thank you for your order on\n" + str(date.today()) +
                                      "! Your items will be\n" +
                                      "shipped to the address we have \non file as soon as possible. Enjoy!",
                      fg='yellow', bg='black', font=("Arial", 45))
        final.place(x=920, y=10)
        last_button = Button(last_root, text="Exit", fg='black', bg='yellow', height=2, width=20,
                             command=final_gang)
        last_button.place(x=1290, y=900)
        last_root.mainloop()

    def final_gang():
        quit()

    this_root = tk.Toplevel()
    this_root.title("Check Out       ")
    this_root.geometry("2115x1155")
    pics = ["/home/sudojudowarrior/Pictures/Mikasa.png", "/home/sudojudowarrior/Pictures/secure-checkout.png",
            "/home/sudojudowarrior/Pictures/morty.png", "/home/sudojudowarrior/Pictures/sexy-icon.png",
            "/home/sudojudowarrior/Pictures/rick&Morty replacement.png", "/home/sudojudowarrior/Pictures/ribbon.png",
            "/home/sudojudowarrior/Pictures/ribbon.png", "/home/sudojudowarrior/Pictures/ribbon.png",
            "/home/sudojudowarrior/Pictures/line.png"]
    i = 0
    for execute in pics:
        myImg = ImageTk.PhotoImage(file=execute)
        lbl = Label(this_root, image=myImg)
        if i == 0:
            lbl.place(x=960, y=5)
        elif i == 1:
            lbl.place(x=20, y=20)
        elif i == 2:
            lbl.place(x=-15, y=500)
        elif i == 3:
            lbl.place(x=500, y=50)
        elif i == 4:
            lbl.place(x=1275, y=560)
        elif i == 5:
            lbl.place(x=350, y=300)
        elif i == 6:
            lbl.place(x=650, y=500)
        elif i == 7:
            lbl.place(x=950, y=700)
        elif i == 8:
            lbl.place(x=500, y=875)
        lbl.image = myImg
        i += 1
    lbl1 = Label(this_root, text="Deliver To", fg='yellow', bg='black', font=("Times New Roman", 40))
    lbl1.place(x=800, y=25)
    lbl2 = Label(this_root, text="First Name", font=("Times New Roman", 13))
    lbl2.place(x=750, y=125)
    lbl3 = Label(this_root, text="Last Name", font=("Times New Roman", 13))
    lbl3.place(x=750, y=150)
    lbl4 = Label(this_root, text="Phone", font=("Times New Roman", 13))
    lbl4.place(x=765, y=175)
    lbl5 = Label(this_root, text="Email", font=("Times New Roman", 13))
    lbl5.place(x=765, y=200)
    lbl6 = Label(this_root, text="Address", font=("Times New Roman", 13))
    lbl6.place(x=762.5, y=225)
    e1 = Entry(this_root)
    e1.place(x=840, y=125)
    e1.focus_set()
    e2 = Entry(this_root)
    e2.place(x=840, y=150)
    e3 = Entry(this_root)
    e3.place(x=840, y=175)
    e4 = Entry(this_root, width=27)
    e4.place(x=840, y=200)
    e5 = Entry(this_root, width=27)
    e5.place(x=840, y=225)
    b2 = Button(this_root, text="Finish", fg='black', bg='yellow', command=add_data)
    b2.place(x=885, y=250)


def covid_button():
    this_root = tk.Toplevel()
    this_root.title("COVID-19                   ")
    this_root.geometry("2115x1155")
    canvas = Canvas(this_root, width=50, height=50)
    canvas.pack(expand=YES, fill=BOTH)
    img = PhotoImage(file="/home/sudojudowarrior/Pictures/quikstop.png")
    canvas.create_image(630, 605, image=img, anchor=NW)
    canvas.img = img
    lbl = Label(this_root,
                text="We have carried out a COVID-19 risk assessment and "
                     "shared the results with the people who work here\n\n-We have cleaning, hand washing and hygiene "
                     "procedures in line with guidance\n\n-We have taken all reasonable steps to help people work from"
                     " home\n\n-We have taken all reasonable steps to maintain a 2m distance in the workplace\n\n"
                     "-Where people cannot be 2m apart, we have done everything practical to manage transmission risk",
                fg='yellow', bg='black', font=("Times New Roman", 30))
    lbl.place(x=90, y=175)
    lbl2 = Label(this_root, text="COVID-19 Policy", fg='white', bg='black', font=("Arial", 40))
    lbl2.place(x=670, y=50)
    button = Button(this_root, text="Exit", fg='black', bg='yellow', command=this_root.destroy, width=25)
    button.place(x=757.5, y=125)


def main():
    root = tk.Tk()
    root.title("QuikStop Online Store                 ")
    root.geometry("2115x1155")
    pics = ["/home/sudojudowarrior/Pictures/quikstop.png", "/home/sudojudowarrior/Pictures/squiggly.png",
            "/home/sudojudowarrior/Pictures/squiggly.png"]
    i = 0
    for execute in pics:
        myImg = ImageTk.PhotoImage(file=execute)
        lbl = Label(root, image=myImg)
        if i == 0:
            lbl.place(x=620, y=225)
        elif i == 1:
            lbl.place(x=17.50, y=150)
        elif i == 2:
            lbl.place(x=1525, y=150)
        lbl.image = myImg
        i += 1
    frame1 = Frame(root, bg='white')
    frame1.place(relwidth=0.75, relheight=0.75, relx=0.125, rely=0.125)
    frame1.pack()
    lbl1 = Label(root, text="Shop Low Prices Today!", fg='blue', bg='red', font=("Times New Roman", 36))
    lbl1.place(x=647.50, y=100)
    lbl2 = Label(root, text="Click below for all COVID-19 updates", fg='white', bg='black', font=("Arial", 30))
    lbl2.place(x=550, y=810)
    button1 = Button(root, text="Click here to browse listings", fg='black', bg='yellow', command=clicked, width=25)
    button1.place(x=773.5, y=175)
    button2 = Button(root, text="COVID-19 Update", fg='black', bg='yellow', command=covid_button, width=25)
    button2.place(x=763.5, y=880)
    root.mainloop()


if __name__ == "__main__":
    main()
