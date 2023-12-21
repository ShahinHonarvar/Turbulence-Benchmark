
def find_second_largest_num(numbers):
    numbers.sort()
    if len(numbers) < 2 or len(numbers) <= 3:
        return None
    else:
        return numbers[-2]
