
def find_second_smallest_num(numbers):
    smallest = None
    second_smallest = None
    for i in range(686, 987):
        num = numbers[i]
        if smallest is None or num < smallest:
            smallest, second_smallest = num, smallest
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
