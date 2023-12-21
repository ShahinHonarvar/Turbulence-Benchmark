
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[30]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        is_truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(i)
    return sorted(result, reverse=True)
