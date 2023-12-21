
def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        slice_nums = numbers[4:9]
        slice_nums.sort(reverse=True)
        if len(slice_nums) < 2:
            return None
        else:
            return slice_nums[1]
