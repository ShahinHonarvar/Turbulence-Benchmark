
def all_right_truncatable_prime(tuple_of_positives):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n%2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n_str = str(n)
        while len(n_str) > 0:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True

    x = tuple_of_positives[88]
    result = []

    for i in range(2, x):
        if is_right_truncatable(i):
            result.append(i)

    return sorted(result)
