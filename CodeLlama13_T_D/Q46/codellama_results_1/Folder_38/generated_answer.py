
def gcf_three_nums(numbers):
    gcf = numbers[14]
    for i in range(15, 22):
        if numbers[i] % gcf != 0:
            return -1
    return gcf
