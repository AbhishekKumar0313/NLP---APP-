from tkinter import *
from tkinter import messagebox
from db_connection import Database
from myapis import API


class NLPApp:
    def __init__(self) -> None:
        self.dbo=Database()
        self.apio=API()
        # we create a object of tkinter so that we can create gui
        self.root=Tk()
        # setting title name and favicon icon
        self.root.title("NLP App")
        self.root.iconbitmap('./resources/favicon.ico')
        # setting window size and background color
        self.root.geometry('400x600')
        self.root.configure(bg='crimson')
        
        # Login call
        self.login_gui()
        # we want hold the window on screen so we are using mainloop method of tkinter
        self.root.mainloop()
        
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP App",bg="crimson",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',20,'bold'))
        
        email=Label(self.root,text="Enter your email",bg="crimson",fg="white",font=('verdana',13,'bold'))
        email.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.email_value=Entry(self.root,width=50)
        self.email_value.pack(ipady=4)
        
        password=Label(self.root,text="Enter your password",bg="crimson",fg="white",font=('verdana',13,'bold'))
        password.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.password_value=Entry(self.root,width=50,show='*')
        self.password_value.pack(ipady=4)
        
        btn=Button(self.root,text='Login',width=8,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.login_process)
        btn.pack(pady=(30,10),padx=(48,10),anchor='w')
        
        
        register=Label(self.root,text="Not a member ? Register Now ",bg="crimson",fg="white",font=('verdana',10,'bold'))
        register.pack(pady=(20,10),padx=(45,10),anchor='w')
        
        register_btn=Button(self.root,text='Register',width=8,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.register_gui)
        register_btn.pack(pady=(10,10),padx=(48,10),anchor='w')
        
    
    def register_gui(self):
        self.clear()
        
        heading=Label(self.root,text="Register",bg="crimson",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',20,'bold'))
        
        name=Label(self.root,text="Enter your name",bg="crimson",fg="white",font=('verdana',13,'bold'))
        name.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.name_value=Entry(self.root,width=50)
        self.name_value.pack(ipady=4)
        
        email=Label(self.root,text="Enter your email",bg="crimson",fg="white",font=('verdana',13,'bold'))
        email.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.email_value=Entry(self.root,width=50)
        self.email_value.pack(ipady=4)
        
        password=Label(self.root,text="Enter your password",bg="crimson",fg="white",font=('verdana',13,'bold'))
        password.pack(pady=(20,10),padx=(45,10),anchor='w')
        self.password_value=Entry(self.root,width=50,show='*')
        self.password_value.pack(ipady=4)
        
        btn=Button(self.root,text='Register',width=8,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.registration_process)
        btn.pack(pady=(30,10),padx=(48,10),anchor='w')
        
        
        login=Label(self.root,text="Already a member ? Login Now ",bg="crimson",fg="white",font=('verdana',10,'bold'))
        login.pack(pady=(20,10),padx=(45,10),anchor='w')
        
        login=Button(self.root,text='Login',width=8,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.login_gui)
        login.pack(pady=(10,10),padx=(48,10),anchor='w')
        
        
        
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def registration_process(self):
        name=self.name_value.get()
        email=self.email_value.get()
        password=self.password_value.get()
        
        response=self.dbo.add(name,email,password)
        if response==1:
            messagebox.showinfo('Success','Registration Successful')
            self.login_gui()
        else:
            messagebox.showerror('Error','Email Already Exists')
    
    def login_process(self):
        email=self.email_value.get()
        password=self.password_value.get()
        
        response=self.dbo.search(email,password)
        if response==1:
            messagebox.showinfo('Success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect Email or Password')
    
    def home_gui(self):
        self.clear()
        heading=Label(self.root,text="Home",bg="crimson",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',20,'bold'))
        
        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=20,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.sentiment_gui)
        sentiment_btn.pack(pady=(30,10),padx=(48,10))
        
        NER_btn=Button(self.root,text='Name Entity Recognition',width=20,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.login_gui)
        NER_btn.pack(pady=(30,10),padx=(48,10))
        
        Emotion_btn=Button(self.root,text='Emotion Analysis',width=20,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.login_gui)
        Emotion_btn.pack(pady=(30,10),padx=(48,10))
        
        
        logout=Button(self.root,text='Logout',width=8,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.login_gui)
        logout.pack(pady=(30,10),padx=(48,10))
        
    def sentiment_gui(self):
        self.clear()
        heading=Label(self.root,text="Sentiment Analysis",bg="crimson",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',20,'bold'))
        
        label=Label(self.root,text="Enter text here",bg="crimson",fg="white",font=('verdana',13,'bold'))
        label.pack(pady=(20,10),padx=(30,10))
        self.content=Entry(self.root,width=30)
        self.content.pack()
        
        Analyze=Button(self.root,text='Analyze',width=8,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.do_sentiment)
        Analyze.pack(pady=(30,10),padx=(48,10))
        
        self.result=Label(self.root,text="",bg="crimson",fg="white",font=('verdana',13,'bold'))
        self.result.pack(pady=(20,10),padx=(45,10))
        
        
        
        Go_back=Button(self.root,text='Go back',width=8,bg="white",fg="crimson",font=('verdana',10,'bold'),command=self.home_gui)
        Go_back.pack(pady=(30,10),padx=(48,10))
        
    def do_sentiment(self):
        text=self.content.get()
        result=self.apio.sentiment_analysis(text)
        data=[]
        for i in result['scored_labels']:
            data.append((i['label'],i['score']))
        sorted(data,reverse=True,key=lambda x:x[1])
        res=data[0][0]
        self.result['text']=res
        
app=NLPApp()