
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    composites = set()
    for num in lst[74:96]:
        if not is_prime(num):
            composites.add(num)

    return composites
