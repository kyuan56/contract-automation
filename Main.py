import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.filedialog     
def merge(l1,l2):          #sorting which can be called everytime
    c = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i][0] < l2[j][0]:
            c.append(l1[i])
            i=i+1
        else:
            c.append(l2[j])
            j=j+1
    if i==len(l1):
        for k in l2[j:]:
            c.append(k)
    else:
        for k in l1[i:]:
            c.append(k)
    return c
def sort(l):        
    if len(l) <= 1:
        return l
    mid = len(l)//2
    left = sort(l[:mid])
    right = sort(l[mid:])
    return merge(left, right)
def bins(l,n):      #binary search
    mid=len(l)//2
    if l[mid][0]>n:
        return bins(l[:mid],n)
    elif l[mid][0]<n:
        return bins(l[mid+1:],n)
    elif l[mid][0]==n:
        return l[mid][1]
class item:           #class of items
    def __init__(self):
        self.num=""
        self.q=""
        self.name=""
        self.l=""
        self.d=""
    def insert(self,num,q,name,l,d): 
        self.num=num
        self.q=q
        self.name=name
        self.l=l
        self.d=d
def deallist(l,a,b,c,d,e):#five attribute the function is used to add item to list
    k=item()
    k.insert(a,b,c,d,e)
    l.append((a,k))
