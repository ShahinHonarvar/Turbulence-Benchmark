
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def truncate_right(n):
    str_n = str(n)
    truncations = []
    for i in range(len(str_n)):
        truncations.append(int(str_n[:i+1]))
    return truncations

def all_right_truncatable_prime(numbers):
    x = numbers[46]
    result = []
    for i in range(x, 0, -1):
        if is_prime(i):
            truncations = truncate_right(i)
            all_prime = True
            for t in truncations:
                if not is_prime(t):
                    all_prime = False
                    break
            if all_prime:
                result.append(i)
    result.sort(reverse=True)
    return result
