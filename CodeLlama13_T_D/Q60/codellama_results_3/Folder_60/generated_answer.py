
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(n):
    if n < 2 or any(d == 0 for d in str(n)):
        return False
    for i in range(1, int(len(str(n))/2)+1):
        if not is_prime(n) or not is_prime(int(str(n)[:-i])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
