
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False

    composite_set = set()
    for i in range(533, min(606, len(num_list))):
        if is_composite(num_list[i]):
            composite_set.add(num_list[i])
    return composite_set
