def getprimefactors(num,factdictionary={}):
    if num==1:
        return factdictionary
    if num==2:
        if factdictionary.has_key(num):
            factdictionary[num]=factdictionary[num]+1;
        else:
            factdictionary[num]=+1; 
        return factdictionary
    if num==3:
        if factdictionary.has_key(num):
            factdictionary[num]=factdictionary[num]+1;
        else:
            factdictionary[num]=+1; 
        return factdictionary
    j=num**(.5);
    j=int(j);
    if j==1:
        return factdictionary
    while j<=num:
        if num==j:
            if factdictionary.has_key(num):
                factdictionary[num]=factdictionary[num]+1;
            else:
                factdictionary[num]=+1; 
            return factdictionary;          
        if(num%j==0):
                factdictionary.update(getprimefactors(j,factdictionary));
                factdictionary.update(getprimefactors(num/j,factdictionary));
                break;
        j=j+1;
    return factdictionary


       
 







QuestionLimit=500
numb=2
sum=3
print numb,sum
factdictionary={}
nofactors=2;
while(nofactors<QuestionLimit):
    numb=numb+1;
    sum=sum+numb;
    factdictionary={}
    factdictionary=getprimefactors(sum,factdictionary);
    value=map(lambda x: x+1,factdictionary.itervalues())
    nofactors=1;
    for fact  in value:
        nofactors=nofactors*fact;
    print numb,sum,factdictionary,value,nofactors

print numb,sum,nofactors
