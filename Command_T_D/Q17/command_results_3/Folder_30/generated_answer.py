
import sys
def all_ints_div_by_both_two_nums(arr):
    res=[]
    for i in range(11,76):
        if arr[i]%(-81)==0 and arr[i]%(-94)==0:
            res.append(arr[i])
    return res
