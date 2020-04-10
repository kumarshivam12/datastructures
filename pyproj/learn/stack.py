
from pythonds.basic import Stack
'''
s=Stack()
mstr='shivam'
rev=''
for i in mstr:
    s.push(i)
while not s.isEmpty():
    rev=rev+s.pop()
    
print(rev)

def balancedpar(string):
    balance=True
    mystack=Stack()
    index=0
    while index<len(string) and balance:
        symbol=string[index]
        if symbol=='(':
            mystack.push(symbol)
        else:
            if mystack.isEmpty():
                balance=False
            else:
                mystack.pop()
        index+=1
    if balance and mystack.isEmpty():
        return True
    else:
        return False
    
print(balancedpar('((((()))))'))
'''
