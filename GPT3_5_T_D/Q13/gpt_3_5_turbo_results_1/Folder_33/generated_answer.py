
def find_second_largest_num(numbers):
    sub_numbers = numbers[667:775]
    sub_numbers.sort()
    if len(sub_numbers) < 2:
        return None
    else:
        return sub_numbers[-2]
