import time
start=time.clock()
def getSequenceSize(num,numcallatzSerSiz):
    if numcallatzSerSiz.has_key(num):
        return numcallatzSerSiz[num]
    else:
        if (num%2==0):
            return (1+getSequenceSize(num/2,numcallatzSerSiz));
        else :
            return (1+getSequenceSize(3*num+1,numcallatzSerSiz));
        



def startProcessing():
    numcallatzSerSiz={1:1}
    MaxSize=1000000;
    maxsequence=0;
    keyforMaxSequence=0;
    for num in xrange(2,MaxSize):
        numcallatzSerSiz[num]=getSequenceSize(num,numcallatzSerSiz);
        if maxsequence<numcallatzSerSiz[num]:
            maxsequence=numcallatzSerSiz[num]
            keyforMaxSequence=num
    print keyforMaxSequence


startProcessing();
print("time : %s"%(time.clock()-start))
