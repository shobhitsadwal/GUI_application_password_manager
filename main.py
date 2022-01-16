from tkinter import *
import random
compact=None
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nums=[1,2,3,4,5,6,7,8,9,10]

speci=["(]p)","*des","#Wgfd","!#$%^WEWE"]

# a=random.choice(alp)
# b=random.choice(nums)
# c=random.choice(speci)
#
# compact=f"{a}{b}{c}"

#........................PASSWORD FUNCTION .............................#

def password_gen():
    global compact
    a = random.choice(alp)
    b = random.choice(nums)
    c = random.choice(speci)

    compact = f"{a}{b}{c}"
    inp_passwd.insert(0,compact)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def getter():
    # global website
    # global email
    website=inp_website.get()
    email=inp_email.get()
    passwd=inp_passwd.get()

    if len(website)==0 or len(passwd)==0:
        messagebox.showinfo(title="error",message="you cannot leave password or website  fields empty,do you wish to continue?")
    else:

        mer=messagebox.askokcancel(title=website,message="this is the final message , do you wish to continue",)

        if mer:

            with open("passwordmanager.txt","a") as pw:
                pw.write(f"\n website={website},email={email},passwd={passwd} \n")

                inp_website.delete(0,END)
                inp_passwd.delete(0,END)





# ---------------------------- UI SETUP ------------------------------- #



windows=Tk()

windows.title("password generator")
windows.wm_minsize(width=400,height=470)
windows.config(padx=60,pady=100)
image1=PhotoImage(file="logo.png")
windows.configure(bg="pink")


label0=Label(text="program by shobhit sadwal ,coprights reserved",font=("Arial",6,"italic"),bg="pink")
label0.grid(column=0,row=1)


canvas = Canvas(bg="pink",highlightthickness=0)
canvas.create_image(200,180,image=image1)
canvas.grid(column=1,row=2)

label=Label(text="website: ",font=("Arial",12,"bold"),bg="pink")
label.grid(column=0,row=4)

label_emp=Label(text='',bg="pink")
label_emp.grid(column=0,row=3)

inp_website=Entry(width=35)
inp_website.focus()
# website=inp_website.get()
inp_website.grid(columns=1,row=4,columnspan=2)

label_email=Label(text="Email/Username: ",font=("Arial",12,"bold"),bg="pink")
label_email.grid(column=0,row=5)

inp_email=Entry(width=35)
inp_email.insert(0,"shobhit@gmail.com")
# email=inp_email.get()
inp_email.grid(column=0,row=5,columnspan=2)

label_passwd=Label(text="PASSWORD** ",font=("Arial",13,"bold"),bg="pink")
label_passwd.grid(column=0,row=6)

inp_passwd=Entry(width=31)
inp_passwd.grid(column=0,row=6,columnspan=2)

pas_button=Button(width=16,text="generate password",command=password_gen)
pas_button.grid(column=2,row=6)


add_button=Button(width=36,text="ADD",command=getter)
add_button.grid(column=1,row=7)

info_label=Label(text="(click to add the password in the  user file) ",font=("Arial",10,"italic"),bg="pink")
info_label.grid(column=1,row=8)


print(inp_passwd.get())
print(inp_email.get())




windows.mainloop()