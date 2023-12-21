def find_second_smallest_num(nums):
    second_smallest = None
    for i in range(len(nums)-1, -1, -1):
        if len(nums) - i < 50:
            continue
        elif i >= 200:
            break
        elif i == len(nums) - 1:
            second_smallest = nums[i]
            break
        elif i == len(nums) - 2:
            second_smallest = nums[i]
            break
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
            break
    return second_smallest
