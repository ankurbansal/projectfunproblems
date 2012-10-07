dict2={1:'one',2:'two', 3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred'};

def num(num):
    sum=0;
    if num==1000:
        return 'onethousand'.__len__();
    if num>=100:
        hundred= num/100;
        sum=sum+(dict2[hundred]).__len__();
        sum=sum+(dict2[100]).__len__();
        num=num%100;
        if num>0:
            sum=sum+str("and").__len__();
    if num>19 :
        sum=sum+str(dict2[(num/10)*10]).__len__();
        num=num%10;
    if dict2.has_key(num):
        sum=sum+(dict2[num]).__len__();
    return sum;


print sum(map(num,xrange(1,1001)))