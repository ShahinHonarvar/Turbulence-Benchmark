
def find_second_smallest_num(numbers):
    second_smallest = None
    for i in range(1, 8):
        if numbers[i] < numbers[i - 1]:
            continue
        if second_smallest is None or numbers[i] < second_smallest:
            second_smallest = numbers[i]
    return second_smallest
