
def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    sorted_nums = sorted(numbers)[661:924+1]
    second_largest = sorted_nums[1] if len(sorted_nums) >= 2 else None
    return second_largest
