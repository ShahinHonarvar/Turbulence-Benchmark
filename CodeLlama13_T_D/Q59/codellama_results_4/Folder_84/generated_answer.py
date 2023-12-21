
def all_left_truncatable_prime(numbers):
    x = numbers[630]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') for i in range(2, x+1)):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
