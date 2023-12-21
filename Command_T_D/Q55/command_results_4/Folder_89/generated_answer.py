import sys
def lists_with_product_equal_n(nums):
    res = []
    for a in range(1,nums.count(1)+1):
        if 1 == a or a == n:
            res += [[1]]
        elif 2 == a:
            res += [[1,2]]
        else:
            res += [[a]]
            for b in range(2,nums.count(a)+1):
                if a == b or b == n:
                    res += [[a,b]]
                else:
                    res += [[a,b]]
        if res:
            return res
    return []
