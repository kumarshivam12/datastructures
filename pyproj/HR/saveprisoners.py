def saveThePrisoner(n, m, s):
    result=((m+s-2)%n)+1
    r=m%n
    if(r+(s-1)%n==0):
        return n
    else:
        return r+(s-1)%n  