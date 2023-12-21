import itertools
def lists_with_product_equal_n(nums):
    for i in range(len(nums)):
        yield [nums[i]]
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                yield [nums[i],nums[j],nums[k]]
    for p in itertools.permutations(nums):
        yield [p]
