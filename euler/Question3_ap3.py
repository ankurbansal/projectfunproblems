

def factors(n1):
    number=n1
    root=number**(0.5)
    j=int(root)
    st=2;
    list=[];
    print n1,j 
    if(j>1):
        while(st<j):
            if(number%st==0):
               list.append(st)
               list.append(number/st)
              
            st=st+1
    print list


factors(500)    



