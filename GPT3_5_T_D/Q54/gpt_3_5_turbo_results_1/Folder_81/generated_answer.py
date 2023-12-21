
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[98]
    results = []

    for n in range(2, x):
        if is_prime(n):
            truncate = str(n)
            while truncate:
                if not is_prime(int(truncate)):
                    break
                truncate = truncate[:-1]
            else:
                results.append(n)

    return sorted(results)
