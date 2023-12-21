
import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[89]
    result = []
    for num in range(x-1, 0, -1):
        if sympy.isprime(num) and '0' not in str(num):
            num_str = str(num)
            is_truncatable_prime = True
            for i in range(1, len(num_str)):
                if not sympy.isprime(int(num_str[i:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(num)
    return sorted(result, reverse=True)
