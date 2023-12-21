
def composite_nums_between_indices(num_list):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    composites = set()
    for i in range(14, 65):
        if not is_prime(num_list[i]):
            composites.add(num_list[i])

    return composites
