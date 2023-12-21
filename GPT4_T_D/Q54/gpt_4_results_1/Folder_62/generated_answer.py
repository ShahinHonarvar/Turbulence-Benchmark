
def all_right_truncatable_prime(values):
    x = values[70]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n**0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_val = str(n)
        for i in range(len(str_val)):
            if not is_prime(int(str_val[i:])):
                return False
        return True

    results = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(results)
