
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[39]
    results = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            temp = num
            while temp > 10:
                temp //= 10
                if not is_prime(temp):
                    truncatable = False
                    break
            if truncatable:
                results.append(num)
    return sorted(results)
