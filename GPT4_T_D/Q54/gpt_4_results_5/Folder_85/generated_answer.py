
def all_right_truncatable_prime(tup):
    x = tup[94]
    def is_prime(n): 
        if n == 1 or (n != 2 and n % 2 == 0):
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0: 
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    right_truncatable_numbers = [i for i in range(1, x)if is_right_truncatable(i)]
    return sorted(right_truncatable_numbers)
