import requests
import json
import tkinter as tk
from tkinter.messagebox import showerror,showinfo

def send_sms(number,message):
    url="https://www.fast2sms.com/dev/bulk"
    params={
        "authorization":"JGcl2VPCY314r9eQLFvMBzqmptb5gSUNIAKoxaXZshk7EjDd0ORZtahncMqoS8kPJ31LAxX4sbluVN6W",
        "sender_id":"FSTSMS",
        'message':message,
        'language':'english',
        'route':'p',
        'numbers':number
    }
    response=requests.get(url, params=params)
    dic=response.json()
    print(dic)
    return dic.get('return')


# defining fucntions:
def btn_click():
    num=str(entryField1.get())
    msg=str(textbox1.get('1.0',tk.END))
    r=send_sms(num,msg)

    if r:
        showinfo("Send Success","Sending SUCCESSFUL")
    else:
        showerror("FAILED","Something went wrong")



# Creating GUI for the above.
window=tk.Tk()
window.title("Message Sender Automated")
window.geometry("550x400")
``

# label
label1=tk.Label(text="Phone Number",font=["times new roman",15,'bold'])
label1.grid(row=0,column=0)

# entry field
entryField1=tk.Entry()
entryField1.grid(row=0,column=1)

# label1
label3=tk.Label(text="Text message",font=["times new roman",15,'bold'])
label3.grid(row=1,column=0)

# text box
textbox1=tk.Text(master=window,height=5,width=40)
textbox1.grid(row=1,column=1)

# button
sendBtn=tk.Button(window,text="Send SMS", command=btn_click)
sendBtn.grid(row=2,column=1)
# label2
label2=tk.Label(text="Hello And Welcome To Automated Message Sender\n deleveloped by Kshitiz",font=["Blackadder ITC",12,'bold'])
label2.grid(row=22,column=1)

window.mainloop()