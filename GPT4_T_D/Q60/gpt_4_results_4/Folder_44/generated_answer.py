
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    def is_left_right_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        length = len(num_str)
        for i in range(length):
            left = num_str[i:]
            right = num_str[:length-i]
            if not (isprime(int(left)) and isprime(int(right))):
                return False
        return True

    x = numbers[39]
    result = []
    for n in range(2, x + 1):
        if is_left_right_truncatable(n):
            result.append(n)
    return sorted(result)
