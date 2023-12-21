
def all_neg_ints_exclusive(nums):
    start = 20
    end = 43
    neg_ints = []
    
    for num in nums[start:end]:
        if num < 0:
            neg_ints.append(num)
    
    return neg_ints
