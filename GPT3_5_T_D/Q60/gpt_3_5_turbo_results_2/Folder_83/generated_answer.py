
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if num < 10:  # Skip single-digit numbers
            continue
        str_num = str(num)
        if '0' in str_num:  # Skip numbers with 0
            continue
        if is_prime(num):
            is_truncatable_prime = True
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(num)
    return sorted(result)
