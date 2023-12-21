
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    result = []
    for i in range(x-1, 0, -1):
        if is_prime(i):
            truncatable = True
            for j in range(len(str(i))-1):
                if not is_prime(int(str(i)[j+1:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return result
