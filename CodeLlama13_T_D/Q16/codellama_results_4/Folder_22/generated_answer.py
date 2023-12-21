
def sum_even_ints_inclusive(my_list):
    even_nums = []
    for i in range(40, 42):
        if my_list[i] % 2 == 0:
            even_nums.append(my_list[i])
    return sum(even_nums) or 0
