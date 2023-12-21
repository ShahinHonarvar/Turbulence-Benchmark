
def composite_nums_between_indices(num_list):
    def check_if_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composite_nums_set = set()
    for num in num_list[0:9]:
        if check_if_composite(num):
            composite_nums_set.add(num)
    return composite_nums_set
