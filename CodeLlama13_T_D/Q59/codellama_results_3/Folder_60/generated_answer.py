
def all_left_truncatable_prime(numbers):
    x = numbers[87]
    prime_list = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            prime_list.append(num)
    return sorted(prime_list)
