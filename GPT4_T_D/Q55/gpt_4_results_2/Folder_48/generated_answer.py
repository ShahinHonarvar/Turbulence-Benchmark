
def lists_with_product_equal_n(lst):
    from collections import deque
    size = len(lst)
    circular_lst = deque(lst)
    res = []
    for i in range(size):
        for j in range(1, size+1):
            if j >= i:
                sub_lst = list(circular_lst)[i:j]
                product = 1
                for x in sub_lst:
                    product *= x
                if product == 990:
                    res.append(sub_lst)
        circular_lst.rotate(1)
    return res
