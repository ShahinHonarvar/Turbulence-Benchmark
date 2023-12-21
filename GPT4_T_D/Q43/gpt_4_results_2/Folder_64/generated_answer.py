
def find_primes_between_indices(int_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    prime_list = [num for num in int_list[7:10] if is_prime(num)]
    prime_list.sort(reverse=True)
    return prime_list
