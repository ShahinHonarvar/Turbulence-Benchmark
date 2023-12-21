
def find_second_smallest_num(numbers):
    if len(numbers) < 94:
        return None
    second_smallest = float('inf')
    for i in range(75, 95):
        if numbers[i] < second_smallest and numbers[i] != float('inf'):
            second_smallest = numbers[i]
    return second_smallest
