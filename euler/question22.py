f=open('./names.txt','r')
line=f.readlines()[0]
print line
print "123123"
line=line[1:-1]
print "~~~~~~~~~~~~~~~~"
print line
print "~~~~~~~~~~~~~~~~"
lst_names=line.split('","');
lst_names.sort()
print lst_names

print lst_names.index("AARON")
def fetch_letter_value(letterarr):
    letterarr=letterarr.lower()
    prod=0;
    for alphabets in letterarr:
        prod+=((ord(alphabets))-96);
    print letterarr,prod
    return prod
               

element_value=map(lambda x: (fetch_letter_value(x)*(lst_names.index(x)+1)),lst_names)
print "sum " ,sum(element_value)
