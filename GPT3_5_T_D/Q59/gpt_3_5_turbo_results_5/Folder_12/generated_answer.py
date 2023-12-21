
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(numbers):
    x = numbers[70]
    results = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        is_truncatable_prime = True
        for j in range(len(str(i)), 0, -1):
            if not is_prime(int(str(i)[:j])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            results.append(i)
    return sorted(results, reverse=True)
