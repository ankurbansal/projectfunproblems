
# find the fact_number of factor 
# add them. put in  HashMap . 
# create total sum add it to that . 
# reusable components . 
def lst_all_factors(num):
    """get all the factors """
    fact_number=num;
    root=fact_number**(0.5);
    j=int(root)
    list=[1];
#    print fact_number,j 
    if(j>1):
        while(j<fact_number):
            if(fact_number%j==0):
                list.append(j)
                list.append(fact_number/j)
            j=j+1
    return list

num_sum_factors_map={}
lstValue=[]
num=50
total=0

for num in xrange(1,10000):
    lstValue=lst_all_factors(num)
    #print lstValue
    sum_factors=reduce(lambda x,y: x+y,lstValue)
    num_sum_factors_map[num]=sum_factors
    if(
       num_sum_factors_map.has_key(sum_factors)
       and num_sum_factors_map.get(sum_factors)==num
       and sum_factors<>num):
        print num,sum_factors
        total+=num+sum_factors
        
print total
