
def find_primes_between_indices(num_list):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in num_list[14:69] if is_prime(num)]
    prime_numbers.sort(reverse=True)
    return prime_numbers
