
def composite_nums_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    composites = set()
    for index in range(30, 88):
        if not is_prime(lst[index]):
            composites.add(lst[index])
    return composites
