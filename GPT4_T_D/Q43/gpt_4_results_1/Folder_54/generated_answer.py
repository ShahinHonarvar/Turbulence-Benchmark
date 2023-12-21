
def find_primes_between_indices(number_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    number_list = number_list[13:64]
    prime_numbers = [num for num in number_list if is_prime(num)]
    return sorted(prime_numbers)
