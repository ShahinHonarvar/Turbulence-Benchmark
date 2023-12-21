import set
def composite_nums_between_indices(nums):
    c = set()
    for i in range(50, 201):
        if any(str(i) in str(j) for j in nums):
            c.add(i)
    return c
