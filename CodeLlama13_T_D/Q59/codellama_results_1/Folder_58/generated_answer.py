
def all_left_truncatable_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if str(num).startswith('0'): continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and all(int(str(num)[1:]) % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)
