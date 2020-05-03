
class Node:
    def __init__(self,data=None,nxt=None):
        self.data=data
        self.nxt=None
    def setdata(self,item):
        self.data=item
    def getdata(self):
        return self.data
    def setnxt(self,newnxt):
        self.nxt=newnxt
    def getnxt(self):
        return self.nxt

class list:
    def __init__(self):
        self.head=None
    def isempty(self):
        return self.head==None
    def addatbegin(self,item):
        temp=Node(item)
        temp.setnxt(self.head)
        self.head=temp
        
    def addatend(self,item):
        newnode=Node(item)
        if self.head is None:
            self.head=newnode
            return
        start=self.head
        while start.nxt is not None:
            start=start.getnxt()
        start.setnxt(newnode)
    
    
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.getdata())
            temp = temp.getnxt()
        
        
    def bubbledataexchange(self):
        end = None
        while end != self.head:
            p = self.head
            while p.nxt != end:
                q = p.nxt
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                p = p.nxt
            end = p
    def bubwithlinkage(self):
        end=None
        while end!=self.head:
            r = p = self.head
            while p.nxt != end:
                q = p.nxt
                if p.data > q.data:
                    p.nxt = q.nxt
                    q.nxt = p
                    if p != self.head:
                        r.nxt = q
                    else:
                        self.head = q
                    p,q = q,p
                r = p
                p = p.nxt
            end = p

    
    #sort and merge two linked list with and without
    #third list
    
def mergewiththirdlist(head1,head2):
    temp=None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data<=head2.data:
        temp=head1
        temp.nxt=mergewiththirdlist(head1.nxt,head2)
    else:
        temp=head2
        temp.nxt=mergewiththirdlist(head1,head2.nxt)
    return temp

newlist=list()

for i in range(10,50,10):
    newlist.addatend(i)
newlist.printList()
print('--------------------------------------->')



newlist2=list()

for i in range(80,120,12):
    newlist2.addatend(i)
    
newlist2.printList()
    
print('--------------------------------------->')
    
newlist3=list()
newlist3.head=mergewiththirdlist(newlist.head,newlist2.head)

newlist3.printList()
