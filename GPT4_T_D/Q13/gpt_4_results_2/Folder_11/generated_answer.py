
def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    
    second_largest = sorted(numbers[37:52], reverse=True)[1] if len(numbers[37:52]) > 1 else None

    return second_largest
