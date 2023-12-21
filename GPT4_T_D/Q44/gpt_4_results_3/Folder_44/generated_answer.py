
def composite_nums_between_indices(int_list):
    composite_nums = set()

    for i in range(64, 67):
        if i >= len(int_list):
            break
        num = int_list[i]

        if num <= 1:
            continue

        factor_found = False
        for j in range(2, num):
            if num % j == 0:
                factor_found = True
                break

        if factor_found:
            composite_nums.add(num)

    return composite_nums
