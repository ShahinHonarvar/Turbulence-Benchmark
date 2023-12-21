import itertools
def composite_nums_between_indices(nums):
    i, j = 10, 66
    c = set(range(i, j+1))
    return set(list(itertools.filterfalse(lambda x: x == 1 or x == 2 or x == 3, c & set(nums)))))
