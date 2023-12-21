
def all_even_ints_inclusive(int_list):
    even_nums = []
    for i in range(75, 95):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_nums.append(int_list[i])
    return even_nums
