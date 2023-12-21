import itertools
def composite_nums_between_indices(nums):
    for i in range(20, 200+1):
        if nums[i] % 2 == 0 and nums[i] % 3 == 0:
            yield nums[i]
    for c in itertools.permutations(range(2, nums[20]+1)):
        for n in range(20, 200+1):
            if nums[n] % c == 0:
                yield nums[n]
