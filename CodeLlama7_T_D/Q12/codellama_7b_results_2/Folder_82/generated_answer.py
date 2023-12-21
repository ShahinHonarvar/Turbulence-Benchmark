
def find_smallest_num(numbers):
    smallest = float('inf')
    for i in range(20, 201):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest
