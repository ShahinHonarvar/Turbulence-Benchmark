def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(70, 85):
        if len(set(nums)) == 2 and sorted(nums)[i - 1] == sorted(nums)[i]:
            second_smallest_num = sorted(nums)[i]
    return second_smallest_num
