
def all_left_truncatable_prime(tup):
    import sympy
    x = tup[8]

    def is_left_truncatable_prime(num):
        if '0' in str(num):
            return False
        else:
            for i in range(len(str(num))):
                if not sympy.isprime(int(str(num)[i:])):
                    return False
            return True

    left_truncatables = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatables.append(i)

    left_truncatables.sort(reverse=True)
    return left_truncatables
