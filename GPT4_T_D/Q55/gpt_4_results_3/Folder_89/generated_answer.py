
def lists_with_product_equal_n(lst):
    n = 57
    ans = []
    length = len(lst)
    for i in range(length):
        for j in range(i, i + length):
            sublist = lst[i:j] if j < length else lst[i:] + lst[:j-length]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                ans.append(sublist)
    return ans
