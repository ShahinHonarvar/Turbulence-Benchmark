
def find_second_smallest_num(numbers):
    second_smallest_num = sorted(numbers)[1] if len(numbers) >= 2 else None
    return second_smallest_num if 64 <= numbers.index(second_smallest_num) <= 66 else None
