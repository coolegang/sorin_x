from tkinter import *
import tkinter.messagebox
import time
from random import randint as rand # dont read this line please
import os
import asyncio
import PySimpleGUI as pb
import psutil
root = Tk()
root.geometry('300x300')

root.title('sorin fat ass scammer X')

textlaunch = Label(text='launcheng..', font='Verdana 20').pack()
credits = Label(text='by Purple.#6663', font='Verdana 15').pack()

pb.one_line_progress_meter('sorin X', 0, 8, 'installing malware to your pc')
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 1, 8, 'stealing your keys from paid hubs..')
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 2, 8, 'preparing to bypass hyperion..')
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 3, 8, 'Injecting Discord') # Spidey
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 4, 8, 'checking for roblox (idc if you dont have it)')
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 5, 8, 'real discord hacking methods…') # added by Spidey btw pls give me robuk
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 6, 8, 'ip logging you')
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 7, 8, 'looking into your cookies') # Spidey
time.sleep(0.1)
pb.one_line_progress_meter('sorin X', 8, 9, 'prob done. launching..')
time.sleep(0.5)
pb.one_line_progress_meter('sorin X', 9, 9, 'BALLS')

injected = False

def execute():
    if injected == True:
        tkinter.messagebox.showinfo('yes', 'your script successfully injected into your roblos game')
    else:
        tkinter.messagebox.showerror('pls inject','you must inject to roblox web before executing your script FE bals xd')

def injection():
    found = False
    global injected
    fps = tkinter.messagebox.askyesno('do u want cool fps unloke?', 'please dont clik this text you will get nothing in result')
    pb.one_line_progress_meter('sorin X', 0, 4, 'checking..')
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "RobloxPlayerBeta.exe":
            found = True
            time.sleep(1.2)
            pb.one_line_progress_meter('sorin X', 1, 4, 'preparing discord methods..')
            time.sleep(0.7)
            pb.one_line_progress_meter('sorin X', 2, 4, 'transfering all your robux to sorins account..')
            time.sleep(0.8)
            pb.one_line_progress_meter('sorin X', 3, 4, 'injecting..')
            time.sleep(1)
            if fps == True:
                pb.one_line_progress_meter('sorin X', 3.5, 4, 'unlocking fps limit..')
                time.sleep(1)
            pb.one_line_progress_meter('sorin X', 4, 4, 'good')
            injected = True
            window.title('sorin fat ass scammer X | injected | bypased')
            tkinter.messagebox.showinfo('sorin X status','injected and bypased hyperion and anticheat. feel free to lego hak now')
            break
    if found == False:
        tkinter.messagebox.showerror('run ur roblox to inject pls','read title of this error and giv me robuk')

def scripts():
    tkinter.messagebox.showinfo('shut up pls', 'im lazy to do this but if yall ask for it so much i will get an idea for it and update it')
    tkinter.messagebox.showwarning('ok so', 'this is not my channel but hey do you want free robuk')
    

