
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[466]
    result = []
    for i in range(x-1, 0, -1):
        if '0' in str(i):
            continue
        truncatable = True
        num_str = str(i)
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                truncatable = False
                break
            num_str = num_str[1:]
        if truncatable:
            result.append(i)
    return result
