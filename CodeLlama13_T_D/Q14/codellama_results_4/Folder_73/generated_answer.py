
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    if len(sorted_nums) < 2:
        return None
    else:
        for i in range(59, 98):
            if sorted_nums[i] != sorted_nums[i - 1]:
                return sorted_nums[i]