def robuk():
    pb.one_line_progress_meter('sorin X', 0, 20, 'preparing..')
    time.sleep(1)
    pb.one_line_progress_meter('sorin X', 1, 20, 'collecting HWID..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 2, 20, 'logging account logged in..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 3, 20, 'false trigging roblox anticheat..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 4, 20, 'calling roblox about your exploiting..')
    time.sleep(1)
    pb.one_line_progress_meter('sorin X', 5, 20, 'locking files..')
    time.sleep(1.7)
    pb.one_line_progress_meter('sorin X', 6, 20, 'saving your ntuser.dat ..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 7, 20, 'sending to roblox all your information..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 8, 20, 'logging all your saved passwords..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 9, 20, 'logging your cookies to sorin..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 10, 20, 'getting you into ban wave..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 11, 20, 'robuk..')
    time.sleep(2)
    pb.one_line_progress_meter('sorin X', 12, 20, 'yes.. robuk..')
    time.sleep(2)
    pb.one_line_progress_meter('sorin X', 13, 20, 'YES.. ROBUK..')
    time.sleep(2)
    pb.one_line_progress_meter('sorin X', 14, 20, 'sharing your robuk to purple..')
    time.sleep(1)
    pb.one_line_progress_meter('sorin X', 15, 20, 'checking..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 16, 20, 'success!')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 17, 20, 'selling your data..')
    time.sleep(1)
    pb.one_line_progress_meter('sorin X', 18, 20, 'checking for limiteds..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 19, 20, 'sharing limiteds to sorin..')
    time.sleep(0.5)
    pb.one_line_progress_meter('sorin X', 20, 21, 'we are done!!1!1 robuk prob generated yw')
    time.sleep(1.5)
    pb.one_line_progress_meter('sorin X', 21, 21, 'we are done!!1!1 robuk prob generated yw')
    time.sleep(1.5)

def paypal_withdraw():
    global usermoney
    if int(usermoney) <= 10:
        tkinter.messagebox.showerror('sorin X', 'get at least 10$ to withdraw pls')
    else:
        pb.one_line_progress_meter('sorin X', 0, 4, 'connecting to paypal..')
        time.sleep(0.5)
        pb.one_line_progress_meter('sorin X', 1, 4, 'sending to you your $$$$$$$')
        time.sleep(1)
        pb.one_line_progress_meter('sorin X', 2, 4, 'verifying..')
        time.sleep(2)
        pb.one_line_progress_meter('sorin X', 3, 4, 'something wrong happened!')
        time.sleep(4)
        pb.one_line_progress_meter('sorin X', 4, 4, '(exit scam)')
        tkinter.messagebox.showwarning('sorin X','something wrong happened while sending your money to you! we actually instantly make action to return money back and they are totally on your balance 100%')
        money = open('notpaypalmoney.txt', 'w')
        money.write('0')
        money.close()

def paypal():
    global usermoney
    pb.one_line_progress_meter('sorin X', 0, 2, 'connecting to your personal paypal account (through logging passwords your browser ofc)..')
    time.sleep(1.5)
    pb.one_line_progress_meter('sorin X', 1, 2, 'preparing..')
    time.sleep(0.8)
    pb.one_line_progress_meter('sorin X', 2, 2, 'done')
    pp = Tk()
    pp.title('sorin fat ass scammer X | paepal account fr')
    pp.geometry('500x300')
    try:
        money = open('notpaypalmoney.txt', 'r')
    except:
        money = open('notpaypalmoney.txt', 'w')
        money.write('0') # YES ITS VERY RUDE
        money.close()
        money = open('notpaypalmoney.txt', 'r')
    usermoney = money.read()
    money.close()
    #ui part

    moneyshow = Label(pp, text='ur wallet is smelling like {}$'.format(usermoney), font='Verdana 14').pack()
    withdraw = Button(pp, text='withdraw', font='Verdana 12', command=paypal_withdraw).pack()


window = Tk()
window.title('sorin fat ass scammer X | waitin for inject')
window.geometry('600x300')
window['bg']='#0c0021'
frame = Frame(window, bg='#0c0021')
frame.pack()
injecti = Button(frame, text='inject lego hak', font='Verdana 12', command=injection, bg='#0c0021', fg='#d6bfff')
injecti.pack(side=LEFT)
execut = Button(frame, text='execut', font='Verdana 12', command=execute, bg='#0c0021', fg='#d6bfff')
execut.pack(side=LEFT)
robux = Button(frame, text='generate robuk', font='Verdana 11', command=robuk, bg='#0c0021', fg='#d6bfff')
robux.pack(side=LEFT)
scripts = Button(frame, text='dark ecentrik scripts', font='Verdana 11', command=scripts, bg='#0c0021', fg='#d6bfff')
scripts.pack(side=LEFT)
paypalb = Button(frame, text='paepal', font='Verdana 11', command=paypal, bg='#0c0021', fg='#d6bfff')
paypalb.pack(side=LEFT)
scripthere = Text(window, width=70, height=50, bg='#0c0021', fg='#d6bfff')
scripthere.pack()
root.destroy()
window.mainloop()

































# to not spoiler functions or something im hiding code on record like this