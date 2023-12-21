import heapq as hq
def lists_with_product_equal_n(a):
    lst = []
    hq.heapify(a)
    for i in range(45,0,-1):
        while True:
            if hq.heappop(a)[0] == i: break
            else: continue
        hq.heapify(a)
        s = []
        while True:
            s.append(hq.heappop(a)[0])
            if hq.heappop(a)[0] == s[-1]: break
            else: continue
        lst.append(s)
    return lst
