
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[87]
    result = []

    for num in range(2, x):
        if '0' in str(num):
            continue

        is_truncatable = True
        while len(str(num)) > 1:
            num = int(str(num)[1:])
            if not is_prime(num):
                is_truncatable = False
                break

        if is_truncatable:
            result.append(num)

    return sorted(result)
