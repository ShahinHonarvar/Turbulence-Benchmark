
def find_second_largest_num(numbers):
    if 90 < len(numbers) < 100:
        numbers = numbers[91:100]
        numbers.sort()
        return numbers[-2]
    else:
        return None
