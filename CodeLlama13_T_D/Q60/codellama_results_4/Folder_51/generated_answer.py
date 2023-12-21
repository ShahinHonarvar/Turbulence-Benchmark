
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_right_truncatable_prime(n):
    if n <= 1 or not isinstance(n, int) or str(n).find("0") != -1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
