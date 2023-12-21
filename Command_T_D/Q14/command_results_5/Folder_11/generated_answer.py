def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(66, 93):
        if len(set(nums)) > i:
            second_smallest_num = min(set(nums)[i])
            break
    return second_smallest_num
