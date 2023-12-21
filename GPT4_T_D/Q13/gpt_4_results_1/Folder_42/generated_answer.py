
def find_second_largest_num(numbers):
    inclusive_numbers = numbers[29:80]
    if len(inclusive_numbers) < 2:
        return None
    else:
        inclusive_numbers.sort()
        return inclusive_numbers[-2]
