
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers)[::-1]
    second_largest = sorted_nums[56]
    if second_largest == numbers[57]:
        return None
    else:
        return second_largest
