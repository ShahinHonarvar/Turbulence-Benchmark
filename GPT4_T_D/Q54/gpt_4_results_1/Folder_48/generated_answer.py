
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2): 
            return False
        else: 
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    def is_right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[:len(n_str)-i])):
                return False
        return True

    x = tup[835]
    result = []

    for i in range(2, x):
        if is_prime(i) and is_right_truncatable(i):
            result.append(i)

    return sorted(result)
