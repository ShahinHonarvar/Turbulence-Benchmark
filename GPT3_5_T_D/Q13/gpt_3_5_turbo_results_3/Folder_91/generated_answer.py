
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    numbers = numbers[:6]
    numbers.sort()
    return numbers[-2] if numbers[-2] != numbers[-1] else None
