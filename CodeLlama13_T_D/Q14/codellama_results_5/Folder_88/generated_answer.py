
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(6, 9):
        if numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
