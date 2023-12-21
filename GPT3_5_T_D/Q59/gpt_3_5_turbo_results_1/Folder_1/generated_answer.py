
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    result = []
    for n in range(x - 1, 0, -1):
        num_str = str(n)
        if '0' in num_str:
            continue
        truncatable_prime = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                truncatable_prime = False
                break
        if truncatable_prime:
            result.append(n)
    return result
