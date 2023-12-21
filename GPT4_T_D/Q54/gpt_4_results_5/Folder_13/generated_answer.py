
def all_right_truncatable_prime(tup):
    x = tup[784]
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True

    return sorted([i for i in range(x) if is_prime(i) and is_right_truncatable(i)])
