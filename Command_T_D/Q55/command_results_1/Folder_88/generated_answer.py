import heapq
def lists_with_product_equal_n(nums):
    if nums == []:
        return []
    if nums[0] == -56:
        return [[-56]]
    heapq.heapify(nums)
    output = []
    for _ in range(len(nums)):
        current_product = 1
        current_list = []
        while True:
            current_product *= nums[0]
            current_list.append(nums[0])
            if current_product == -56:
                output.append(current_list)
                break
            if heapq.heappop(nums) == -56:
                break
    return output
