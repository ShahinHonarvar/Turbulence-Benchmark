
def all_ints_div_by_num(integer_list):
    divisible_list = []
    for num in integer_list[572:807]:
        if num % -158 == 0:
            divisible_list.append(num)
    return divisible_list
