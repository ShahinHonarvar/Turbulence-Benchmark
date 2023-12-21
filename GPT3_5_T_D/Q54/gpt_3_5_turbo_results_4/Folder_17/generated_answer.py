
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            is_right_truncatable = True
            n = num // 10
            while n != 0:
                if not is_prime(n):
                    is_right_truncatable = False
                    break
                n = n // 10
            if is_right_truncatable:
                result.append(num)
    result.sort(reverse = True)
    return result
