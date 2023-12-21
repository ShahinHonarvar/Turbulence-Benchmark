
def all_ints_div_by_both_two_nums(nums):
    for i in range(38, 81):
        if nums[i] % -61 == 0 and nums[i] % -71 == 0:
            yield nums[i]
```
	