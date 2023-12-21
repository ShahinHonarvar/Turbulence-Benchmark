
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    results = []
    for i in range(2, x):
        if is_prime(i):
            temp = str(i)
            while len(temp) > 1:
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    break
            else:
                results.append(i)
    return sorted(results)
