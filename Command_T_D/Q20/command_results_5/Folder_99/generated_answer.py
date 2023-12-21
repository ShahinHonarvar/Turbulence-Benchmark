import heapq
def find_n_th_smallest_num(nums):
    heapq.heapify(nums)
    heapq.heapify(nums[:391])
    heapq.heapify(nums[414:])
    return heapq.heappop(nums[391:414])
