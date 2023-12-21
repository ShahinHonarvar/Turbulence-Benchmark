
def find_largest_num(numbers):
    largest = None
    for i in range(75, 86):
        if largest is None or numbers[i] > largest:
            largest = numbers[i]
    return largest
