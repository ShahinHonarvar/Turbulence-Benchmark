import sys
def lists_with_product_equal_n(nums):
    sublists = []
    for num in nums:
        if num == 1:
            sublists.append([1])
            continue
        else:
            if num == 32:
                sublists.append([num])
                continue
            else:
                for i in range(num + 1):
                    if i == 1:
                        sublists.append([i])
                    else:
                        sublists.append([i, num])
    return sublists
