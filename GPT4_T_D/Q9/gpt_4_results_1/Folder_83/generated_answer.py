
def all_odd_ints_inclusive(int_list):
    odd_nums = []
    for idx in range(90, 201):
        if idx < len(int_list) and int_list[idx] % 2 != 0:
            odd_nums.append(int_list[idx])
    return odd_nums
