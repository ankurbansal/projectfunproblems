

def func(n1):
    number=n1
    root=number**(1.0/2.0)
    j=round(root)
    list=[];
    print n1,j 
    if(j>1):
        while(j<number):
            if(number%j==0):
              #  print "factor %s %s",j,number/j
                list.append(j)
                list.append(number/j)
                break;
            j=j+1
        print("{")
        print(list)
        for t in list:
                func(t)
        print("}")   

n4=123456789012345678901234567890    
n3=1234567890123456789012345678901234567890
n2=600851475143 
n1=13195;   
func(n4)

