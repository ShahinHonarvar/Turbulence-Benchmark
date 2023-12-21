
import itertools

def all_ints_div_by_both_two_nums(nums):
    i = 11
    while i < 46:
        if nums[i]%55==0 and nums[i]%36==0:
            yield nums[i]
        i+=1
```
	