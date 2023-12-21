
def all_ints_div_by_num(numbers):
    divisible_nums = []
    for i in range(421, 490):
        if numbers[i] % 885 == 0:
            divisible_nums.append(numbers[i])
    return divisible_nums
