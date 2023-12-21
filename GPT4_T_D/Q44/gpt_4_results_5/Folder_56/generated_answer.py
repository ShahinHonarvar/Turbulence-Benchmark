
def composite_nums_between_indices(int_list):
    composite_nums = set()
    if len(int_list) > 0:
        for i in range(1):
            if int_list[i] > 1:
                for j in range(2, int_list[i]):
                    if (int_list[i] % j) == 0:
                        composite_nums.add(int_list[i])
                        break
    return composite_nums
