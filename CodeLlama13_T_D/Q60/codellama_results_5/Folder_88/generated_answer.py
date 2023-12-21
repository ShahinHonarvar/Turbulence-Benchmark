
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_and_right_truncatable_prime(num):
    if not isinstance(num, int) or num <= 0:
        return False
    for i in range(1, len(str(num)) // 2 + 1):
        if str(num)[i:-i] == "0":
            return False
        if not is_prime(int(str(num)[:-i])) or not is_prime(int(str(num)[i:])):
            return False
    return True

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
