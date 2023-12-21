
def find_second_smallest_num(numbers):
    # Find the second smallest number in the list
    second_smallest = None
    for i in range(19, 93):
        if numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
