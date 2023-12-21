
def all_left_truncatable_prime(numbers):
    x = numbers[70]
    result = []
    for i in range(2, x+1):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
