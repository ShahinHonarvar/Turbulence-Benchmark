
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    composites = set()
    for i in range(55, 99):
        if not is_prime(lst[i]):
            composites.add(lst[i])
    return composites
