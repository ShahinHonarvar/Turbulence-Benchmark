
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[975]
    result = []
    for i in range(x - 1, 0, -1):
        if is_prime(i):
            is_right_truncatable = True
            number = str(i)
            while is_right_truncatable and len(number) > 1:
                number = number[:-1]
                if not is_prime(int(number)):
                    is_right_truncatable = False
            if is_right_truncatable:
                result.append(i)
    return sorted(result, reverse=True)
