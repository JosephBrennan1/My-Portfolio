def solution(S):
    # write your code in Python 3.6
    S=list(S)
    allowed = ('^','>','v','<')
    
    for i in range(0, len(S)):
        if S[i] not in allowed:
            #print('Inappropriate Input')
            break
        elif len(S) > 100:
            #print('Inappropriate Input')
            break
        else:
            up = S.count(allowed[0])
            #print('No. of Up =',up)
            
            right = S.count(allowed[1])
            #print('No. of Right =',right)
            
            down = S.count(allowed[2])
            #print('No. of Down =',down)
            
            left = S.count(allowed[3])
            #print('No. of Left =',left)
            
            totals = {'up': up, 'right': right, 'down': down, 'left': left}
            
            winner = max(totals, key=totals.get)
            print(winner, 'has the most with',totals.get(winner))
                  
        
            rot = len(S) - totals.get(winner)    
            print(rot)
            return(rot)
    pass

