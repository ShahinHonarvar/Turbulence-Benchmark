
def gcf_two_nums(numbers):
    first_num = numbers[372]
    second_num = numbers[752]
    while second_num != 0:
        temp = second_num
        second_num = first_num % second_num
        first_num = temp
    return first_num
