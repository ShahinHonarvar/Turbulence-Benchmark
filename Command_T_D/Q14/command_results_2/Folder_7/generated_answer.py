def find_second_smallest_num(nums):
    second_smallest = sorted(set(nums)[-3:-1])[-2]
    return second_smallest if second_smallest in range(686, 987) else None
