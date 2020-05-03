class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class list:
    def __init__(self):
        self.head=None
        
        
    def addatbegin(self,item):
        temp=Node(item)
        temp.next=self.head
        self.head=temp
        
        
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data)
            temp = temp.next
            
            
            
            
    def getMiddle(self, head): 
        if (head == None): 
            return head 

        slow = head 
        fast = head 

        while (fast.next != None and 
                fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
                
        return slow 

        
    def mergeSort(self, head): 
        if head == None or head.next == None: 
            
            return head
 
        middle = self.getMiddle(head) 
        nexttomiddle = middle.next

        middle.next = None


        left = self.mergeSort(head) 
            

        right = self.mergeSort(nexttomiddle) 

        sortedlist = self.sortedMerge(left, right) 
        return sortedlist 
    def sortedMerge(self, a, b): 
        result = None
        
        if a == None: 
            return b 
        if b == None: 
            return a 
            

        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result 
        


        

lst=[2,3,5,10,15,20,50]  

new=list()
for i in lst:
    new.addatbegin(i)


new.printList()
print('--------------------------->')
new.head = new.mergeSort(new.head) 
new.printList()
