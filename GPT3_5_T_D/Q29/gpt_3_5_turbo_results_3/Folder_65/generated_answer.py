
def gcf_two_nums(numbers):
    num_1 = numbers[29]
    num_2 = numbers[53]

    while num_2:
        num_1, num_2 = num_2, num_1 % num_2

    return num_1
