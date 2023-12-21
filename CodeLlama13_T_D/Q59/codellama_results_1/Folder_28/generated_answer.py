
def all_left_truncatable_prime(numbers):
    x = numbers[19]
    prime_list = []
    for i in range(x):
        if is_prime(i) and '0' not in str(i):
            prime_list.append(i)
    return sorted(prime_list)
