def find_second_smallest_num(nums):
    second_smallest = sorted(nums)[1]
    for i in range(len(nums)):
        if nums[i] < second_smallest:
            second_smallest = nums[i]
            break
    return second_smallest
