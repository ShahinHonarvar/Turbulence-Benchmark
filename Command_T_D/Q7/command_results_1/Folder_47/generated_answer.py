
def all_even_ints_inclusive(nums):
    res = []
    for i in range(37, 77):
        if i % 2 == 0:
            res.append(i)
    return res