class Inv:
    def __init__(self,master):
        self.list=[]
        self.display=[""]
        mainframe=ttk.Frame(master,relief=SUNKEN,padding="3 3 12 12")
        mainframe.grid(column=0,row=0,columnspan=7,rowspan=6,sticky="NWES")
        mainframe.grid_rowconfigure(0,weight=1)
        mainframe.grid_columnconfigure(0,weight=1)

        ttk.Label(mainframe,text="Entry").grid(column=5,row=1,sticky="")
        ttk.Label(mainframe,text="Result").grid(column=2,row=1,columnspan=1,sticky="")
        ttk.Label(mainframe,text="Number").grid(column=0,row=2,columnspan=2,sticky="W")
        ttk.Label(mainframe,text="Quanity").grid(column=0,row=3,columnspan=2,sticky="WE")
        ttk.Label(mainframe,text="Name").grid(column=0,row=4,columnspan=2,sticky="WE")
        ttk.Label(mainframe,text="Location").grid(column=0,row=5,columnspan=2,sticky="WE")
        ttk.Label(mainframe,text="Description").grid(column=0,row=6,columnspan=2,sticky="WE")
        

        Message=ttk.Label(mainframe,text="Welcome",background="white")
        Message.grid(column=0,row=8,columnspan=3,sticky="E")

        self.num=StringVar()
        self.location=StringVar()
        self.name=StringVar()
        self.quan=StringVar()
        self.descrip=StringVar()
        inum=ttk.Label(mainframe,text="_____________")
        inum.grid(column=2,row=2,columnspan=2,sticky="W")

        iquan=ttk.Label(mainframe,text="_____________")
        iquan.grid(column=2,row=3,columnspan=2,sticky="W")

        iname=ttk.Label(mainframe,text="_____________")
        iname.grid(column=2,row=4,columnspan=2,sticky="W")        

        iloca=ttk.Label(mainframe,text="_____________")
        iloca.grid(column=2,row=5,columnspan=2,sticky="W")

        ides=ttk.Label(mainframe,text="_____________")
        ides.grid(column=2,row=6,columnspan=2,sticky="W")

        number=ttk.Entry(mainframe,width=12,textvariable=self.num)
        number.grid(column=5,row=2,columnspan=1,sticky="")

        quanity=ttk.Entry(mainframe,width=12,textvariable=self.quan)
        quanity.grid(column=5,row=3,columnspan=1,sticky="")

        name=ttk.Entry(mainframe,width=12,textvariable=self.name)
        name.grid(column=5,row=4,columnspan=1,sticky="")

        location=ttk.Entry(mainframe,width=12,textvariable=self.location)
        location.grid(column=5,row=5,columnspan=1,sticky="")

        description=ttk.Entry(mainframe,width=12,textvariable=self.descrip)
        description.grid(column=5,row=6,columnspan=1,sticky="")

        search=ttk.Button(mainframe,text="Search",command=lambda:self.bsearch(inum,iquan,iname,iloca,ides,number),state="disabled")
        search.grid(column=8,row=2,pady=3,sticky="W")

        add=ttk.Button(mainframe,text="New",command=lambda:self.iadd(number,quanity,name,location,description))
        add.grid(column=7,row=2,pady=3,sticky="W")

        delete1=ttk.Button(mainframe,text="Delete",command=lambda:self.del1(delete2),state="disabled")
        delete1.grid(column=7,row=3,pady=3,sticky="W")

        delete2=ttk.Button(mainframe,text="",command=lambda:self.del2(delete2,inum,iquan,iname,iloca,ides),state="disabled")
        delete2.grid(column=8,row=3,pady=3,sticky="W")

        update=ttk.Button(mainframe,text="Update",command=lambda:self.up(number,quanity,name,location,description,inum,iquan,iname,iloca,ides),state="disabled")
        update.grid(column=7,row=4,pady=3,sticky="W")

        loadf=ttk.Button(mainframe,text="Load Data",command=lambda:self.load())
        loadf.grid(column=7,row=5,pady=3,sticky="W")

        savef=ttk.Button(mainframe,text="Save Data",command=lambda:self.save(),state="disabled")
        savef.grid(column=8,row=5,pady=3,sticky="W")
        self.search1=[]
        self.search1.append(search)
        self.delete11=[]
        self.delete11.append(delete1)
        self.save1=[]
        self.save1.append(savef)
        self.notion=[]
        self.notion.append(Message)
        self.update1=[]
        self.update1.append(update)
       
    def message(self,arg,text1):      # to change instant messages 
        arg[0].config(text=text1)
    def disable(self,args):         #disable button
        for i in args:
            i.config(state="disabled")
    def enable(self,args):          #enable button
        for i in args:
            i.config(state="active")
    def save(self):                    
        path=tkinter.filedialog.askopenfilename()
        f=open(path,"w")
        for i in self.list:
            t=str(i[1].num)+","+str(i[1].q)+","+i[1].name+","+i[1].l+","+i[1].d+"\n"
            f.write(t)
        self.message(self.notion,"File Saved")
    def load(self):
        path=tkinter.filedialog.askopenfilename()
        try:
            f=open(path,"r")
        except:
            self.message(self.notion,"Invalid File")    #raise error when read unvalid file
        text=f.readlines()
        itemAttri=[]
        list1=[]
        for i in text:
            a=i.split(",")
            for j in a:
                k=j.strip()
                itemAttri.append(k)
            
            a=int(itemAttri[0])
            b=int(itemAttri[1])
            c=itemAttri[2]
            d=itemAttri[3]
            e=itemAttri[4]
            deallist(list1,a,b,c,d,e)             #putting item in list
            itemAttri=[]
        self.list=list1                       # makes the list completely the same as the loaded one
        self.list=sort(self.list)
        self.enable(self.search1)
        self.enable(self.save1)
        self.message(self.notion,"File Loaded")
        self.disable(self.update1)         #update is only avaliable after search
    def bsearch(self,num,q,name,loc,des,number):#five attribute from lable
        t=number.get()
        try:
            t=int(t)
        except:
            self.message(self.notion,"Invalid Entry")
        try:
            k=bins(self.list,t)
        except:
            self.message(self.notion,"Not found")
        num.config(text=k.num)
        q.config(text=k.q)
        name.config(text=k.name)
        loc.config(text=k.l)
        des.config(text=k.d)
        self.display[0]=(t,k)
        self.enable(self.delete11)
        self.enable(self.update1)         #update is only avaliable after search
        self.message(self.notion,"Search Complete")
    def iadd(self,num,q,name,loc,des):#five attribute of an item from entry
        t=item()
        t.num=num.get()
        t.q=q.get()
        t.name=name.get()
        t.l=loc.get()
        t.d=des.get()      #error when the quanity and number are not number or quanity is negative
        try:
            n=int(t.num)
        except:
            self.message(self.notion,"Value Invalid")
        try:
            test=int(t.q)
            test>=0
        except:
            self.message(self.notion,"Value Invalid")
        
        b=(n,t)
        self.list.append(b)
        self.list=sort(self.list)
        self.enable(self.search1)
        self.enable(self.save1)
        self.disable(self.delete11)
        self.message(self.notion,"Item added")
        self.disable(self.update1)      #update is only avaliable after search
    def del1(self,del2):               # two steps of deleting
        del2.config(state="active",text="confirm")

    def del2(self,del2,v1,v2,v3,v4,v5):#v1 to v5 is the attribute displayed which needed to be cleared
        self.list.remove(self.display[0])
        del2.config(state="disabled",text="") #disable delete until search
        self.disable(self.delete11)
        v1.config(text="_________")
        v2.config(text="_________")
        v3.config(text="_________")
        v4.config(text="_________")
        v5.config(text="_________")
        self.message(self.notion,"Item deleted")
        
    def up(self,num,q,name,loc,des,v1,v2,v3,v4,v5):#five attribute of an item from entry
        #v1 to v5 is the attribute displayed which needed to be changed
        t=item()
        t.num=num.get()
        t.q=q.get()
        t.name=name.get()
        t.l=loc.get()
        t.d=des.get()
        try:
            n=int(t.num)           #same as add item
        except:
            self.message(self.notion,"Entry Invalid")
        b=(n,t)
        k=bins(self.list,n)
        self.list.remove((n,k))
        self.list.append(b)

        self.list=sort(self.list)
        v1.config(text=t.num)
        v2.config(text=t.q)
        v3.config(text=t.name)
        v4.config(text=t.l)
        v5.config(text=t.d)
        self.message(self.notion,"Update Complete")
        
def main():
    master=Tk()
    
    master.title("表格")
    Inv(master)
    master.mainloop()

if __name__==main():
    main()

