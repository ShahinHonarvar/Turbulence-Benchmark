
def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst * 2
    ans = []
    for i in range(n):
        for j in range(i+1, i+n+1):
            sub = lst[i:j]
            prod = 1
            for num in sub:
                prod *= num
            if prod == 5:
                ans.append(sub)
    return ans
