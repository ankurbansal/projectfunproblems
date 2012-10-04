
lst=reversed(range(1,20))

def closedfactor(n):
    number=n
    root=number**(1.0/2.0)
    j=int(root)
    if(n==2):
        return 2;
    if(n==3):
        return 3;
    if j>1:
        while(j<=number):
           if(number%j==0):
               return j
           j=j+1;

def valueInkey():
    pass

def factors(n,lst):
    if(n==1):
        return lst
    else :
       value=closedfactor(n)
       if(value>1 and value!=n):
            lst.remove(n)
            lst.append(value)
            lst.append(n/value)
            lst=factors(value,lst)
            lst=factors(n/value,lst)
       return lst
    

lst=[];
#factors(2,lst)
#print lst

number=13195*4
lst.append(number)
print factors(number,lst)
    
