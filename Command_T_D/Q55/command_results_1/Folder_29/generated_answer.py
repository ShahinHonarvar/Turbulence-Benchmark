import heapq as hq
def lists_with_product_equal_n(nums):
    hq.heapify(nums)
    result = []
    while True:
        prod = 1
        curr = hq.heappop(nums)
        while curr != 0:
            prod *= curr
            curr = hq.heappop(nums)
            if prod == 15:
                curr += 1
                hq.heappush(nums, curr)
                result.append(nums[:-1])
                break
    return result
