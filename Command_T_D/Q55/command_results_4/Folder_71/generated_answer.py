import heapq as hq
def lists_with_product_equal_n(nums):
    if len(nums) < 2:
        return []
    hq.heapify(nums)
    result = []
    for i in range(2, len(nums)):
        prod = 1
        j = hq.heappop(nums)
        prod *= j
        while prod == 47:
            j = hq.heappop(nums)
            prod *= j
            result.append(list(range(i, j + 1)))
            prod = 1
    return result
