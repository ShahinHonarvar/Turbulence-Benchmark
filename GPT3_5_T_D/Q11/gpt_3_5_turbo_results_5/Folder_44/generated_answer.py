
def find_largest_num(numbers):
    largest_num = numbers[13]
    for i in range(13, 69):
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return largest_num
