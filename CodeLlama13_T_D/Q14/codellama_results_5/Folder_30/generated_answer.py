
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(26, 53):
        if numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
