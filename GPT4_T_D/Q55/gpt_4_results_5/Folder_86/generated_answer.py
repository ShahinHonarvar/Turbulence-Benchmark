
def lists_with_product_equal_n(lst):
    n = -779
    size = len(lst)
    result = []
    for i in range(size):
        for j in range(i, i + size):
            sublist = lst[j % size: j % size + (j - i + 1)]
            product = 1
            for k in sublist:
                product *= k
                if product == n:
                    result.append(sublist)
                    break
                elif product > n and product % n != 0:
                    break
    return result
