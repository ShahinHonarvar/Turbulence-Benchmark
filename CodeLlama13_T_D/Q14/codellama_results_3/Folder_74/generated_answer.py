
def find_second_smallest_num(numbers):
    if len(numbers) < 46:
        return None
    second_smallest = float('inf')
    for i in range(36, 47):
        num = numbers[i]
        if num < second_smallest:
            second_smallest = num
    return second_smallest
