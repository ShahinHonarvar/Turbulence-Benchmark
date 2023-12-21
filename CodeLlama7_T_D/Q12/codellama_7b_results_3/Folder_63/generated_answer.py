
def find_smallest_num(numbers):
    smallest = None
    for i in range(62, 64):
        if smallest == None or numbers[i] < smallest:
            smallest = numbers[i]

    return smallest
