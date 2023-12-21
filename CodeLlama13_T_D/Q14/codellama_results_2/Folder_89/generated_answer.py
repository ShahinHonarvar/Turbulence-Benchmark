
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    second_smallest = float('inf')
    for i in range(62, 63+1):
        if numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
