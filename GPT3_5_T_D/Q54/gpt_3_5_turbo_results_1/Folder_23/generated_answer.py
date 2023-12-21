
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    result = []
    for i in range(x-1, 1, -1):
        num = str(i)
        is_right_truncatable_prime = True
        while is_right_truncatable_prime and len(num) > 1:
            num = num[:-1]
            if not is_prime(int(num)):
                is_right_truncatable_prime = False
        if is_right_truncatable_prime:
            result.append(i)
    return sorted(result, reverse=True)
