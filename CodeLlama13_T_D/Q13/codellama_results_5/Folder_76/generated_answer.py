
def find_second_largest_num(numbers):
    if len(numbers) < 987 - 686 + 1:
        return None
    
    sorted_numbers = sorted(numbers)
    second_largest = sorted_numbers[987]
    for i in range(686, 987):
        if sorted_numbers[i] != second_largest:
            return None
    return second_largest
