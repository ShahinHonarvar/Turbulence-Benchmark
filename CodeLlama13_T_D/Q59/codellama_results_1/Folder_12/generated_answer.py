
def all_left_truncatable_prime(numbers):
    x = numbers[70]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not any('0' in str(i) for _ in range(len(str(i))):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
