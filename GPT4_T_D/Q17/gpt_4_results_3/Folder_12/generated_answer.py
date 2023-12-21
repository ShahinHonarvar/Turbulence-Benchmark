
def all_ints_div_by_both_two_nums(numbers):
    divisible_numbers = []
    for i in range(35, 65):
        if numbers[i] % -30 == 0 and numbers[i] % -95 == 0:
            divisible_numbers.append(numbers[i])
    return divisible_numbers
