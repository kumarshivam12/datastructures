'''
class Fraction():
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)


frcn=Fraction(3,5)
frcn2=Fraction(4,9)
frnc3=frcn+frcn2
print(frnc3)

def findmin(alist):
    
    overallmin=alist[0]
    for i in alist:
        for j in alist:
            if i>j:
                overallmin=j
        return overallmin


def findminn(alist):
    smallest=alist[0]
    for i in alist:
        if i<smallest:
            smallest=i
    return smallest
print(findminn([5,94,0,44,5,66]))
'''
import timeit
from timeit import Timer

def test1():
    l=[x for x in range(1000)]
    
def test2():
    l=list(range(1000))
    
