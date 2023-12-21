
def find_second_largest_num(numbers):
    numbers.sort()
    if len(numbers) < 21:
        return None
    else:
        return numbers[-2]
