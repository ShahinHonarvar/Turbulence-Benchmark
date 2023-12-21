
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composite_set = set()
    for index in range(90, min(201, len(num_list))):
        if is_composite(num_list[index]):
            composite_set.add(num_list[index])
    return composite_set
