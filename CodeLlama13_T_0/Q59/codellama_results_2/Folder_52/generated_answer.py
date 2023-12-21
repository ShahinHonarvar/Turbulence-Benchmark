
def all_left_truncatable_prime(numbers):
    x = numbers[52]
    prime_list = []
    for i in range(x):
        if is_prime(i) and not contains_zero(str(i)):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
