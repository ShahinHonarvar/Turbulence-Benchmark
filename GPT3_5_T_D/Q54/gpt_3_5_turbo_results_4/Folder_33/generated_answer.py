
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    result = []
    for num in range(x-1, 1, -1):
        num_str = str(num)
        is_right_truncatable_prime = True
        while num_str:
            if not is_prime(int(num_str)):
                is_right_truncatable_prime = False
                break
            num_str = num_str[:-1]
        if is_right_truncatable_prime:
            result.append(num)
    return sorted(result, reverse=True)
