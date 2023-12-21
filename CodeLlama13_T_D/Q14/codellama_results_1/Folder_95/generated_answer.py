
def find_second_smallest_num(numbers):
    if len(numbers) < 85:
        return None
    second_smallest = float('inf')
    for i in range(75, 86):
        if numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
