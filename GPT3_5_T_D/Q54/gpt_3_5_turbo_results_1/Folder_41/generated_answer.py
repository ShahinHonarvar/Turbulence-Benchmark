
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[46]
    result = []
    for number in range(x-1, 10, -1):
        prime = True
        truncated = number // 10
        while truncated > 0:
            if not is_prime(truncated):
                prime = False
                break
            truncated //= 10
        if prime:
            result.append(number)
    return sorted(result, reverse=True)
