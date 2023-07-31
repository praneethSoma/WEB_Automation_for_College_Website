from EVS import *
from MECH import *
from MATH import *
from PHY import *
from PCPS import *
from EE import *
from links import *

from tkinter import *
def Print():
    #print('As of now this is still under construction')
    dis_pop = Tk(className = 'Apologies')
    dis_pop.iconbitmap('C:/Users/suraj/Desktop/PCPS Project/Final/icon.ico')
    Dis_play=Label(dis_pop, text='As of now this is still under construction', bg='grey', fg='Red',width=30, height=15,font=("Arial", 20)).pack()
    E_it = Button(dis_pop, text='OK' , command=dis_pop.destroy, font=('Arial', 13)).pack()
    dis_pop.mainloop()
def Print1():
    #print('As of now this is still under construction')
    dis_pop = Tk(className = 'About')
    dis_pop.iconbitmap('C:/Users/suraj/Desktop/PCPS Project/Final/icon.ico')
    Dis_play=Label(dis_pop, text='"text this is here bruh', bg='grey', fg='Red',width=30, height=15,font=("Arial", 20)).pack()
    E_it = Button(dis_pop, text='OK' , command=dis_pop.destroy, font=('Arial', 13),fg='Red').pack()
    dis_pop.mainloop()
def b_lank(x,y,*z):
    temp=Label(Input, text=z).grid(row=x,column=y)
def store(x):
    result = x.get()
    return str(result)
def getsub():
    global s_a
    s_a = str(store(sub))
    #print(s_a,type(s_a))
def sub_ass(): #assign of the subject
    getsub()
    global subject
    if s_a == subjects[0]:
        #from EVS import *  
        subject = EVS
    elif s_a == subjects[1]:
        #from PCPS import *
        subject = PCPS
    elif s_a == subjects[2]:
        #from EE import *
        subject = EE
    elif s_a == subjects[3]:
        #from MATH import *
        subject = MATH
    elif s_a == subjects[4]:
        #from MECH import *
        subject = MECH
    elif s_a == subjects[5]:
        #from PHY import *
        subject = PHY
    #print(subject)
    next1()
def windup():
    Input.destroy
    project.destroy
    
def next1(): #used for unit
    Uni_title = Label(Input,text='Unit:-',font=('Arial', 12)).place(x=50,y=70)#.grid(row=3,column=1)
    global uni  
    uni = StringVar(Input)
    unit=subject.keys()
    unit_a=[i for i in unit]

    uni.set(unit_a[0])
    s_m = OptionMenu(Input,uni, *unit_a).place(x=230,y=70)#.grid(row=3,column=2)
    next1 = Button(Input,text='next',command=next2 ,font=('Arial', 11), padx= 6).place(x=520,y=70)#.grid(row=3,column=3)
def next2(): #used for chapter
    global s_u
    s_u = str(store(uni))
    #print(s_u,type(s_u))
    ch_title = Label(Input,text='Chapter:-',font=('Arial', 12)).place(x=50,y=100)#.grid(row=4,column=1)
    global ch
    ch = StringVar(Input)
    chapter = subject[s_u].keys()
    #print(chapter)
    chapter_a = [i for i in chapter]
    #global ch
    ch.set(chapter_a[0])
    s_m = OptionMenu(Input,ch, *chapter_a).place(x=230,y=100)#.grid(row=4,column=2)
    next2 = Button(Input,text='next',command=next3,font=('Arial', 11) , padx= 6).place(x=520,y=100)#.grid(row=4,column=3)
