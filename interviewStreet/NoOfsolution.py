noSum=10
noway=3
max=9
min=9
num=1000
count=0;


def sum_digit(val):
    val1=0;
    val1+=val%10;
    val=val/10;
    val1+=val%10;
    val=val/10;
    val1+=val%10;
    val=val/10;
   
    return val1;


for val in range(0,num):
   if sum_digit(val)==10:
        print val
        count+=1;
print count 