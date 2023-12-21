
def find_smallest_num(numbers):
    smallest = None
    for i in range(527, 538 + 1):
        if smallest is None or numbers[i] < smallest:
            smallest = numbers[i]
    return smallest
