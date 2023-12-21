
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[55]
    result = []
    for num in range(2, x):
        num_str = str(num)
        if '0' not in num_str:
            is_truncatable_prime = True
            for i in range(len(num_str)):
                truncated_num = int(num_str[i:])
                if not is_prime(truncated_num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(num)
    return sorted(result)
