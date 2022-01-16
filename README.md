# GUI_application_password_manager
A GUI desktop application made entirely by using the TKINTER module and python for generating new passwords and username for saving the time to create new passwords during work .

# This is the Desktop application of the password manager that I made using Tkinter library . 

![manager](https://pbs.twimg.com/media/Ey90b8pW8AE7S54?format=jpg&name=medium)

## Prompt windows after generating the new password inside the desktop
![prompt](https://pbs.twimg.com/media/Ey90b8rXIAEEYdT?format=png&name=small)

## Generating of the password and the username in the python console 
![stero](https://pbs.twimg.com/media/Ey90b9PWQAMJtLs?format=png&name=900x900)

# Aim and Objective 
 To make a desktop application that helps in generating passwords as it has been seen by a research that a lot of productivity and time is wasted on trying new passwords and usernames .
 Here is the article https://owmobility.com/press-releases/research-shows-wasting-16-billion-hours-year-hunting-passwords/
 
# Requirements 
  - python 
  - Tkinter 
  - date-time 
  - random module 
  
# important files to refer
  - ```main.py/``` for the whole code flow
  - ```passwordmanager.txt/``` for the passwords and username containing files 
  
# steps 

 - importing all the necessary libraries including ```random``` and ```from Tkinter import *```
 - making a getter function to get all the ```random.choice()```` for lists containnig metadata
 - creating objects from the tkinter module 
 - making a default image referral for the desktop application 
 - creating a canvas and pushing buttons , labels and enteries inside the canvas
 - creating warnings for the application
 - creating a ```windows.mainloop()``` for the desktop environment
 
 
# some code snippets

  ```python
  def password_gen():
      global compact
      a = random.choice(alp)
      b = random.choice(nums)
      c = random.choice(speci)

      compact = f"{a}{b}{c}"
      inp_passwd.insert(0,compact)
      
      
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

```

## Future uses and scalablity

- making a web page and integrating the program inside it 
- randomly generating million of passwords and storing it inside the database by key value errors 
- integrating this project with flask forms and machine learning model to identify the pattern of **Mersenn-Twister algorithm**
      
      
      

 




 
  
 
 
