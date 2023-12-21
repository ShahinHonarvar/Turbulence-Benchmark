
def find_second_smallest_num(numbers):
    numbers = numbers[1:101] if len(numbers) >= 101 else numbers[1:]
    numbers = list(set(numbers))
    if len(numbers) < 2:
        return None
    numbers.sort()
    return numbers[1]
