from tkinter import *
window=Tk()
window.geometry("450x450")
window.title("GUI")
window.config(background="#F7CFD8")


counter=0

#the counter function
def handleEvent(event):
    
    if event.keysym not in ['BackSpace','Delete','space']:
        global counter
        counter+=1
        label2.config(text=counter)
        label3.config(text=f'your name has {counter} characters')
        
#submit function 

def submit():
    name=entry.get()
    label.config(text=name)
    if name=="":
        label.config(text="please enter something ")
    else:         
        label.config(text=f' Hello, {name} ,nice to meet you!')   


#entry 1 setup     
entry=Entry(width=30,bd=2, relief="solid")
entry.insert(0,"Enter your name")
entry.pack(pady=10,padx=10)

#button 1 setup
button1=Button(window,text="click me",command=submit,width=10)
button1.pack(pady=5) 


#entry 2 
entry2=Entry(width=30,bd=2, relief="solid")
entry2.insert(0,"Enter the input string")
entry2.pack(pady=10,padx=10)
entry2.bind("<Key>", handleEvent)

#button 2
button2=Button(window,text="click me",command=handleEvent,width=10)
button2.pack(pady=5)


#label setup
label=Label(window,font=('Arial',20),bg="#F7CFD8",pady=125)
label.pack()#to add the label to the window


#label 2
label2=Label(window,font=('Arial',20),bg="#F7CFD8",pady=125)
label2.pack()

#label 3
label3=Label(window,font=('Arial',20),bg="#F7CFD8",pady=125)
label3.pack()

window.mainloop() #it will display the window 