
def all_right_truncatable_prime(numbers):
    x = numbers[23]
    prime_list = []
    for i in range(x):
        if is_right_truncatable_prime(i, numbers):
            prime_list.append(i)
    return sorted(prime_list)
