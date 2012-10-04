

def func(n1):
    number=n1
    root=number**(1.0/2.0)
    j=round(root)
    print(j) 
    print("{")
    while(j<number):
        if(number%j==0):
            print j
            func(number/j)
            break;
        j=j+1
    print("}")   



