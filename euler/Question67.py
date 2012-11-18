f = open(r'C:\ank\poc\projectfunproblems\inputfile.txt', 'r')
arr=[]
for line in f.readlines():
    arr2=[]
    arr2=line.replace("\n","").split(" ");
    arr.append(arr2)
#arr=[[75],[95,64],[17,47,82],[18,35,87,10],[20,04,82,47,65],[19,01,23,75,03,34],[88,02,77,73,07,63,67],[99,65,04,28,06,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,04,68,89,53,67,30,73,16,69,87,40,31],[04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]];
print arr
print "--------------"
for i in xrange(1,arr.__len__()):
    for j in xrange(0,arr[i].__len__()):
        parenty=i-1;
        parentx=j;
        parentx2=j-1;
        if parentx<arr[i-1].__len__() and parentx2>=0:
            value=max(int(arr[parenty][parentx]),int(arr[parenty][parentx2]));
        elif parentx<arr[i-1].__len__():
            value =int(arr[parenty][parentx]);
        else :
            value =int(arr[parenty][parentx2]);
        arr[i][j]=int(arr[i][j])+value;
        

print max(arr[arr.__len__()-1])
    