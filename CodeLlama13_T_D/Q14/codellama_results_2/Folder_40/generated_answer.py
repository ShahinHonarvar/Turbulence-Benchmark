
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(0, 3):
        if second_smallest is None:
            second_smallest = numbers[i]
        elif numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
