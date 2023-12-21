
def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    second_smallest = sorted(numbers)[1]
    for i in range(2, 4):
        if numbers[i] == second_smallest:
            return None
    return second_smallest
