class Node:
    def __init__(self,data=None):
        self.data=data
        self.nxt=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def addatbegin(self,data):
        newnode=Node(data)
        newnode.nxt=self.head
        self.head=newnode
    
    def printlist(self):
        start=self.head
        while(start is not None):
            print(start.data)
            start=start.nxt
            
                
    def addtwoll(self,head1,head2):
        prev=None
        temp=None
        carry=0
        while(head1 is not None or head2 is not None):
            fdata=0 if head1 is None else head1.data
            sdata=0 if head2 is None else head2.data
            Sum=carry+fdata+sdata
            carry=1 if Sum>=10 else 0
            Sum=Sum if Sum<10 else Sum%10
            temp=Node(Sum)
            if self.head is None:
                self.head=temp
            else:
                prev.nxt=temp
            prev=temp
            if head1 is not None:
                head1=head1.nxt
            if head2 is not None:
                head2=head2.nxt
                
        if carry>0:
            temp.nxt=Node(carry)
            
newlist=LinkedList()
newlist.addatbegin(1)
newlist.addatbegin(2)
newlist.addatbegin(3)
newlist.addatbegin(4)
newlist.printlist()
newlist1=LinkedList()
newlist1.addatbegin(5)
newlist1.addatbegin(6)
newlist1.addatbegin(7)
newlist1.addatbegin(8)
newlist1.addatbegin(9)
newlist1.printlist()
res=LinkedList()
res.addtwoll(newlist.head,newlist1.head)
res.printlist()