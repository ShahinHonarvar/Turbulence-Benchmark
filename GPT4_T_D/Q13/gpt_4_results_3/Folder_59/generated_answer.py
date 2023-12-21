
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        numbers.sort()
        return numbers[-2]
