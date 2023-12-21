
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(n):
    if n < 10 or str(n).count("0") > 0:
        return False
    for i in range(len(str(n))-1):
        if not is_prime(int(str(n)[:i+1])) or not is_prime(int(str(n)[i+1:])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
