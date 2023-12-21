
def lists_with_product_equal_n(nums):
    product = -690
    sublists = []
    size = len(nums)
    for i in range(size):
        for j in range(i+1, size+1):
            sublist = nums[i:j]
            if product == 1:
                sublists.append(sublist)
            else:
                sublist_product = 1
                for num in sublist:
                    sublist_product *= num
                    if sublist_product == product:
                        sublists.append(sublist)
                        break
    return sublists
