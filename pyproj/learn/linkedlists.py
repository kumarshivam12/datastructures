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
            
            
            
            
    def insertbefore(self,node,item):
        
        if node == self.head.data:
            newnode=Node(item)
            newnode.setnxt(self.head)
            self.head=newnode
            return
        n=self.head
        while n.nxt is not None:
            if n.nxt.data==node:
                break
            n=n.nxt
            
        if n.nxt is None:
            print('No Items')
        else:
            newnode=Node(item)
            newnode.setnxt(n.getnxt())
            n.setnxt(newnode)
            
    def deletenode(self,item):
        
        """The delete node function can also be written with the help 
        of two pointers viz. Current aand Previous"""
        
        
        if self.head is None:
            print('No items in linked list')
        if self.head.getdata()==item:
            self.head=self.head.getnxt()
        n=self.head
        while n.getnxt() !=None:
            if n.getnxt().getdata()==item:
                break
            n=n.getnxt()
        if n.getnxt() is None:
            print('item not found')
        else:
            nxtnode=n.getnxt().getnxt()
            n.setnxt(nxtnode)

    def addatindex(self,index,item):
        if index==1:
            self.addatbegin(item)
            return

        i=1
        n=self.head
        while i< index-1 and n.getnxt() is not Node:
            i+=1
            n=n.getnxt()
        if n is None:
            print('no items')
        else:
            newnode=Node(item)
            newnode.setnxt(n.getnxt())
            n.setnxt(newnode)
            
    def len(self):
        if self.head==None:
            return 0
        n= self.head
        count=0
        while n is not None:
            count+=1
            n=n.getnxt()
        return count
    
    def search(self,data):
        i=1
        if self.head is None:
            return
        n=self.head
        count=0
        while n is not None:
            if n.getdata()==data:
                count=i
                print(f"Found node {data} at index {count}")
            i+=1
            n=n.getnxt()
            
    def deleteelementbyvalue(self,data):
        if self.head==None:
            return
        n=self.head
        while n.getnxt() is not None:
            if n.getnxt().getdata()==data:
                break
            n=n.getnxt()
        if n.getnxt()==None:
            return
        else:
            n.setnxt(n.getnxt().getnxt())
            
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            nextpointer=current.nxt
            current.nxt=prev
            prev=current
            current=nextpointer
        self.head=prev


    def recreverse(self,current,prev):
        if current.nxt is None :
            self.head=current
            current.nxt = prev
            return
        nextpointer=current.nxt
        current.nxt=prev
        self.recreverse(nextpointer,current)
        
    def callreverse(self):
        current=self.head
        prev=None
        self.recreverse(current,prev)


























mylist=List()
mylist.addatbegin(40)
mylist.addatbegin(30)
mylist.addatend(50)
mylist.insertAfter(50,60)
mylist.addatend(70)
mylist.addatend(80)
mylist.addatend(90)
mylist.deletenode(40)
mylist.insertbefore(50,40)
mylist.addatindex(8,100)
mylist.deleteelementbyvalue(50)


#========================================================>

mylist.printList()



print('--------------------------------------------------------------------')


print('length of list is',mylist.len())
mylist.search(70)
mylist.reverse()
mylist.printList()
mylist.callreverse()
mylist.printList()