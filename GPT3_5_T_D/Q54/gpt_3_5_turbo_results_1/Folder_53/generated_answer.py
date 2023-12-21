
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            num_str = str(num)
            is_truncatable = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:-i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result, reverse=True)
