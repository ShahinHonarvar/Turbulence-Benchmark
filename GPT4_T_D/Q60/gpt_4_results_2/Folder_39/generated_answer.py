
def all_left_right_truncatable_prime(t):
    from sympy import isprime

    def is_left_right_truncatable(n):
        num_str = str(n)
        if "0" in num_str:
            return False
        for i in range(len(num_str)):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:len(num_str)-i])):
                return False
        return True

    x = t[30]
    prime_numbers = [i for i in range(11, x+1) if isprime(i)]
    return sorted([i for i in prime_numbers if is_left_right_truncatable(i)], reverse=True)
