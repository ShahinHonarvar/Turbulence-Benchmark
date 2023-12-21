def find_second_smallest_num(nums):
    sm = sorted(nums)[10]
    while True:
        sm += 1
        if len(nums) > sm:
            break
        else:
            return None
    return nums[sm - 1]
