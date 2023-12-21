
def find_second_largest_num(numbers):
    return sorted(numbers[22:64], reverse=True)[1] if len(numbers) >= 64 else None
