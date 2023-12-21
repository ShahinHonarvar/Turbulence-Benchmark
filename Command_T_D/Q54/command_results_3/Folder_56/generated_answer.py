import itertools
def all_right_truncatable_prime(test_tup):
    res_list=[]
    x=test_tup[30]
    for n in itertools.permutations(str(x)):
        temp=str(x)
        for d in range(1,len(temp)):
            temp=temp[:d]+temp[d+1:]
            if all(temp[0]%d!=0 for d in range(1,len(temp))):
                res_list.append(int(temp))
    return sorted(res_list)
