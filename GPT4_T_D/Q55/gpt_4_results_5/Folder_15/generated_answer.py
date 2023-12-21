
def lists_with_product_equal_n(lst):
    ans = []
    n = len(lst)
    for length in range(1, n+1):
        for start in range(n):
            sublist = [lst[(start+i)%n] for i in range(length)]
            prod = 1
            for num in sublist:
                prod *= num
            if prod == -7:
                ans.append(sublist)
    return ans
