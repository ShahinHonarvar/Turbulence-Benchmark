
def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = sorted(numbers)[-2]
    for i in range(len(numbers)):
        if numbers[i] == second_largest:
            return second_largest
    return None
