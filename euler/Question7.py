def isPrime(n,list):
    isPrime=False;
    for pn in list:
        if pn>int(n**(0.5)):
         isPrime=True;
         break;
        if (n%pn==0):
         break;
   
    return isPrime


count=3
value=2
lst=[2,3]
while (value<10001):
      count=count+2;
      if isPrime(count,lst):
         lst.append(count);
         value=value+1;
        
print count
print lst  
     

        
         
        
     
