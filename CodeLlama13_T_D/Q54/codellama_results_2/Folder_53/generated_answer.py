
def all_right_truncatable_prime(numbers):
    x = numbers[86]
    prime_list = []
    for i in range(x, 10**7 + 1):
        if is_prime(i) and is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
