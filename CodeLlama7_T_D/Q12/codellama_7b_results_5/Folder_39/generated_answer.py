
def find_smallest_num(numbers):
    smallest = float('inf')
    for i in range(52, 71 + 1):
        if numbers[i] < smallest:
            smallest = numbers[i]

    return smallest
