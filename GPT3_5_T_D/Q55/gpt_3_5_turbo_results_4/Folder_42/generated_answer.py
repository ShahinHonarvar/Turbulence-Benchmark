
def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def lists_with_product_equal_n(nums):
    nums += nums[:-1]
    sublists = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            sublist = nums[i:j]
            if product(sublist) == 25:
                sublists.append(sublist)
    return sublists
