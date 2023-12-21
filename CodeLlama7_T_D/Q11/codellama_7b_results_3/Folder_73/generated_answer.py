
def find_largest_num(numbers):
    largest_num = None
    for i in range(19, 93):
        if largest_num is None or numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num
