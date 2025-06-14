
def find_second_smallest_num(numbers):
    second_smallest = None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
