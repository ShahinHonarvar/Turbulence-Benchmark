
def all_left_truncatable_prime(numbers):
    x = numbers[3]
    prime_list = []
    for i in range(x-1, 0, -1):
        if is_prime(i) and '0' not in str(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
