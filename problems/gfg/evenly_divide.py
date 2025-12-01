def evenlyDivides(n):
    temp=n
    
    count=0
    
    while n!=0:
        
        last_digit=n%10
        n=n//10
        
        
        if last_digit!=0 and  temp%last_digit==0:
            
            count+=1
    return count 
                