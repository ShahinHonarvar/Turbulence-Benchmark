
def find_largest_num(numbers):
    largest = -1
    for i in range(60, 201):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest
