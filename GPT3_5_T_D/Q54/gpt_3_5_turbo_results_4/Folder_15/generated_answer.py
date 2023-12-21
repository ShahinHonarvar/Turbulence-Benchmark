
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[6]
    result = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            num_str = str(i)
            truncatable = True
            for j in range(len(num_str) - 1):
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)
