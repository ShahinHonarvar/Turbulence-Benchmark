
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_prime(num) and '0' not in str(num) and len(str(num)) > 1:
            result.append(num)
    return sorted(result)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
