
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_composite(n):
        return not is_prime(n)

    result = set()
    for i in range(7):
        if i >= len(lst):
            break
        if is_composite(lst[i]):
            result.add(lst[i])

    return result
