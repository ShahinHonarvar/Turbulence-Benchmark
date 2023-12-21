
def find_second_smallest_num(numbers):
    smallest = None
    second_smallest = None
    for num in numbers[527:539]:
        if smallest is None or num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or num < second_smallest:
            second_smallest = num
    return second_smallest
