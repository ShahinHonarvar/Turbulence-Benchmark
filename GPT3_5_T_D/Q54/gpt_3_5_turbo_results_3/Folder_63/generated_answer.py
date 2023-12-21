
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[88]
    result = []
    for num in range(2, x):
        if not is_prime(num):
            continue
        temp = str(num)
        is_right_truncatable_prime = True
        while len(temp) > 0:
            if not is_prime(int(temp)):
                is_right_truncatable_prime = False
                break
            temp = temp[:-1]
        if is_right_truncatable_prime:
            result.append(num)
    return sorted(result)
