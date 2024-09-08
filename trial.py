from tkinter import *
import tkinter as tk
import pymysql

def login():
    def authenticate():
        username = entry_username.get()
        password = entry_password.get()

        if username == "maaz12" and password == "ahmed12":
            root.deiconify()  # Show the main menu
            login_window.destroy()  # Close the login window
        else:
            label_message.config(text="Invalid username or password")

    login_window = Tk()  # Use Toplevel for additional windows
    login_window.title("Login")
    login_window.configure(bg="gray")  # Set background color to gray

    window_width = 300
    window_height = 150
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    login_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    label_heading = Label(login_window, text="LOGIN", font=("Arial", 14), bg="gray")  # Add LOGIN heading
    label_heading.place(relx=0.5, rely=0.15, anchor="center")  # Adjust rely for positioning

    label_username = Label(login_window, text="Username:", bg="gray")  # Set background color to gray
    label_username.place(relx=0.5, rely=0.3, anchor="center")  # Adjust rely for positioning

    entry_username = Entry(login_window)
    entry_username.place(relx=0.5, rely=0.37, anchor="center")  # Adjust rely for positioning

    label_password = Label(login_window, text="Password:", bg="gray")  # Set background color to gray
    label_password.place(relx=0.5, rely=0.47, anchor="center")  # Adjust rely for positioning

    entry_password = Entry(login_window, show="*")
    entry_password.place(relx=0.5, rely=0.54, anchor="center")  # Adjust rely for positioning

    button_login = Button(login_window, text="Login", command=authenticate, bg="red")  # Set button color to red
    button_login.place(relx=0.5, rely=0.65, anchor="center")  # Adjust rely for positioning

    label_message = Label(login_window, text="", fg="red", bg="gray")  # Set background color to gray
    label_message.place(relx=0.5, rely=0.75, anchor="center")  # Adjust rely for positioning

# Call the login function
login()

root = Tk()
root.title("Rally Driver Stats")
root.geometry("400x400")
root.config(bg="grey")  # Set background color to grey

def driver():
    master = Tk()
    master.geometry("520x400")
    master.title("Rally Driver Stats")

    textName = StringVar()
    textDob = StringVar()
    textDrivNum = StringVar()
    textDrivId = StringVar()

    # Your existing driver function code here
    
    Label(master, text="Name: ").grid(row=0)
    Label(master, text="Date Of Birth: ").grid(row=1)
    Label(master, text="Phone Number: ").grid(row=2)
    Label(master, text="Driver I.D.: ").grid(row=3)

    Label(master, text="(Example of Name input: Lebron James )").grid(row=15)
    Label(master, text="(Example of Date Of Birth input: 1996-05-05) ").grid(row=16)
    Label(master, text="(Example of Phone Number input: 3012239229) ").grid(row=17)
    Label(master, text="(Example of Driver I.D. input: 1222)").grid(row=18)
    Message(master, text="*** In order to change information as a driver, you must delete your information using your driver I.D. and input new information ***", width = 200).grid(row=19)

    name= Entry(master, text = textName)
    dob= Entry(master,  text = textDob)
    drivNum= Entry(master,  text = textDrivNum)
    drivId = Entry(master,  text = textDrivId)
    
    name.grid(row=0, column=1)
    dob.grid(row=1, column=1)  # Adjusted row for Date Of Birth
    drivNum.grid(row=2, column=1)  # Adjusted row for Phone Number
    drivId.grid(row=3, column=1)


    def done():



        texta = "{}".format(name.get())
        textb = "{}".format(dob.get())
        textc = "{}".format(drivNum.get())
        textd = "{}".format(drivId.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2',
                             autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Driver VALUES""" + str(dataa))
        db.commit()


        cursor.execute("""SELECT * FROM Driver;""")

        print(cursor.fetchall())

        db.close()

        #print('"{}"'.format(name.get()))
       # print(texta)

    def deleteDriver():
        deleteDriv = Tk()
        deleteDriv.geometry("700x220")
        deleteDriv.title("Rally Driver Stats")

        deleteDrivInput = StringVar()

        Label(deleteDriv, text="Driver Number: ").grid(row=0)
        Label(deleteDriv, text="You have to know your Driver Number to delete your driver data").grid(row=1)
        Label(deleteDriv, text="(Example of Driver Number: 1122212232) ").grid(row=2)

        drivDelete = Entry(deleteDriv, text=deleteDrivInput)

        drivDelete.grid(row=0, column=1)


        def delete():
            texta = "{}".format(drivDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2',
                                     autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Driver WHERE drivNum=""" + str(dataa));

            cursor.execute("""SELECT * FROM Driver;""")

            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deleteDriv, text="Done", command=delete, bg="#4CAF50",fg="white").place(x=20, y=150)


    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50",fg="white").place(x=20, y=300)
    Buttong = Button(master, text="Delete Driver", command=deleteDriver, bg="red",fg="white").place(x=20, y=330)

    name.grid(row=0, column=1)
    drivId.grid(row=3, column=1)

