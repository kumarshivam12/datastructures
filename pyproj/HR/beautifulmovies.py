def rev(a):
    output=0
    while(a>0):
        rem=a%10
        output=(output*10)+rem
        a//=10
    return output


count=0
for i in range(20,24):
    if abs((i-rev(i))%6==0):
        count+=1
 