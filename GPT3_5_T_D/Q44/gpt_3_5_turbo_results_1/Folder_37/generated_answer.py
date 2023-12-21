
def composite_nums_between_indices(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    res = set()
    for num in lst[:6]:
        if not is_prime(num):
            res.add(num)
    return res
