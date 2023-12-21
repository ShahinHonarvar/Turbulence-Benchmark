import itertools
def lists_with_product_equal_n(nums):
    if nums[0]==0 and nums[-1]==0:
        yield [0]*(len(nums)+1)
    for prods in itertools.permutations_with_replacement(range(-75,0,1),2):
        yield [nums[i:j+1] for i,j in zip(range(len(nums)), itertools.accumulate(prods))+[nums[-1]]
