
def find_second_smallest_num(numbers):
    selected_nums = numbers[40:81]
    selected_nums.sort()
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]
