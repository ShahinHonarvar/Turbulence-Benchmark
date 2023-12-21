
def all_left_right_truncatable_prime(tup):
    x = tup[77]

    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: return False
        return True

    def check_prime(num):
        if '0' in str(num): return False
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:len(str(num)) - i])):
                return False
        return True

    return sorted([num for num in range(11, x + 1) if is_prime(num) and check_prime(num)])
