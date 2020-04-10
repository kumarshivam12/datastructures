from pythonds.basic import Deque
def pall(string):
    q=Deque()
    for ch in string:
        q.addRear(ch)
    eql=True
    while q.size()> 1 and eql:
        first=q.removeFront()
        last=q.removeRear()
        if first!=last:
            eql=False
    return eql

print(pall('radar'))
