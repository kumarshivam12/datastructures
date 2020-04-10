class Node:
    def __init__(self,item):
        self.data=item
        self.nxt=None
        
    def setdata(self,item):
        self.data=item
    def getdata(self):
        return self.data
    def setnxt(self,newnxt):
        self.nxt=newnxt
    def getnxt(self):
        return self.nxt
    
class List:
    def __init__(self):
        self.head=None
    def isempty(self):
        return self.head==None
    def addatbegin(self,item):
        temp=Node(item)
        temp.setnxt(self.head)
        self.head=temp
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.getdata())
            temp = temp.getnxt()
    def addatend(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        n=self.head
        while n.nxt is not None:
            n=n.getnxt()
        n.setnxt(newnode)
        
        
    def insertAfter(self,node,item):
        n=self.head
        while n is not None:
            data=n.getdata()
            if data==node:
                break
            n=n.getnxt()
        if n is None:
            print('No data found')
        else:
            newnode=Node(item)
            newnode.setnxt(n.getnxt())
            n.setnxt(newnode)
    def test(self,item):
        n=self.head
        while n.getnxt() !=None:
            if n.getnxt().getdata()==item:
                break
            n=n.getnxt()
        print(n.getdata())
        



mylist=List()
mylist.addatbegin(40)
mylist.addatbegin(30)
mylist.addatend(50)
mylist.insertAfter(50,60)
mylist.addatend(70)
mylist.addatend(80)
mylist.addatend(90)
mylist.test(70)
mylist.printList()