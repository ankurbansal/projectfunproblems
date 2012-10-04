def add(dict,fact):
    if dict.has_key(fact):
        dict[fact]=dict[fact]+1
    else :
        dict[fact]=1

def delete(dict,k):
        if dict.has_key(k):
            if dict[k]==1:
                del dict[k]
            else:
                dict[k]=dict[k]-1
                
def compute(dict):
    value=1;
    for (k,v) in dict.items():
        value=value*(k**v)
    return value
