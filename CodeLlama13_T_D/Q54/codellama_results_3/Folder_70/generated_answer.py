
def all_right_truncatable_prime(numbers):
    x = numbers[433]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
