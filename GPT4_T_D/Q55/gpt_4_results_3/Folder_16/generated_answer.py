
def lists_with_product_equal_n(lst):
    from collections import deque
    size = len(lst)
    results = []
    for i in range(size):
        q = deque()
        product = 1
        for j in range(i, i+size):
            indx = j % size
            q.append(lst[indx])
            product *= lst[indx]
            while q and product > -837:
                val = q.popleft()
                product /= val
            if product == -837:
                results.append(list(q))
    return results
