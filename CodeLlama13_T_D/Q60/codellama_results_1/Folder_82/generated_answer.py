
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if str(num).count("0") == 0 and is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable(num):
    while len(str(num)) > 1:
        if not is_prime(int(str(num)[1:])):
            return False
        num //= 10
    return True

def is_right_truncatable(num):
    while len(str(num)) > 1:
        if not is_prime(int(str(num)[:-1])):
            return False
        num = int(str(num)[1:])
    return True
