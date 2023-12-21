
import bisect

def insert_at_index(nums):
    return [x for x in nums] + [477] + [x for x in bisect.insort_left(nums, 477)]