def next3(): #used for resource
    global s_c
    global ch
    s_c = str(store(ch))
    #print(s_c,type(s_c))
    r_sou_title = Label(Input,text='Resource:-',font=('Arial', 12)).place(x=50,y=130)#.grid(row=5,column=1)
    global rc
    rc = StringVar(Input)
    rsou = subject[s_u][s_c].keys() #unwanted
    #print(chapter)
    r_sou = [i for i in rsou]
    try:
        r_sou.remove('MCQ')
        r_sou.remove('Reference')
    except:
        try:
            r_sou.remove('MCQ')
            r_sou.remove('Reference')
        except:
            pass
    #   global ch
    rc.set(r_sou[0])
    s_m = OptionMenu(Input,rc, *r_sou).place(x=230,y=130)#.grid(row=5,column=2)
    next3 = Button(Input,text='Submit',command=next4 , font=('Arial', 13), padx= 10, pady= 6).place(x=320,y=170)#.grid(row=5,column=3)
def next4(): #get the final link (xpath)
    global s_sou
    s_sou = str(store(rc))
    #print(s_sou,type(s_sou))
    global final_link
    final_link = subject[s_u][s_c][s_sou]
    #print(final_link,type(final_link))
    
    sendval_link() #this function will send all the values required into a new file for retrival
        
    #calling for the final Go
    #windup()
    
    import Project
    
def sendval_link():
    global s_a
    global s_u
    #global r_sou
    global final_link
    f=open('temp.py','a')
    f.write('s_a='+'\''+str(s_a)+'\''+'\n')
    f.write('s_u='+'\''+str(s_u)+'\''+'\n')
    #f.write('s_sou='+s_sou+'\n')
    f.write('final_link='+'\''+str(final_link)+'\''+'\n')
    f.close()
#Menu options(unwanted)
    
Input = Tk(className='User Input')
Input.iconbitmap('C:/Users/suraj/Desktop/PCPS Project/Final/icon.ico')
Input.geometry("800x500")
'''
bg3 = PhotoImage(file="C:\\Users\\suraj\\Desktop\\PCPS Project\\Final\\BG(1).png")
ji = Label(Input,image = bg3)
ji.place(x=20,y=200)
'''
menu = Menu(Input) 
Input.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New' , command=Print) 
filemenu.add_command(label='Open', command=Print) 
filemenu.add_separator()
filemenu.add_command(label='Exit', command=Input.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About', command=Print1)

#code starts from here

#b_lank(1,1)
subjects=[
'Environmental Studies and Life Sciences',
'Python for Computational Problem Solving',
'Elements of Electrical Engineering',
'Engineering Mathematics - I',
'Mechanical Engineering Sciences',
'Engineering Physics'
]
sub_title = Label(Input,text='Choose your subject:-',font=('Arial', 12)).place(x=50,y=40)#.grid(row=2,column=1)
sub = StringVar(Input)
sub.set(subjects[0])
s_m = OptionMenu(Input,sub, *subjects).place(x=230,y=40)#.grid(row=2,column=2)
#s_a = store(sub)

submit1 = Button(Input,text='next',command=sub_ass ,font=('Arial', 11), padx= 6).place(x=520,y=40)#.grid(row=2,column=3)

'''  
if s_a == subjects[0]:
    from EVS import *   
    subject = EVS
elif s_a == subjects[1]:
    from PCPS import *
    subject = PCPS
elif s_a == subjects[2]:
    from EE import *
    subject = EE
elif s_a == subjects[3]:
    from MATH import *
    subject = MATH
elif s_a == subjects[4]:
    from MECH import *
    subject = MECH
elif s_a == subjects[5]:
    from PHY import *
    subject = PHY
elif s_a == subjects[6]:
    from PHL import *
    subject = PHL
'''
#submit1 = Button(Input,text='next1>',command=getsub , padx= 10, padx= 6).grid(row=2,column=3)

#chapter starts from here

#line 33 not able to retrive proper chapter names
#it can be solved by taking the input when clicked to next 
#line 28 is causing the error it takes the input before clciking on next which should be avaoided 
## make line 28 exicute when the next button is clciked so that proper input can be taken from the user

#first gui login is to beexicuted the the GUI should be exicuted which takes input and later exicutes the project file to start automation
# we need to add the scroll feature inorder to access the links which are not vissible