def track():
    master = Tk()
    master.geometry("500x250")
    master.title("Rally Driver Stats")

    textTrackNum = StringVar()
    textLapNum = StringVar()

    # Your existing track function code here
    Label(master, text="Track Number: ").grid(row=0)
    Label(master, text="Lap Number: ").grid(row=1)

    Label(master, text="(Example of Track Number input: 12255)").grid(row=15)
    Label(master, text="(Example of Lap Number input: 128) ").grid(row=16)

#Change seat number

    trackNum = Entry(master, text=textTrackNum)
    lapNum = Entry(master, text=textLapNum)






    def done():



        texta = "{}".format(trackNum.get())
        textb = "{}".format(lapNum.get())

        print(texta)

        dataa = (texta, textb)
        print(dataa)


        db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2',
                             autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Track VALUES""" + str(dataa))
        db.commit()


        cursor.execute("""SELECT * FROM Track;""")

        print(cursor.fetchall())

        db.close()

        #print('"{}"'.format(name.get()))
       # print(texta)







    def deleteTrack():


        deleteTrac = Tk()
        deleteTrac.geometry("450x220")
        deleteTrac.title("Rally Driver Stats")

        deleteTracInput = StringVar()

        Label(deleteTrac, text="Track Number: ").grid(row=0)

        Label(deleteTrac, text="Example of Track Number: 12211 ").grid(row=1)

        trackDelete = Entry(deleteTrac, text=deleteTracInput)

        trackDelete.grid(row=0, column=1)

        def delete():


            texta = "{}".format(trackDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2',
                                     autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Track WHERE trackNum="""+str(dataa));



            cursor.execute("""SELECT * FROM Track;""")

            print(cursor.fetchall())

            db.close()


        Buttonf = Button(deleteTrac, text="Done", command=delete, bg="#4CAF50",fg="white").place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50",fg="white").place(x=20, y=150)
    Buttong = Button(master, text="Delete Track", command=deleteTrack, bg="red",fg="white").place(x=20, y=180)

    trackNum.grid(row=0, column=1)
    lapNum.grid(row=1, column=1)

def venue():
    master = Tk()
    master.geometry("500x350")
    master.title("Rally Driver Stats")

    textVenueId = StringVar()
    textVenueName = StringVar()
    textVenueTicket = StringVar()
    textNumVenue = StringVar()

    # Your existing venue function code here
    
    Label(master, text="Venue I.D.: ").grid(row=0)
    Label(master, text="Venue Name: ").grid(row=1)
    Label(master, text="Venue Ticket: ").grid(row=2)
    Label(master, text="Number of Venue: ").grid(row=3)

    Label(master, text="(Example of Venue I.D.: 1221) ").grid(row=15)
    Label(master, text="(Example of Venue Name: A-5) ").grid(row=16)
    Label(master, text="(Example of Venue Ticket: 300)  ").grid(row=17)
    Label(master, text="(Example of Number of Venue: 1) ").grid(row=18)
    Message(master, text="*** In order to change venue information, you must delete it using your venue I.D. number and then insert another one***", width = 200).grid(row=19)


    venueId = Entry(master, text=textVenueId)
    venueName = Entry(master, text=textVenueName)
    venueTicket = Entry(master, text=textVenueTicket)
    numVenue = Entry(master, text=textNumVenue)



    def done():



        texta = "{}".format(venueId.get())
        textb = "{}".format(venueName.get())
        textc = "{}".format(venueTicket.get())
        textd = "{}".format(numVenue.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)
        db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2',
                             autocommit=True)

        cursor = db.cursor()

        '''Mysql for user input'''

        cursor.execute("""INSERT INTO Venue VALUES""" + str(dataa))
        db.commit()


        cursor.execute("""SELECT * FROM Venue;""")

        print(cursor.fetchall())

        db.close()

        #print('"{}"'.format(name.get()))
       # print(texta)

    def deleteVenue():
        deleteVen = Tk()
        deleteVen.geometry("700x220")
        deleteVen.title("Rally Driver Stats")

        deleteVenInput = StringVar()

        Label(deleteVen, text="Driver Number: ").grid(row=0)
        Label(deleteVen, text="You have to know your Venue I.D. to delete your venue data").grid(row=1)
        Label(deleteVen, text="Example of Driver Number: 1122212232 ").grid(row=2)

        venDelete = Entry(deleteVen, text=deleteVenInput)

        venDelete.grid(row=0, column=1)


        def delete():
            texta = "{}".format(venDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

            db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2',
                                     autocommit=True)

            cursor = db.cursor()

            '''Mysql for user input'''

            cursor.execute("""DELETE FROM Venue WHERE venueId=""" + str(dataa));

            cursor.execute("""SELECT * FROM Venue;""")

            print(cursor.fetchall())

            db.close()

        Buttonh = Button(deleteVen, text="Done", command=delete, bg="#4CAF50",fg="white").place(x=20, y=150)

    Buttonf = Button(master, text="Done", command=done, bg="#4CAF50",fg="white").place(x=20, y=280)
    Buttong = Button(master, text="Delete Venue", command=deleteVenue, bg="red",fg="white").place(x=20, y=310)

    venueId.grid(row=0, column=1)
    venueName.grid(row=1, column=1)
    venueTicket.grid(row=2, column=1)
    numVenue.grid(row=3, column=1)

