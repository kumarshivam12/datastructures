
def climbingLeaderboard(scores, alice):
    # List to contain and return Alice's ranks.
    results = []
    
    # Unique values from scores, since duplicate scores will have same rank (their index value).
    leaderboard = sorted(set(scores), reverse = True)
    
    # Use this var to track index within leaderboard later.
    l = len(leaderboard)
    #print(leaderboard[l)
    
    # Loop through each of Alice's scores
    for a in alice:
        
        # If Alice's score is >= the score at the index of the end of leaderboard...
        # Subtract 1 from that index value (which is also the rank) to check the next score up.
        # If the score is less than the next score up, the index (rank) will be added to results.
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
            print(l)
            
        # We add 1 to the appended value to account for 0-indexing.
        #print(l)
        results.append(l+1)
        print(results)
    return results







scores=[100,100,50,40,40,20,10]
alice=[5,25,50,120]
print(climbingLeaderboard(scores,alice))
'''
leaderboard=scores
leaderboard.extend(alice)
new= sorted(set(leaderboard),reverse=False)
print(new)
def bs(arr,i,r,x):
    while i <= r: 
  
        mid = i + (r - i) // 2 
        
          
      
        if (arr[mid] == x):
            return mid 
  
    
        elif (arr[mid] < x): 
            i = mid + 1
  
       
        else: 
            r = mid - 1
#print(len(new))
for i in alice:
    
    result=bs(new,0,len(new)-1,i)
    print(len(new)-result) 
 '''   
scores=[100,100,50,40,40,20,10]
alice=[5,25,50,120] 
res=[]
n=[]
n.insert(0,1)
for i in range(1,len(scores)):
    if scores[i]==scores[i-1]:
        n.append(n[i-1])
    else:
        n.append(n[i-1]+1)
      