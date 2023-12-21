
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None

    numbers.sort()
    second_largest = numbers[len(numbers) - 2]

    for i in range(62, 93):
        if numbers[i] == second_largest:
            return second_largest
    
    return None