def car():
    master = Tk()
    master.geometry("850x300")
    master.title("Rally Driver Stats")

    textCompany = StringVar()
    textName = StringVar()
    textCarNum = StringVar()
    textSpeedNum = StringVar()
    textCarSize = StringVar()

    # Your existing car function code here
    Label(master, text="Car Company: ").grid(row=0)
    Label(master, text="Car Name: ").grid(row=1)
    Label(master, text="Car Number: ").grid(row=2)
    Label(master, text="Top Speed: ").grid(row=3)
    Label(master, text="Car Size: ").grid(row=4)

    Label(master, text="(Example of Company : Mercedes (Insert time based on 24 hour clock)) ").grid(row=15)
    Label(master, text="(Example of Car Name: Mayback (Insert time based on 24 hour clock)) ").grid(row=16)
    Label(master, text="(Example of Car Number: 29) ").grid(row=17)
    Label(master, text="(Example of Number of Seats: 2) ").grid(row=18)
    Label(master, text="(Example of Car Size: Small,Medium, or Large) ").grid(row=19)
    Label(master, text="For reference on Car Size, Small(150 feet long), Medium(200 feet long), Large(250 feet long)").grid(row=20)

    company= Entry(master, text=textCompany)
    name= Entry(master,  text=textName)
    carNum= Entry(master,  text=textCarNum)
    speedNum = Entry(master,  text=textSpeedNum)
    carSize = Entry(master, text=textCarSize)

    def done():
        texta = "{}".format(company.get())
        textb = "{}".format(name.get())
        textc = "{}".format(carNum.get())
        textd = "{}".format(speedNum.get())
        texte = "{}".format(carSize.get())

        dataa = (texta, textb, textc, textd, texte)

        db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2', autocommit=True)
        cursor = db.cursor()

        cursor.execute("""INSERT INTO Car VALUES""" + str(dataa))
        db.commit()

        cursor.execute("""SELECT * FROM Car;""")
        print(cursor.fetchall())

        db.close()

    def deleteCar():
        deleteCarWindow = Tk()
        deleteCarWindow.geometry("450x220")
        deleteCarWindow.title("Delete Car")

        deleteCarInput = StringVar()

        Label(deleteCarWindow, text="Car Number: ").grid(row=0)
        Label(deleteCarWindow, text="Example of Car Number: 29 ").grid(row=1)

        carDeleteEntry = Entry(deleteCarWindow, text=deleteCarInput)
        carDeleteEntry.grid(row=0, column=1)

        def delete():
            carNumber = carDeleteEntry.get()
            db = pymysql.connect(host='localhost', user='root', passwd='Ahmed@123', db='cars2', autocommit=True)
            cursor = db.cursor()

            cursor.execute("""DELETE FROM Car WHERE carNum={}""".format(carNumber))
            cursor.execute("""SELECT * FROM Car;""")
            print(cursor.fetchall())

            db.close()

        Button(deleteCarWindow, text="Delete", command=delete).grid(row=2, column=0)

    Button(master, text="Done", command=done, bg="#4CAF50", fg="white").place(x=20, y=270)
    Button(master, text="Delete Car", command=deleteCar, bg="red", fg="white").place(x=120, y=270)

    company.grid(row=0, column=1)
    name.grid(row=1, column=1)
    carNum.grid(row=2, column=1)
    speedNum.grid(row=3, column=1)
    carSize.grid(row=4, column=1)

    

"mainloop():this is the main menu"
label = Label(root, text="WELCOME TO RALLY DRIVER STATS", font=("Arial", 20, "bold"), fg="white", bg="black")
label.pack(pady=20)

myButtonb = Button(root, text="Venue", command=venue, font=("Arial", 14), fg="#FFFFFF", bg="#0052CC", activeforeground="#FFFFFF", activebackground="#003399")
myButtonb.pack(pady=10)

myButtonc = Button(root, text="Track", command=track, font=("Arial", 14), fg="#FFFFFF", bg="#009933", activeforeground="#FFFFFF", activebackground="#006600")
myButtonc.pack(pady=10)

myButtond = Button(root, text="Car", command=car, font=("Arial", 14), fg="#FFFFFF", bg="#CC0000", activeforeground="#FFFFFF", activebackground="#990000")
myButtond.pack(pady=10)

myButtone = Button(root, text="Driver", command=driver, font=("Arial", 14), fg="#FFFFFF", bg="#CC3300", activeforeground="#FFFFFF", activebackground="#993300")
myButtone.pack(pady=10)

# Hide the main menu initially
root.withdraw()

# Show the login page
login()

root.mainloop() 

