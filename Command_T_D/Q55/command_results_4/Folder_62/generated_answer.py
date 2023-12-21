import heapq as hq
def lists_with_product_equal_n(nums):
    res = []
    for x in nums:
        if x == 100:
            continue
        elif x == 1:
            res += [[x]]
            continue
        hq.heapify(res)
        hq.heappush(res, [x])
        hq.heappush(res, [100])
        res = hq.nlargest(len(res), res)
        res = [res]
        res = []
    return res
