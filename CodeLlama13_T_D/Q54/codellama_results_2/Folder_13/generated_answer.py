
def all_right_truncatable_prime(numbers):
    prime_list = []
    for num in numbers:
        if is_prime(num) and all(is_prime(num % 10**i) for i in range(len(str(num))-1)):
            prime_list.append(num)
    return sorted(prime_list)
