
def find_smallest_num(numbers):
    smallest = None
    for i in range(0, 9):
        if smallest is None or numbers[i] < smallest:
            smallest = numbers[i]
    return smallest
