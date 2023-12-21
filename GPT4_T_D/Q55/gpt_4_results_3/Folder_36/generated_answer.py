
def lists_with_product_equal_n(lst):
    n = len(lst)
    ans = []
    for i in range(n):
        init = 1
        for j in range(i, i+n):
            j %= n
            init *= lst[j]
            if init == 714:
                ans.append(lst[i:j+1])
            elif init > 714:
                break
    return ans
