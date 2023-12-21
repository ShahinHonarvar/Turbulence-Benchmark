import itertools
def all_left_truncatable_prime(nums):
    return [x for x in range(3,int(str(nums[0])[0])+1) if all(x%d!=0 for d in range(2,int(str(x))+1)) and all(str(x)[:i]+str(x)[i+1:]==str(x) for i in range(1,len(str(x))+1))]
