
def all_right_truncatable_prime(numbers):
    x = numbers[1]
    prime_list = []
    for i in range(x, 0, -1):
        if is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_right_truncatable_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
