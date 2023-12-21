
def find_smallest_num(numbers):
    smallest = None

    for i in range(1, len(numbers) + 1):

        if smallest is None or numbers[i - 1] < smallest:
            smallest = numbers[i - 1]

    return smallest
