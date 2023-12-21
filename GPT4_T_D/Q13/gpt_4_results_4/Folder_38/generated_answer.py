
def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    second_largest = sorted(numbers[22:64], reverse=True)[1] if len(numbers[22:64]) > 1 else None
    return second_largest
