
def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    nums = numbers[8:10]
    nums.sort()
    return nums[-2] if nums[-2] != nums[-1] else None
