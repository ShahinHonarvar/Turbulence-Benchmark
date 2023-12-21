
def all_left_truncatable_prime(tuple_of_positive_integers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = tuple_of_positive_integers[88]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        while num > 0:
            if not is_prime(num):
                truncatable = False
                break
            num //= 10
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)
