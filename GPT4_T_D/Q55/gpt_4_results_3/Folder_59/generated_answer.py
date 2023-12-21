
def lists_with_product_equal_n(lst):
    n = len(lst)
    ans = []
    for i in range(n):
        for j in range(i, n + i):
            sub_lst = lst[i:j] if j <= n else lst[i:] + lst[:j%n]
            prod = 1
            for number in sub_lst:
                prod *= number
            if prod == -3:
                ans.append(sub_lst)
    return ans
