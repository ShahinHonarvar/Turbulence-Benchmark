
def find_second_largest_num(numbers):
    if len(numbers) < 557:
        return None
    nums = sorted(numbers[209:557])
    return nums[-2] if len(nums) >= 2 else None
