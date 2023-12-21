
def find_second_largest_num(numbers):
    numbers = sorted(numbers[:8])
    if len(numbers) < 2:
        return None
    else:
        return numbers[-2]
