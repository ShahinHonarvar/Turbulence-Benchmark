
def all_left_truncatable_prime(numbers):
    x = numbers[38]
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i) and not any('0' in str(i) for i in range(2, int(str(i)[1:]))):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
