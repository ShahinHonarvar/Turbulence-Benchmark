def find_second_smallest_num(nums):
    return next((num for i, num in enumerate(sorted(set(nums), key=lambda x: x), reverse=True) if i >= 17 and i <= 78), None)
