
def find_second_largest_num(numbers):
    numbers = sorted(numbers[246:751], reverse=True)
    if len(numbers) <= 1:
        return None
    else:
        return numbers[1]
