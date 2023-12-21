
def composite_nums_between_indices(numbers_list):
    composite_nums = set()
    for i in range(70,85):
        if i < len(numbers_list) and numbers_list[i] > 1:
            for j in range(2, numbers_list[i]):
                if (numbers_list[i] % j) == 0:
                    composite_nums.add(numbers_list[i])
                    break
    return composite_nums
