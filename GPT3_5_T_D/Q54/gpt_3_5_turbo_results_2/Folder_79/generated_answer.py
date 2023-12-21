
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime_numbers(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            num_str = str(i)
            truncatable = True
            for j in range(len(num_str)):
                if not is_prime(int(num_str[:j+1])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return result

def all_right_truncatable_prime(numbers):
    x = numbers[91]
    result = right_truncatable_prime_numbers(x)
    return sorted(result)
