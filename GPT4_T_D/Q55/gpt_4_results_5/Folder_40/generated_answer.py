
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(1, n+1):
            temp = lst[i:j] + lst[0:i+j-n] if i+j > n else lst[i:j]
            product = 1
            for number in temp:
                product *= number
            if product == -9:
                sublists.append(temp)
    return sublists
