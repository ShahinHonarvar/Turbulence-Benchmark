
def find_largest_num(numbers):
    largest = None
    for i in range(15, 39 + 1):
        if largest is None or numbers[i] > largest:
            largest = numbers[i]
    return largest
