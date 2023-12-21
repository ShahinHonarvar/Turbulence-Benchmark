
def find_second_largest_num(numbers):
    selected_nums = numbers[29:94]

    if not selected_nums:
        return None

    selected_nums.sort()
    
    if len(selected_nums) == 1:
        return None

    return selected_nums[-2]
