import bisect
def composite_nums_between_indices(nums):
    c = set()
    for i in range(15,40):
        j = bisect.bisect_left(nums,i)
        if j != -1:
            for k in range(i*2,nums[j],i):
                if not k%i:
                    c.add(k)
        else:
            break
    return c
