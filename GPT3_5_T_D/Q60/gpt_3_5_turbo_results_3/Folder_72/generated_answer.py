
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    def is_truncatable_prime(n):
        if n < 10 and is_prime(n):
            return True
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[:i])) or not is_prime(int(n_str[i:])):
                return False
        return True

    x = numbers[31]
    result = []
    for num in range(x, 9, -1):
        if is_truncatable_prime(num):
            result.append(num)
            
    result.sort(reverse=True)
    return result
