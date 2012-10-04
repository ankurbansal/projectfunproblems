#
#a+b+c=1000
#Find the product abc
#a2+b2=c2
def func(k,m):
    n=(500/(k*m))-m
    return n


for k in [1,2,250,4,125,5,100,10,50,20,25,500]:
    for m in [2,250,4,125,5,100,10,50,20,25]:
       n=func(k,m)
       if(n>0):
           if(m>n):
               print k,m,"--->",n
               a=(m**2-n**2)*k
               b=2*m*n*k
               c=(m**2+n**2)*k
               if(a+b+c)==1000:
                   print a,b,c,(a+b+c),a*b*c
               

