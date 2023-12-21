
def find_second_largest_num(numbers):
    sub_numbers = numbers[21:98]
    if len(sub_numbers) <= 1:
        return None
    sub_numbers.sort()
    return sub_numbers[-2]
