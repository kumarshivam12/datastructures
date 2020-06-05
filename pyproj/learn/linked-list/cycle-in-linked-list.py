#Brent's Algorithm,the fast pointer moves in the power of 2^
#in comparision to the floyd's algorithm it reduces the cost by lowering the number of movements
#Time Complexity: O(m + n) where m is the smallest index of the sequence 
# which is the beginning of a cycle, and n is the cycle’s length.

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
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.getnxt()
            
    def returnend(self):
        temp=self.head
        while(temp.nxt!=None):
            temp=temp.getnxt()
        return temp
        
    def cycle(self):
        temp=self.head
        #if there is no element
        if not temp:
            return False
        slow=temp
        fast=temp.nxt
        power=1
        length=1
        while(fast and fast!=slow):
            if(length==power):
                #when this condition meets,increase the power in the power of 2
                power*=2
                length=0
                slow=fast
            fast=fast.nxt
            length+=1
        print('length of loop is',length)  #if there is cycle then this lenght is the lenght of cycle
        #there is no extra cost for calculating the length
        if(not fast):
            return
        
        #driver to find the begening of the loop
        fast=slow=self.head
        while(length>0):
            fast=fast.nxt
            length-=1
        while(fast!=slow):
            fast=fast.nxt
            slow=slow.nxt  
        return fast
    
    
    
ll=list()
ll.addatbegin(10)
ll.addatbegin(20)
ll.addatbegin(30)
ll.addatbegin(40)
ll.addatbegin(50)
ll.printlist()
end=ll.returnend()
end.nxt=ll.head.nxt.nxt
res=ll.cycle()
if(res):
    print("found cycle at")
    print(res.data)
  

         
        