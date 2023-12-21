
def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None

    numbers_limit = numbers[30:201] if len(numbers) > 200 else numbers[30:]
    numbers_limit.sort()

    return numbers_limit[1] if len(numbers_limit) > 1 else None
