
def find_smallest_num(numbers):
    smallest = None

    for i in range(6, 9):
        if smallest is None or numbers[i] < smallest:
            smallest = numbers[i]

    return smallest
