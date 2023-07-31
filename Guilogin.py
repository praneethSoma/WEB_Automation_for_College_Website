#count=0 future interpretation link line 23
from tkinter import *
def Print():
    #print('As of now this is still under construction')
    dis_pop = Tk(className = 'Apologies')
    dis_pop.iconbitmap('C:/Users/suraj/Desktop/PCPS Project/Final/icon.ico')
    Dis_play=Label(dis_pop, text='As of now this is still under construction \n Kindly Co-operate', bg='grey', fg='Red',width=30, height=15,font=("Arial", 20)).pack()
    
    E_it = Button(dis_pop, text='OK' , command=dis_pop.destroy, font=('Arial', 13)).pack()
    dis_pop.mainloop()
def Print1():
    #print('As of now this is still under construction')
    dis_pop = Tk(className = 'About')
    dis_pop.iconbitmap('C:/Users/suraj/Desktop/PCPS Project/Final/icon.ico')
    Dis_play=Label(dis_pop, text='All the rights are reserved by \n The creaters of the application \n copying any of the resources \n will lead to law enforcements \n\n Legal actions will \n be taken against \n such people', bg='grey', fg='Red',width=30, height=15,font=("Arial", 20)).pack()
    
    E_it = Button(dis_pop, text='OK' , command=dis_pop.destroy, font=('Arial', 13),fg='Red').pack()
    dis_pop.mainloop()
def submision():
    global user_name
    user_name=user_n.get() #the username from user
    #print(user_name)
    global user_pass
    user_pass=user_p.get() #the password from user
    
    sendval_login()#used to send values to a different file
    #count+=1 future interpretation
    import Gui
def b_lank(x,y,*z):
    temp=Label(project, text=z).grid(row=x,column=y)
def sendval_login():
    p=open('temp.py','w')
    global user_name
    global user_pass
    p.write('user_name='+'\''+str(user_name)+'\''+'\n')
    p.write('user_pass='+'\''+str(user_pass)+'\''+'\n')
    p.close()
project = Tk(className='Login Credentials')
project.iconbitmap('C:/Users/suraj/Desktop/PCPS Project/Final/icon.ico')
project.geometry("800x450")

bg = PhotoImage(file="C:\\Users\\suraj\\Desktop\\PCPS Project\\Final\\BG.png")
ji = Label(project,image = bg)
ji.place(x=20,y=0)

#unwanted

menu = Menu(project) 
project.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New' , command=Print) 
filemenu.add_command(label='Open', command=Print) 
filemenu.add_separator()
filemenu.add_command(label='Exit', command=project.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About', command=Print1)

#code starts from here

user_n= Entry(project, width=30, font=('Arial', 18))
#user_n.insert(0, 'Entre you Username')
user_p=Entry(project, width=30,show='.', font=('Arial', 18))
#user_p.insert(0, 'Entre you Password')
user_n.place(x=250,y=270)#.grid(row=1,column=2)
user_p.place(x=250,y=310)#.grid(row=1,column=2)
l_n=Label(project,text='Username:-', font=('Arial', 18)).place(x=100,y=270)#.grid(row=1,column=1)
l_p=Label(project,text='Password:-', font=('Arial', 18)).place(x=100,y=310)#.grid(row=1,column=1)
b_lank(3,1)
submit = Button(project,text='Submit',command=submision ,font=('Arial', 13), padx= 10, pady= 6).place(x=410,y=350)#.grid(row=3,column=2)
'''
#this is perfect

possibilities=['hey','ssup','heavy','ji']
clicked = StringVar()
clicked.set(possibilities[0])
drop = OptionMenu(project,clicked, *possibilities)
drop.grid(row=5,column=1)
'''
'''
user_n = Entry(project, text="Entre you Username").get()
user_P = Entry(project, text="Entre you Password", show='*').get()
input = Entry(Project, text="will be displayed").get()#this is used to get values # we can use .insert(0, 'Hey') / .delete(0) / .
'''
project.mainloop()